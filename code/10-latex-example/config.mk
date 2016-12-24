# Directories for code and books
CODE=..
BOOKS=../../data/books

# Count words script.
COUNT_SRC=$(CODE)/wordcount.py
COUNT_EXE=python $(COUNT_SRC)

# Plot word counts script.
PLOT_SRC=$(CODE)/plotcount.py
PLOT_EXE=python $(PLOT_SRC)

# Test Zipf's rule
ZIPF_SRC=$(CODE)/zipf_test.py
ZIPF_EXE=python $(ZIPF_SRC)
