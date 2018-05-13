#! /data/home/lingw/anaconda3/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import Counter
from operator import methodcaller
import gzip
import itertools

fastq = sys.argv[1]  # a .gz format fastq file as the only input

strip = methodcaller('strip')

c1 = Counter()
with gzip.open(fastq, 'rt') as f:
    for line in map(strip, itertools.islice(f, 3, None, 4)):  # start=3, stop=None, step=4
        c1.update(line)

total_base = sum(c1.values())
q10 = sum(value for key, value in c1.items() if ord(key) - 43 >= 0)  # q10 base count
q20 = sum(value for key, value in c1.items() if ord(key) - 53 >= 0)  # q20 base count
q30 = sum(value for key, value in c1.items() if ord(key) - 63 >= 0)  # q 30 base count

print(fastq, total_base, q10, q20, q30, sep='\t')  # print the fastq file, total base, q10 , q20 , q30 to stander output
