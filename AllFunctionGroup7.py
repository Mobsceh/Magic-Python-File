#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
def Fibon():
  output = 0
  n0 = 1  
  n1 = 2  
  while n0 <= 4000000:
    if n0 % 2 == 0:
      output += n0
    n0, n1 =n1, n0 + n1
  return output

def Digit():
  d=""
  output = 1
  for i in range(1, 185186):
    d+=str(i)
  for i in range(7):
    output *= int(d[10**i - 1])
  return output


def Sunday_Count():
    def Day_finder(d, m, y):
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        y -= m < 3
        return (( y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7)
    count=0
    for i in range(1901, 2001):
      for j in range(1, 13):
        if Day_finder(1, j, i)==0:
          count+=1
    return(count)

def String_manipulator (s):
  t=""
  for i in s:
    if (i.isalpha()):
            t+=i
  return t.swapcase()

def UpLow (s):
  l_count=0
  u_count=0
  for i in s:
    if (i.islower()):
      l_count+=1
    if (i.isupper()):
      u_count+=1
  return [l_count, u_count]

def Name_checker(s):
  r= False
  if s.isalpha() and (s[0].isupper() and s[1:].islower()):
    r=True
  return r

def Name_checker_2(L):
  for i in range(len(L)):
    for j in L[i].split():
      if Name_checker(j):
        r=i
        return r
  return -1

def Maximum_Neg (L):
  g=[]
  [g.append(i) for i in L if i<0]
  if len(g)==0:
    return 0
  return max(g) 

def MaxNegMat_row (M):
    g=[]
    rw=np.shape(M)[0]
    for i in range(rw):
        g.append(Maximum_Neg(list(M[i,:])))
    return np.array(g).reshape (rw,-1), sum(g) 

def MaxNegMat_col (M):
  g=[]
  l=np.shape(M)[1]
  for i in range(l):
    g.append(Maximum_Neg(list(M[:,i])))
  return np.array(g).reshape (-1, l), sum(g)  

def Trap(a, b, f, H=0.001):
  N=int((b-a)/H)
  x=np.linspace(a, b, N+1)
  Z=0
  for i in range(1, N+1):
    Z+=H*((f(x[i-1])+f(x[i]))/2)
  return Z

def non_linear_solver (s):
  x,y=s
  F=np.empty([2])
  F[0]=x**2+y+x-4
  F[1]=2*(np.exp(x))+3*y-14
  return F

def EulerMethod(a,b,c,N,f):
  x=np.linspace(a,b,N)
  H=x[1]-x[0]
  y=np.zeros(len(x))
  y[0]=c
  for i in range(0, N-1):
    y[i+1] = y[i] + f(x[i], y[i]) * H
  return x, y 


def RK2Method (a,b,c,N,f):
  x=np.linspace(a,b,N)
  y=np.zeros(len(x))
  H=x[1]-x[0]
  y[0]=c
  for i in range(0, N-1):
    y[i+1] = y[i] + H * f( x[i] + (H / 2.0), y[i] + ((H/2) * f(x[i], y[i] )))
  return x, y

def model(y,x):
    dydt = (2*y)+(np.exp(2*x))
    return dydt

def  MatGenerator(a,b,lamda,alp,beta,N,g):
    h=(b-a)/N
    R=-np.eye(N+1,N+1,k=-1)+2*np.eye(N+1,N+1,k=0)-np.eye(N+1,N+1,k=1)
    A=(lamda**2/h**2)*R
    x=np.linspace(a,b,N+1)
    B=np.empty((N+1))
    B[0]=g(x[0])+alp*(lamda**2/h**2)
    B[N]=g(x[N])+beta*(lamda**2/h**2)
    for i in range(1,N):
        B[i]=g(x[i-1])

    return A,B
