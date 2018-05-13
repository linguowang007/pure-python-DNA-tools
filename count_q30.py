#! /data/home/lingw/anaconda3/bin/python
# -*- coding: utf-8 -*-
import sys
import gzip
import itertools
from collections import Counter

fastq = sys.argv[1]  # a .gz format fastq file as the only input

with gzip.open(fastq, 'rt') as f:
    quality_lines = (i.strip() for i in itertools.islice(f, 3, None, 4))  # start from 3, end of file, step is 4
    quality_count = Counter(itertools.chain.from_iterable(quality_lines))

total_base = sum(quality_count.values())
q10 = sum(value for key, value in quality_count.items() if ord(key) - 43 >= 0)  # q10 base count
q20 = sum(value for key, value in quality_count.items() if ord(key) - 53 >= 0)  # q20 base count
q30 = sum(value for key, value in quality_count.items() if ord(key) - 63 >= 0)  # q30 base count

print(fastq, total_base, q10, q20, q30, sep='\t')  # print the fastq file, total base, q10 , q20 , q30 to stander output
