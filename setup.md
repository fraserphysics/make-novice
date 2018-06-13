---
layout: page
title: "Setup"
root: .
---

## Files

You need to download some files to follow this lesson:

1. Open a Bash shell window.

2. (Optional) Navigate to a convenient directory.

3. Use the following git command to fetch the necessary files:

   ~~~
   $ git clone https://github.com/fraserphysics/setup_make_novice.git make-lesson
   ~~~
   {: .bash}

4. Change into the `make-lesson` directory:

   ~~~
   $ cd make-lesson
   ~~~
   {: .bash}

5. Verify that you have a branch for each episode:

   ~~~
   $ git branch -a
   ~~~
   {: .bash}
~~~
* 01-intro_py2
  remotes/origin/01-intro_py2
  remotes/origin/01-intro_py3
  remotes/origin/02-makefiles_py2
  remotes/origin/02-makefiles_py3
  remotes/origin/03-variables_py2
  remotes/origin/03-variables_py3
  remotes/origin/04-dependencies_py2
  remotes/origin/04-dependencies_py3
  remotes/origin/05-patterns_py2
  remotes/origin/05-patterns_py3
  remotes/origin/06-variables_py2
  remotes/origin/06-variables_py3
  remotes/origin/07-functions_py2
  remotes/origin/07-functions_py3
  remotes/origin/08-self-doc_py2
  remotes/origin/08-self-doc_py3
  remotes/origin/09-latex_py2
  remotes/origin/09-latex_py3
  remotes/origin/HEAD -> origin/01-intro_py2
~~~
{: .output}

## Software

You also need to have the following software installed on your computer to
follow this lesson:

### GNU Make

#### Linux

Make is a standard tool on Linux systems and should already be available.
Check if you already have Make installed by typing `make -v` into a terminal.

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
