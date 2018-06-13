---
title: "LaTeX Example"
teaching: 15
exercises: 5
questions:
- "How can one ensure that a paper is reproducible?"
objectives:
- "Illustrate using make for a report."
keypoints:
   - "make can document how you got your results."
   - "make can simplify trying a variation of your analysis."
   - "make saves time by automating repetitive work."
   - "make saves time by only rebuilding things that might change."
---

Here we wrap previous work in a LaTeX document.  An advantage of LaTeX
is that the source files are simply text files.  Thus you can manage
them with git and Make.

Begin by using git

~~~
$ git checkout 09-latex_...
~~~
{: .bash}

Next list the files.

~~~
$ ls
~~~
{: .bash}

~~~
books  countwords.py  local.bib  Makefile  plotcounts.py  __pycache__  report.tex  testzipf.py
~~~
{: .output}

Now see how the default target would be built.

~~~
$ make -n
~~~
{: .bash}

~~~
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

~~~
{: .output}

The major new features in the python calls are that the plots
are in pdf format.  The other new features work with latex or *LaTeX*

Now look at the Makefile.

Issue the following commands:

~~~
$ make help
~~~
{: .bash}

~~~
 all           : The default target is report.pdf
 results.tex   : Make a Zipf summary table in LaTeX format.
 file_list.tex : Make a list of files under version control, ie, source files
 report.pdf    : Build the pdf document
 report.bbl    : Build the bibliography for the report
 clean         : Remove the auto-generated files.
 variables     : Print selected variables.
~~~
{: .output}

~~~
$ make variables
~~~
{: .bash}

~~~
TXT_FILES: books/abyss.txt books/isles.txt books/last.txt books/sierra.txt
DAT_FILES: abyss.dat isles.dat last.dat sierra.dat
PLOT_FILES: abyss.pdf isles.pdf last.pdf sierra.pdf
~~~
{: .output}

Now make all of the PLOT_FILES

~~~
$ make last.pdf isles.pdf abyss.pdf sierra.pdf
~~~
{: .bash}


> ## Figure out how make builds the plots
>
> Work with your neighbor
>
> > ## Solution
> >
> > Look at the pattern rules for %.dat and %.pdf
> > ~~~
> > # EG makes abyss.dat from books/abyss.txt
> > %.dat : books/%.txt countwords.py
> >	python countwords.py $< $*.dat
> >
> > # EG makes abyss.pdf from abyss.dat
> > %.pdf : %.dat plotcounts.py
> > python plotcounts.py $*.dat $*.pdf
> > ~~~
> > {: .make}
> {: .solution}
{: .challenge}

Next, make and examine the targets file_list.tex and results.tex
~~~
$ make file_list.tex
~~~
{: .bash}
~~~
echo -e "\\\begin{verbatim}\n$ git ls-files" > file_list.tex
git ls-files >> file_list.tex
echo "\end{verbatim}" >> file_list.tex
~~~
{: .output}
~~~
$ cat file_list.tex
~~~
{: .bash}
~~~
\begin{verbatim}
$ git ls-files
Makefile
config.mk
local.bib
report.tex
\end{verbatim}
~~~
{: .output}
This is the list of files wrapped in LaTeX markup,
~~~
$ make results.tex
~~~
{: .bash}
~~~
python3 ../testzipf.py --latex  last.dat  isles.dat  abyss.dat  sierra.dat > results.tex
~~~
{: .output}
~~~
$ cat results.tex
~~~
{: .bash}
~~~
Book & First & Second & Ratio\\ \hline
last & 12244 & 5566 & 2.20 \\
isles & 3822 & 2460 & 1.55 \\
abyss & 4044 & 2807 & 1.44 \\
sierra & 4242 & 2469 & 1.72 \\
~~~
{: .output}
and this is a table of the calculated word count ratios.

Now make the default target and eximine the result>
~~~
$ make
$ evince report.pdf &
~~~
{: .bash}

> ## Putting part of the Makefile in the document
>
> Section 1.1 begins with an excerpt from the Makefile.  How does that
> get into the document?  Implement a solution that instead copies
> lines from the Makefile into the document.
>
> > ## Solution
> > Add the following target to the Makefile
> > ~~~
> > makefile_tail.tex: Makefile
> >		echo -e "\\\begin{verbatim}" > $@
> >		tail -3 $< >> $@
> >		echo "\end{verbatim}" >> $@
> > ~~~
> > {: .make}
> > and put the following into report.tex
> > ~~~
> > \input{makefile_tail.tex}
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}
