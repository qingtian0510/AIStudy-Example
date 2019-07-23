#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


path = "../datasets/flower_photos"
sub_dirs = [x[0] for x in os.walk(path)]

for x in os.walk(path):
    print(x[0])

print(os.path.basename(sub_dirs[1]))
