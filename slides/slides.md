% Ftrace 实现原理和产品开发实践
% 吴章金 @ 魅族科技
% \today

# 什么是 Ftrace

## Linux tracing overview

## Ftrace itself

# Ftrace 实现原理

## Ftrace function tracer footstone: -pg

以 MIPS 为例：`arch/mips/kernel/mcount.S`

* `gcc -pg`

```
    $ echo 'main(){}' | \
      mipsel-linux-gnu-gcc -x c -S -o - - -pg | grep mcount
	subu	$sp,$sp,8		# _mcount pops 2 words from  stack
	jal	_mcount
```

* `gcc -finstrument-functions`

```
    $ echo 'main(){}' | \
      mipsel-linux-gnu-gcc -x c -S -o - - \
      -finstrument-functions | egrep "enter\)|exit\)"
	lw	$25,%call16(__cyg_profile_func_enter)($28)
	lw	$25,%call16(__cyg_profile_func_exit)($28)
```

## Dynamic function tracing

以 MIPS 为例：`arch/mips/kernel/ftrace.c`

* 编译阶段
    * `scripts/recordmcount.{pl,c}` 扫描所有 `.text` 中的 `mcount` 调用点并创建`__mcount_loc` 段

* 引导阶段
    * 调用 `ftrace_process_locs` 把所有 `mcount` 调用点替换为 nop 指令：`ftrace_make_nop()`

* 跟踪阶段
    * 调用 `ftrace_run_update_code`，替换回 `mcount` 调用点：`ftrace_make_call()`

## Function Graph tracer

* 模拟实现 `__cyg_profile_func_exit`

* 在 `_mcount` 中记录、劫持并恢复函数返回地址
    * `prepare_ftrace_return`
        * 记录，劫持并模拟enter：`ftrace_push_return_trace`
    * `return_to_handler`
        * 用于劫持原有的返回地址
        * 然后调用 `ftrace_return_to_handler`
            * 模拟exit：`ftrace_pop_return_trace`
        * 恢复原来的返回地址并跳回

## High resolution trace clock: `sched_clock`

* `sched_clock` 要求
    * 高精度：`us/ns`
        * `kernel/sched_clock.c` 定义的 `sched_clock` 基于 `jiffies`，精度不够
    * 快速高效
        * 无锁，直接读硬件计数器，X86：`rdtsc/rdtscll`，MIPS: `read_c0_count()`
        * `Cycles` 转 `ns` 算法优化：`arch/x86/include/asm/timer.h`
    * 不能溢出
        * 32 位转 64 位：`include/linux/cnt32_to_63.h: cnt32_to_63()`

* notrace
    * 不能跟踪，否则会死循环
    * `_mcount() -> sched_clock() -> _mcount()`

## User space tracing

* 可通过 `trace_marker` 模拟实现应用程序跟踪
* 实例：Systrace
    * atrace_init_once()
        * `atrace_marker_fd = open("/sys/kernel/debug/tracing/trace_marker", O_WRONLY);`
    * `ATRACE_BEGIN(name)/ATRACE_END()` 写 `trace_marker`
    * `ATRACE_BEGIN(name)`
        * `snprintf(buf, ATRACE_MESSAGE_LENGTH, "B|%d|%s", getpid(), name);`
        * `write(atrace_marker_fd, buf, len);`
    * `ATRACE_END()`
        * `char c = 'E'; write(atrace_marker_fd, &c, 1);`

# Ftrace 产品开发实践

## Latency v.s. throughput

* Latency tracing
    * irqsoff tracer: 用于跟踪系统延迟
    * `echo irqsoff > /sys/kernel/debug/tracing/current_tracer`

* Max Latency：+10ms
    * 主要延迟在 USB driver: `dwc3_interrupt()` 中
    * 观察后发现是 `dwc3_interrupt()` 没有线程化

* 中断线程化
    * 增加 `dwc3_thread_interrupt()`，数据延迟到此处理
    * 参照 [drivers/usb/dwc3/gadget.c](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/drivers/usb/dwc3/gadget.c) 线程化

* Latency 消失，但造成 Throughput 衰退
    * 发现 RNDIS 下降明显
    * 线程化前：91／72
    * 线程化后：45／39

## Graphic perf tuning

## Power/Thermal/Network tracing

## CPUIdle tracing

## Filesystem tracing

# Ftrace 在线演示

## Linux Lab 介绍

* 基于 Qemu 的嵌入式 Linux 开发环境
* 首页：<http://tinylab.org/linux-lab>
* 仓库：<https://github.com/tinyclub/linux-lab>
* 特性
    * Docker 容器化
    * 可通过 Web 访问的 LXDE Desktop（基于noVNC）
    * 预安装 4 大架构的交叉编译器
    * 集成 Uboot, Linux Kernel, Buildroot
    * 支持大量 Qemu 虚拟的开发板
    * 灵活配置、编译和引导

## Linux Lab 介绍（Cont.）

\ThisCenterWallPaper{1.0}{images/linux-lab}

## Online Ftrace Demo

* Doc: doc/ftrace

* Linux Lab Host

```
    $ make list             # List supported boards
    $ make BOARD=malta boot
```

* Qemu Malta Board

```
    # tools/trace.sh function_graph "ls -l"
    # head -15 trace.log

    # tracer: function_graph
    #
    # CPU  DURATION                  FUNCTION CALLS
    # |     |   |                     |   |   |   |
     0)               |          unlock_page() {
     0)   0.541 us    |            page_waitqueue();
     0)   0.584 us    |            __wake_up_bit();
     0) + 16.333 us   |          }
```

## Online KFT Demo


* Doc: doc/kft/kft_kickstart.txt

* Linux Lab Host

```
    $ scripts/feature.sh kft v2.6.36 malta
```

* Qemu Malta Board

```
    # cat /proc/kft
    status: run id 0, primed, triggered, complete

    config:
      mode 0
      trigger start entry start_kernel
      trigger stop entry to_userspace
      filter mintime 500
      filter maxtime 0
      logentries 100000
```

## Online KFT Demo (Cont.)

```
    # cat /proc/kft_data
     Entry    Delta     PID        Function                        Caller
    -------- -------- -------- ----------------                 ------------
         686      876      0.0 start_kernel                     rest_init
        4954      717      0.0 clockevents_register_notifier    start_kernel
        6589     4913      0.0 printk                           start_kernel
        6663     4780      0.0 vprintk                          printk
        7128     1606      0.0 vscnprintf                       vprintk
        7208     1433      0.0 vsnprintf                        vscnprintf
        9437      583      0.0 vprintk                          printk
       10090     1198      0.0 release_console_sem              vprintk
       11687     4712      0.0 cpu_probe                        setup_arch
       11789     2419      0.0 cpu_probe                        setup_arch
       11855     2007      0.0 decode_configs                   cpu_probe
       11889     1066      0.0 decode_configs                   cpu_probe
       14418     1851      0.0 cpu_probe                        setup_arch
```
