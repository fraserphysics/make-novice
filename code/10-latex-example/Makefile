include config.mk

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

## results.tex   : Generate Zipf summary table.
results.tex : $(DAT_FILES) $(ZIPF_SRC)
	$(ZIPF_EXE) --latex *.dat > $@
## file_list.tex : Generate list of files under version control, the source files
file_list.tex:
	echo "\\\begin{verbatim}\n$$ git ls-files" > $@
	git ls-files >> $@
	echo "\end{verbatim}" >> $@

## dats          : Count words in text files.
.PHONY : dats
dats : $(DAT_FILES)

%.dat : $(BOOKS)/%.txt $(COUNT_SRC)
	$(COUNT_EXE) $< $*.dat

%.head : %.dat
	head $< |awk '{print $$1, $$2}' > $@

## pngs          : Plot word counts.
.PHONY : pdfs
pdfs : $(PDF_FILES)

%.pdf : %.dat $(PLOT_SRC)
	$(PLOT_EXE) $*.dat $*.pdf

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
