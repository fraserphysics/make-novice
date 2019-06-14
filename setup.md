---
layout: page
title: "Setup"
root: .
---

## Files

You need to clone a git repository to get files to follow this lesson.
We've made a seperate branch in the repository for each episode so
that as we transition from one episode to the next you can save your
work on the old branch and check-out the next branch to get files that
are identical to the ones the instructor is using.  Here are the
steps:

1. Open a Bash shell window.

2. (Optional) Navigate to a convenient directory.

3. Use the following git command to fetch the necessary files:

   ~~~
   $ git clone https://github.com/fraserphysics/setup_make_novice.git make-lesson
   ~~~
   {: .language-bash}

4. Change into the `make-lesson` directory:

   ~~~
   $ cd make-lesson
   ~~~
   {: .language-bash}

5. Verify that you have a branch for each episode:

   ~~~
   $ git branch -a
   ~~~
   {: .language-bash}

	~~~
	* 01-intro
	remotes/origin/01-intro
	remotes/origin/02-makefiles
	remotes/origin/03-variables
	remotes/origin/04-dependencies
	remotes/origin/05-patterns
	remotes/origin/06-variables
	remotes/origin/07-functions
	remotes/origin/08-self-doc
	remotes/origin/09-latex
	remotes/origin/HEAD -> origin/01-intro
	~~~
	{: .output}

## Software

You also need to have the following software installed on your computer to
follow this lesson:

### GNU Make

#### Linux

Make is a standard tool on most Linux systems and should already be available.
Check if you already have Make installed by typing `make -v` into a terminal.

One exception is Debian, and you should install Make from the terminal using
`sudo apt-get install make`.

#### OSX

You will need to have Xcode installed (download from the
[Apple website](https://developer.apple.com/xcode/)).
Check if you already have Make installed by typing `make -v` into a terminal.

#### Windows
Use the Software Carpentry [Windows installer](https://github.com/swcarpentry/windows-installer).

### Python

Python2 or Python3 (preferred), Numpy and Matplotlib are required.
They can be installed separately, but the easiest approach is to install
Anaconda python <https://www.continuum.io/downloads> which includes all of the
necessary python software.

### LaTeX (Optional)

The last episode uses the LaTeX document preparation system.  If you
find it difficult to install, simply listen to the discussion for that
episode without doing any of the exercises.
