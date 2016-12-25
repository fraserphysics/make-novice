BOOKS=../../data/books
TXT_FILES=$(wildcard $(BOOKS)/*.txt)
DAT_FILES=$(patsubst $(BOOKS)/%.txt, %.dat, $(TXT_FILES))
PDF_FILES=$(patsubst $(BOOKS)/%.txt, %.pdf, $(TXT_FILES))

## report.pdf    : Build document that is default target
report.pdf: report.bbl 
	pdflatex report
	pdflatex report
report.aux: report.tex $(PDF_FILES) results.tex file_list.tex abyss.head
	pdflatex report

## report.bbl    : Build bibliography for report
report.bbl: local.bib report.aux
	bibtex report

## results.tex   : Make Zipf summary table.
results.tex : $(DAT_FILES) ../zipf_test.py
	python ../zipf_test.py --latex *.dat > $@

## file_list.tex : Make list of files under version control, ie, source files
file_list.tex:
	echo "\\\begin{verbatim}\n$$ git ls-files" > $@
	git ls-files >> $@
	echo "\end{verbatim}" >> $@

## dats          : Count words in text files.
.PHONY : dats
dats : $(DAT_FILES)

%.dat : $(BOOKS)/%.txt ../wordcount.py
	python ../wordcount.py $< $*.dat

## %head         : Print the first two fields of the first ten lines of %dat
%.head : %.dat
	head $< |awk '{print $$1, $$2}' > $@

%.pdf : %.dat ../plotcount.py
	python ../plotcount.py $*.dat $*.pdf

## clean         : Remove auto-generated files.
.PHONY : clean
clean :
	rm -f $(DAT_FILES)
	rm -f *.head *.pdf
	rm -f results.txt
	rm -f report.aux report.blg report.bbl report.log file_list.tex results.tex

## variables     : Print variables.
.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)
	@echo DAT_FILES: $(DAT_FILES)
	@echo PDF_FILES: $(PDF_FILES)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
