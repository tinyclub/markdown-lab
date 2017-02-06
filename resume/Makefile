# Based on https://github.com/mwhite/resume but improved for gravatar and Chinese support

SRC = $(wildcard *.md)

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
LATEX_TEMPLATE=./templates/default.latex
LATEX_HEADER=./templates/header.tex
HTML_CSS=./templates/resume.css

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
	      -H $(LATEX_HEADER) -o $@

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
	firefox $^ &

read-html: $(HTML)
	firefox $^ &
