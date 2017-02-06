
SRC = $(wildcard *.md)
PDFS=$(SRC:.md=.pdf)
LATEX_TEMPLATE=./templates/default.latex
LATEX_HEADER=./templates/header.tex

pdf: clean $(PDFS)

all: clean $(PDFS)

%.pdf: %.md
	pandoc --toc -N --latex-engine=xelatex --template=$(LATEX_TEMPLATE) -H $(LATEX_HEADER) \
		-f markdown $< -o $@

read: $(PDFS)
	firefox $^ &

clean:
	rm -rf *.pdf
