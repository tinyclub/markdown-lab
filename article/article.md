% Markdown 文档模板
% Wu Zhangjin @ 泰晓科技
% \today

# 第一章 {#ch1}

这里是第一章。本文主要演示 Markdown 文档基本写法。

# 第二章

## 第二章第 1 节

- 列表1
- 列表2

## 第二章第 2 节

- **加粗**
- *斜体*
- 删除

## 第二章第 3 节

- [链接：泰晓科技首页](http://tinylab.org)

## 第二章第 4 节

- 泰晓科技域名地址

  ![Domain Name](./images/logo-login.png)

## 第二章第 5 节

这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。这里是一段很长的内容，用于测试能够自动进行中文换行。连续重复多次。

# 第三章

## 表格用法

| 篇数 | 作者  |
|-----:|:------|
|   24 | test1 |
|    6 | test2 |
|    5 | test3 |
|    4 | test4 |
|    4 | test5 |
|    3 | test6 |
|    2 | test7 |
|    2 | test8 |
|    2 | test9 |
|    1 | test10|
|    1 | test11|

## 命令用法

- 结果统计与排序

```bash
$ cat doc.md | grep "^-" | sort | uniq -c | sort -k1 -g -r
```

- 文档生成

```bash
$ pandoc -f markdown doc.md -o doc.pdf
	--toc -N --latex-engine=xelatex -V mainfont="WenQuanYi Micro Hei"
```

## 文本内命令

这里是文本内的 `command`。

## 代码块

### Python 代码

```python
# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]
print(reversed_string)

# Output
# EDCBA
```

### Java 代码

```Java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

## 上标/脚注

如何明确指定上标[^1]。

[^1]: 这里是一个上标。

## 链接

这里是一个[链接][2]。

[2]: http://tinylab.org "泰晓科技首页"

## 内部链接

点击[这里](#ch1)回到第一章。
