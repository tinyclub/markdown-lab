# Author: Wu Zhangjin / Falcon <wuzhangjin@gmail.com>
# Update: 2014/01/17 PM 14:20

SRC = $(wildcard *.md)

html_theme=dzslides
latex_theme=Darmstadt

# colortheme: beaver,crane,dolphin,dove,fly,lily
# monarca,seagull,seahorse,spruce,wolverine
latex_colortheme=wolverine

# Put and select the .jpg's in images/, without suffix
# e.g. earth, white, darkgray; mx6, orange, black
titlepage_wallpaper=mx6
titlepage_titlefg=orange
titlepage_authorfg=black

# toc bg/fg
toc_number_bg=white
toc_number_fg=violet
toc_section_bg=white
toc_section_fg=orange

latex_template=./templates/zh_template.tex

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
IMGS=$(wildcard images/*.jpg)

all: clean $(PDFS) $(HTML)

pdf: $(PDFS)

html: $(HTML)

%.pdf: %.md $(latex_template) $(IMGS)
	@#sed -n ':a;1,5!{P;N;D;};N;ba' $< > tmp-$<
	sed '/^# 致谢/,$$d' $< > $<.tmp
	pandoc -t beamer \
	  -V titlepage_wallpaper:$(titlepage_wallpaper) \
	  -V titlepage_titlefg:$(titlepage_titlefg) \
	  -V titlepage_authorfg:$(titlepage_authorfg) \
	  -V toc_number_bg:$(toc_number_bg) \
	  -V toc_number_fg:$(toc_number_fg) \
	  -V toc_section_bg:$(toc_section_bg) \
	  -V toc_section_fg:$(toc_section_fg) \
	  -V colortheme:$(latex_colortheme) \
	  -V theme:$(latex_theme) -V fontsize:9pt $<.tmp -o $@ \
	  --toc --template=$(latex_template) --latex-engine=xelatex
	rm $<.tmp

%.html: %.md
	pandoc -t $(html_theme) -s --mathjax $< -o $@

read: $(PDFS)
	firefox $^ &

read-html: $(HTML)
	firefox $^

clean:
	rm -rf *.pdf *.html
