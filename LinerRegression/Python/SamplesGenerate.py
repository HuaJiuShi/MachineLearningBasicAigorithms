#!/usr/bin/python
#-*- coding:utf-8 -*-


'''
All Rights Reserved by THX
This programme is used to generate samples.
'''

import numpy as np
import random
import csv
import matplotlib.pyplot as plt

def OriginalFunction2D(x):
    a = 10.93
    b = 8.32
    return a*x + b
    

#在0-100范围内生成2维随机样本
def SamplesGenerate2D(num, writefile):
    sample2D = np.zeros((num,2))    #构造num行，2列的2维矩阵
    writer = csv.writer(writefile)
    for i in range(num):
        sample2D[i,0] = random.random()*100
        sample2D[i,1] = OriginalFunction2D(sample2D[i,0]) + random.uniform(-1,1)*random.uniform(0,random.uniform(0,200))
        
    writer.writerows(sample2D)
    x = sample2D[:,0]
    y = sample2D[:,1]
    plt.scatter(x,y)
    plt.show()
    

def main():
    csvfile = open('Sample2D.csv', 'w', newline='')
    SamplesGenerate2D(20,csvfile)
    print('Generate Success!!!')
    
if __name__ == '__main__':
    main()
    
