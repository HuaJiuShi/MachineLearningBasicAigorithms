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

def sigmoid(z):
    return 1/(1+np.exp(-z))

def GetCostGrad(theta, X, y):
    m, _ = X.shape
    tem = X.dot(theta)
    hypothesis = sigmoid(tem)
    delta = y*np.log(hypothesis) + (1-y)*np.log(1-hypothesis)
    J = -np.sum(delta)/m
    grad = ((hypothesis-y)*np.transpose(X)).sum(axis=1)/m
    return J, grad

def GetNewThetas(theta, grad, learningRate):
    temp = theta - learningRate*grad
    return temp
    
def StartGradientDescent(theta, X, y, learningRate, num):
    cost = np.zeros(num)
    for i in range(num):
        cost[i], grad = GetCostGrad(theta, X, y)
        print('cost[%d]= %f' %(i,cost[i]))
        theta = GetNewThetas(theta, grad, learningRate)   #梯度下降更新参数
    
    #绘制图像
    PlotResults(cost, X, y, theta)
    print(theta)
    
#绘制图像，使结果可视化
def PlotResults(cost, X, y, theta):
    num = cost.shape
    num = num[0]
    plt.figure("Cost")
    plt.plot(np.linspace(1, num, num),cost)
    plt.scatter(np.linspace(1, num, num),cost)
    plt.title('Cost')
    plt.show()

#LinerRegression Init
def LinerRegressionInit(samples):
    m, n = samples.shape
    X = samples[:,0:n-1]
    X = np.column_stack((np.ones(m),X))
    y = samples[:,n-1]
    #随机初始化theta
    #theta = np.random.normal(0,1,n)
    theta = np.zeros(3)
    return X, y, theta
    
def main():
    sampleRaw = []
    num = 0
    data = open('ex2data1.csv','r')
    for temp in data:
        num = num + 1
        temp = temp.split(',')
        sampleRaw.append([float(temp[0]),float(temp[1]),int(temp[2][0])])
        
    samples = np.array(sampleRaw)
    
    X, y, theta = LinerRegressionInit(samples)
    print(X)
    print(theta)
    
    StartGradientDescent(theta, X, y, 0.0005, 10)


if __name__ == '__main__':
    main()
    
    
    
    