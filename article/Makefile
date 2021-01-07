
SRC = $(wildcard *.md)
PDFS=$(SRC:.md=.pdf)
LATEX_TEMPLATE=./templates/default.tex
LATEX_HEADER=./templates/header.tex

# pygments / kate /monochrome /espresso /haddock /tango /zenburn
HIGHLIGHT_STYLE ?= espresso
# link-color
LINK_COLOR = Cyan

# encryption: empty to disable, nonempty to enable
ENCRYPT ?=
OWNERPW ?= $(ENCRYPT)
USERPW  ?= $(ENCRYPT)
ifneq ($(OWNERPW)$(USERPW), $(ENCRYPT))
  ENCRYPT := $(OWNERPW)$(USERPW)
endif

pdf: clean $(PDFS)

all: clean $(PDFS)

%.pdf: %.md
	pandoc --toc -N \
	  --latex-engine=xelatex \
	  --template=$(LATEX_TEMPLATE) \
	  -H $(LATEX_HEADER) \
	  --highlight-style $(HIGHLIGHT_STYLE) \
	  -V colorlinks -V urlcolor=$(LINK_COLOR) \
	  $(if $(ENCRYPT),-V encrypt:$(ENCRYPT) -V ownerpw:$(OWNERPW) -V userpw:$(USERPW)) \
	  $(if $(WATERMARK),-V watermark:$(WATERMARK)) \
	  -f markdown $< -o $@

read: $(PDFS)
	(chromium-browser $^ 2>&1 > /dev/null &) 2>&1 >/dev/null

clean:
	rm -rf *.pdf
