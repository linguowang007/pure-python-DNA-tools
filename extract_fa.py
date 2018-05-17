#! /data/home/lingw/anaconda3/bin/python
# -*- coding: utf-8 -*-
import sys

fa = sys.argv[1]  # input a fasta file
ids = sys.argv[2:]  # input one or many fasta ids

with open(fa) as f:
    at_body = False
    for line in f:
        if line.startswith('>'):  # header line
            header = line.split()[0][1:]
            if header not in ids:
                at_body = False
                continue
            print(line, end='')
            at_body = True
        elif at_body:  # body line
            print(line, end='')
