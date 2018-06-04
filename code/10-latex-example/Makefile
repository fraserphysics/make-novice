include config.mk

TXT_FILES=$(wildcard $(BOOKS)/*.txt)
DAT_FILES=$(patsubst $(BOOKS)/%.txt, %.dat, $(TXT_FILES))
PLOT_FILES=$(patsubst $(BOOKS)/%.txt, %.pdf, $(TXT_FILES))

## all           : The default target is report.pdf
.PHONY : all
all : report.pdf

## results.tex   : Make a Zipf summary table in LaTeX format.
results.tex : $(DAT_FILES) $(TESTZIPF_SRC)
	$(TESTZIPF_EXE) --latex $(DAT_FILES) > $@

# EG makes abyss.dat from $(BOOKS)/abyss.txt
%.dat : $(BOOKS)/%.txt $(COUNTWORDS_SRC)
	$(COUNTWORDS_EXE) $< $*.dat

# EG makes abyss.pdf from abyss.dat
%.pdf : %.dat $(PLOTCOUNTS_SRC)
	$(PLOTCOUNTS_EXE) $*.dat $*.pdf

## file_list.tex : Make a list of files under version control, ie, source files
file_list.tex:
	echo -e "\\\begin{verbatim}\n$$ git ls-files" > $@
	git ls-files >> $@
	echo "\end{verbatim}" >> $@

# Print the first two fields of the first ten lines of %dat
%.head : %.dat
	head $< |awk '{print $$1, $$2}' > $@

## report.pdf    : Build the pdf document
report.pdf: report.bbl
	pdflatex report
	pdflatex report
report.aux: report.tex $(PLOT_FILES) results.tex file_list.tex abyss.head
	pdflatex report

## report.bbl    : Build the bibliography for the report
report.bbl: local.bib report.aux
	bibtex report

## clean         : Remove the auto-generated files.
.PHONY : clean
clean :
	rm -f $(DAT_FILES)
	rm -f *.head *.pdf
	rm -f results.txt
	rm -f report.aux report.blg report.bbl report.log file_list.tex results.tex

## variables     : Print selected variables.
.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)
	@echo DAT_FILES: $(DAT_FILES)
	@echo PLOT_FILES: $(PLOT_FILES)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
