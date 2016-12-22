#!/usr/bin/env python
from wordcount import load_word_counts
import sys

def top_two_word(counts):
    """
    Given a list of (word, count, percentage) tuples, 
    return the top two word counts.
    """
    limited_counts = counts[0:2]
    count_data = [count for (_, count, _) in limited_counts]
    return count_data


if __name__ == '__main__':
    input_files = sys.argv[1:]
    print('''Book & First & Second & Ratio\\\\
    \\hline''')
    for input_file in input_files:
        counts = load_word_counts(input_file)
        [first, second] = top_two_word(counts)
        bookname = input_file[:-4]
        print("%s & %i & %i & %.2f \\\\" %(bookname, first, second, float(first)/second))

'''To Do: Argument parser in main that prints old way unless --latex.
Here are the old print statments:

    print("Book\tFirst\tSecond\tRatio")
        print("%s\t%i\t%i\t%.2f" %(bookname, first, second, float(first)/second))
'''
