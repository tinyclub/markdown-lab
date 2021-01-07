# Based on https://github.com/mwhite/resume but improved for gravatar and Chinese support

SRC = $(wildcard *.md)

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
LATEX_TEMPLATE=./templates/default.latex
LATEX_HEADER=./templates/header.tex
HTML_CSS=./templates/resume.css

LINK_COLOR ?= Green

# encryption: empty to disable, nonempty to enable
ENCRYPT ?=
OWNERPW ?= $(ENCRYPT)
USERPW  ?= $(ENCRYPT)
ifneq ($(OWNERPW)$(USERPW), $(ENCRYPT))
  ENCRYPT := $(OWNERPW)$(USERPW)
endif

all:    clean $(PDFS) $(HTML)

pdf:   clean $(PDFS)
html:  clean $(HTML)

%.html: %.md
	python resume.py html $(GRAVATAR_OPTION) < $< \
	  | pandoc -t html -c $(HTML_CSS) -o $@

%.pdf:  %.md $(LATEX_TEMPLATE)
	python resume.py tex < $< \
	  | pandoc --latex-engine=xelatex \
	      --template=$(LATEX_TEMPLATE) \
		-V colorlinks -V urlcolor=$(LINK_COLOR)\
		$(if $(ENCRYPT),-V encrypt:$(ENCRYPT) -V ownerpw:$(OWNERPW) -V userpw:$(USERPW)) \
		$(if $(WATERMARK),-V watermark:$(WATERMARK)) \
		-H $(LATEX_HEADER) \
		-o $@

ifeq ($(OS),Windows_NT)
  # on Windows
  RM = cmd //C del
else
  # on Unix
  RM = rm -f
endif

clean:
	$(RM) *.html *.pdf

read: $(PDFS)
	(chromium-browser $^ 2>&1 > /dev/null &) 2>&1 >/dev/null

read-html: $(HTML)
	(chromium-browser $^ 2>&1 > /dev/null &) 2>&1 >/dev/null
