import shutil
import subprocess
import os


with open()'QM.txt', 'r') as f:
    lines = f.readlines()

with open('QM.txt', 'w') as f:
    for line in lines:
        if line.startswith('1'):
            f.write(line)
