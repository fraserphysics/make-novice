include config.mk

TXT_FILES=$(wildcard $(BOOKS)/*.txt)
DAT_FILES=$(patsubst $(BOOKS)/%.txt, %.dat, $(TXT_FILES))
PDF_FILES=$(patsubst $(BOOKS)/%.txt, %.pdf, $(TXT_FILES))
ZIPF_DIR=zipf_analysis
ZIPF_ARCHIVE=$(ZIPF_DIR).tar.gz

report.pdf: report.bbl $(PDF_FILES) results.tex file_list.tex
	pdflatex report
	pdflatex report
report.aux: report.tex local.bib
	pdflatex report
report.bbl: report.aux
	bibtex report

## results.tex : Generate Zipf summary table.
results.tex : $(DAT_FILES) $(ZIPF_SRC)
	$(ZIPF_EXE) --latex *.dat > $@
file_list.tex:
	echo "\\\begin{verbatim}\n$$ git ls-files" > $@
	git ls-files >> $@
	echo "\end{verbatim}" >> $@

## dats        : Count words in text files.
.PHONY : dats
dats : $(DAT_FILES)

%.dat : $(BOOKS)/%.txt $(COUNT_SRC)
	$(COUNT_EXE) $< $*.dat

## pngs        : Plot word counts.
.PHONY : pdfs
pdfs : $(PDF_FILES)

%.pdf : %.dat $(PLOT_SRC)
	$(PLOT_EXE) $*.dat $*.pdf

## clean       : Remove auto-generated files.
.PHONY : clean
clean :
	rm -f $(DAT_FILES)
	rm -f $(PDF_FILES)
	rm -f results.txt
	rm -rf $(ZIPF_DIR)
	rm -f $(ZIPF_ARCHIVE)

## variables   : Print variables.
.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)
	@echo DAT_FILES: $(DAT_FILES)
	@echo PDF_FILES: $(PDF_FILES)
	@echo ZIPF_DIR: $(ZIPF_DIR)
	@echo ZIPF_ARCHIVE: $(ZIPF_ARCHIVE)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
