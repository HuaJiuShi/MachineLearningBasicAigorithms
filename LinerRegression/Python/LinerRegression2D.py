#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
All Rights Reserved by THX

This program is used to verify liner regression.
Samples are generated by SameplesGenerate.py.

Github:https://github.com/HuaJiuShi/MachineLearningBasicAigorithms.git
'''

import numpy as np
import csv
import matplotlib.pyplot as plt

#y = theta1*x + theta0
def GetCostGrad(theta, x, y):
    m, _ = x.shape  #Get x's Line Number
    h = (x * theta).sum(axis=1)   #Get Hypothesis
    error = h - y   #Get Error
    sumError = np.sum(error * error)    #Get the Sum of Error^2
    J = sumError/(2*m)
    grad = ((h - y)*np.transpose(x)).sum(axis=1)/m
    return J, grad               #Return the Cost J and grad
    
#使用梯度下降算法更新theta
#返回值：theta0，theta1
'''
def GetNewThetas(theta, x, y, learningRate):
    m, _ = x.shape
    h = (x * theta).sum(axis=1)
    temp0 = theta[0] - learningRate/m*np.sum((h - y)*x[:,0])
    temp1 = theta[1] - learningRate/m*np.sum((h - y)*x[:,1])
    return temp0,temp1
'''
def GetNewThetas(theta, grad, learningRate):
    temp = theta - learningRate*grad
    return temp

#开始梯度下降
def StartGradientDescent(theta, x, y, learningRate, num):
    cost = np.zeros(num)
    for i in range(num):
        print('theta0 = %f' %(theta[0]))
        print('theta1 = %f' %(theta[1]))
        cost[i], grad = GetCostGrad(theta, x, y)
        print('cost[%d]= %f' %(i,cost[i]))
        theta = GetNewThetas(theta, grad, learningRate)   #梯度下降更新参数
    
    #绘制图像
    plt.figure("Cost")
    plt.plot(cost)
    plt.title('Cost')
    
    plt.figure('Graphic')
    plt.scatter(x[:,1],y)
    finalLine = np.ones([2,2])
    finalLine[0,0] = 0
    finalLine[0,1] = theta[0]+theta[1]*0
    finalLine[0,0] = 100
    finalLine[0,1] = theta[0]+theta[1]*100
    plt.plot(finalLine[:,0],finalLine[:,1],'r')
    plt.title('Graphic')
    plt.show()
    
    
#LinerRegression Init
def LinerRegressionInit(sample2D):
    m, n = sample2D.shape
    x = np.column_stack((np.ones(m),sample2D[:,0]))
    y = sample2D[:,1]
    #随机初始化theta
    theta = np.random.normal(0,1,n)

    return x, y, theta


def main():
    #读取样本数据
    sample2Draw = []
    csvfile = open('Sample2D.csv', 'r') #只读模式打开样本文件
    data = csv.reader(csvfile)
    num = 0
    for temp in data:
        num = num + 1
        sample2Draw.append([float(temp[0]),float(temp[1])])
    sample2D = np.array(sample2Draw)
    
    #准备数据,初始化线性回归模型
    x, y, theta = LinerRegressionInit(sample2D)
    
    #运行梯度下降算法
    StartGradientDescent(theta, x, y, 0.0004, 20)
    
    
if __name__ == '__main__':
    main()
    
    
