#! /data/home/lingw/anaconda3/bin/python
# -*- coding: utf-8 -*-
import sys
import gzip

fq = sys.argv[1]  # input a .gz format fastq file
ids = sys.argv[2]  # input a fastq id list file, per id one line

with open(ids) as f:
    id_set = {i.strip() for i in f}  # put all fastq ids in to a set

with gzip.open(fq, 'rt') as f:
    f = [f] * 4
    for a, *b in zip(*f):
        if not ids:
            break
        fq_id = a.split()[0][1:]
        if fq_id in id_set:
            id_set.remove(fq_id)
            print(a, *b, sep='', end='')
