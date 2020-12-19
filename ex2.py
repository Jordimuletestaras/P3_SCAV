import subprocess as sp
import numpy as np

if __name__ == '__main__':
    n=1
    files = []
    while (n==1):
        print("file name: (with extension)")
        name = input()
        files.append(name)
        print("Insert an other file? (1 = yes, 0 = no)")
        n = int(input())


    line = 'ffmpeg '

    for i in range(len(files)):
        line = line+ ' -i '+files[i]

    for i in range(len(files)):
        line = line + ' -map ' + str(i)

    print("output name (with extension)")
    out_name = input()

    line=line+' '+out_name
    print(line)
    sp.run(line, shell=True)
