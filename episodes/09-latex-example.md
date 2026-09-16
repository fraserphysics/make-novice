---
title: LaTeX Example
teaching: 15
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Illustrate using make for a report.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can one ensure that a paper is reproducible?

::::::::::::::::::::::::::::::::::::::::::::::::::

Here we wrap previous work in a LaTeX document.  An advantage of LaTeX
is that the source files are simply text files.  Thus you can manage
them with git and Make.

Begin by using git

```bash
$ git checkout 09-latex
```

Next list the files.

```bash
$ ls
```

```output
books  countwords.py  local.bib  Makefile  plotcounts.py  __pycache__  report.tex  testzipf.py
```

Now see how the default target would be built.

```bash
$ make -n
```

```output
python countwords.py books/abyss.txt abyss.dat
python plotcounts.py abyss.dat abyss.pdf
python countwords.py books/isles.txt isles.dat
python plotcounts.py isles.dat isles.pdf
python countwords.py books/last.txt last.dat
python plotcounts.py last.dat last.pdf
python countwords.py books/sierra.txt sierra.dat
python plotcounts.py sierra.dat sierra.pdf
python testzipf.py --latex  abyss.dat  isles.dat  last.dat  sierra.dat > results.tex
echo -e "\\\begin{verbatim}\n$ git ls-files" > file_list.tex
git ls-files >> file_list.tex
echo "\end{verbatim}" >> file_list.tex
head abyss.dat |awk '{print $1, $2}' > abyss.head
pdflatex report
bibtex report
pdflatex report
pdflatex report
```

The major new features in the python calls are that the plots
are in pdf format.  The other new features work with *LaTeX*

Now look at the Makefile.

Issue the following commands:

```bash
$ make help
```

```output
 all           : The default target is report.pdf
 results.tex   : Make a Zipf summary table in LaTeX format.
 file_list.tex : Make a list of files under version control, ie, source files
 report.pdf    : Build the pdf document
 report.bbl    : Build the bibliography for the report
 clean         : Remove the auto-generated files.
 variables     : Print selected variables.
```

```bash
$ make variables
```

```output
TXT_FILES: books/abyss.txt books/isles.txt books/last.txt books/sierra.txt
DAT_FILES: abyss.dat isles.dat last.dat sierra.dat
PLOT_FILES: abyss.pdf isles.pdf last.pdf sierra.pdf
```

Now make all of the PLOT_FILES

```bash
$ make last.pdf isles.pdf abyss.pdf sierra.pdf
```

:::::::::::::::::::::::::::::::::::: challenge

## Figure out how make builds the plots

Work with your neighbor

:::::::::::::::::::::::::::::::: solution

## Solution

Look at the pattern rules for %.dat and %.pdf

```make
# EG makes abyss.dat from books/abyss.txt
%.dat : books/%.txt countwords.py
	python countwords.py $< $*.dat

# EG makes abyss.pdf from abyss.dat
%.pdf : %.dat plotcounts.py
	python plotcounts.py $*.dat $*.pdf
```

::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::

Next, make and examine the targets file_list.tex and results.tex

```bash
$ make file_list.tex
```

```output
echo -e "\\\begin{verbatim}\n$ git ls-files" > file_list.tex
git ls-files >> file_list.tex
echo "\end{verbatim}" >> file_list.tex
```

```bash
$ cat file_list.tex
```

```output
\begin{verbatim}
$ git ls-files
Makefile
config.mk
local.bib
report.tex
\end{verbatim}
```

This is the list of files wrapped in LaTeX markup,

```bash
$ make results.tex
```

```output
python3 ../testzipf.py --latex  last.dat  isles.dat  abyss.dat  sierra.dat > results.tex
```

```bash
$ cat results.tex
```

```output
Book & First & Second & Ratio\\ \hline
last & 12244 & 5566 & 2.20 \\
isles & 3822 & 2460 & 1.55 \\
abyss & 4044 & 2807 & 1.44 \\
sierra & 4242 & 2469 & 1.72 \\
```

and this is a table of the calculated word count ratios.

Now make the default target and examine the result

```bash
$ make
$ evince report.pdf &
```

:::::::::::::::::::::::::::::::::::: challenge

## Putting part of the Makefile in the document

Section 1.1 begins with an excerpt from the Makefile.  How does that
get into the document?  Implement a solution that instead copies
lines from the Makefile into the document.

:::::::::::::::::::::::::::::::: solution

## Solution

Add the following target to the Makefile

```make
makefile_tail.tex: Makefile
		echo -e "\\\begin{verbatim}" > $@
		tail -3 $< >> $@
		echo "\end{verbatim}" >> $@
```

and put the following into report.tex

```bash
\input{makefile_tail.tex}
```

::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- make can document how you got your results.
- make can simplify trying a variation of your analysis.
- make saves time by automating repetitive work.
- make saves time by only rebuilding things that might change.

::::::::::::::::::::::::::::::::::::::::::::::::::


