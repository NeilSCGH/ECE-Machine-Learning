import numpy as np
import matplotlib.pyplot as plt

nbEpoch=10
totalDataSize=40
pTraining=0.75

N=8
I=int(totalDataSize*pTraining)

X=np.random.randint(2, size=(totalDataSize,N))
Y=np.sum(X,axis=1).reshape((totalDataSize,1))
XTraining,XTesting = X[:I], X[I:]
YTraining,YTesting = Y[:I], Y[I:]

ones=np.ones((I,1))

def fwp(I,N,XTraining,Vf,Vx):
    #forward propagation
    Fs=[]
    F=np.zeros((len(XTraining),1))
    for t in range(0,N):
        input=XTraining[:,[t]] #column t
        F= F*Vf + input*Vx
        Fs.append(F)

    return Fs,F

def dEdVx(N,I,YOutput,YTraining,Vf,XTraining):
    sum=0
    for t in range(N):
        sum2=0
        for i in range(I):
            sum2+=(YOutput[i][0]-YTraining[i][0])*XTraining[i][t]
        sum+=sum2*(Vf**(N-t))

    return sum

def dEdVf(N,I,YOutput,YTraining,Vf,Fs):
    sum=0
    for t in range(N):
        sum2=np.sum((YOutput-YTraining)*Fs[t-1])
        #print("sum2",sum2)
        sum+=sum2*(Vf**(N-t))

    return sum

#initialisation
Vx=np.random.uniform(0,1)
Vf=np.random.uniform(0,1)
alpha=0.0001

for epoch in range(500):
    #("Vx",Vx," Vf",Vf)
    Fs,YOutput=fwp(I,N,XTraining,Vf,Vx)

    #compute the error
    E=np.sum(np.square(YOutput-YTraining))/2

    if epoch%50==0 : print(E)

    dEx=dEdVx(N,I,YOutput,YTraining,Vf,XTraining)
    dEf=dEdVf(N,I,YOutput,YTraining,Vf,Fs)
    #print("DEX",dEx," DEF",dEf)

    Vx=Vx-alpha*dEx
    Vf=Vf-alpha*dEf


# print(YOutput)
# print(YTraining)

print()
tmp,YOutputTest=fwp(I,N,XTesting,Vf,Vx)
E=np.sum(np.square(YOutputTest-YTesting))/2
print(E)