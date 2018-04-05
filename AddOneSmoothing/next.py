import pickle
from nltk.corpus import gutenberg
from nltk import *
import nltk
import math
from nltk.util import ngrams

cfd_bi=[]
cfd_tri=[]

for i in range(3):
    cfd_bi.append(pickle.load(open('op_bi_'+str(i)+'.txt','rb')))
    cfd_tri.append(pickle.load(open('op_tri_'+str(i)+'.txt','rb')))

def prob(train,test):
    total = 0
    for i in test:
        if i[0] in train.keys():
            if i[1] in train[i[0]].keys():
                total+=train[i[0]][i[1]][1]
            else:
                total+=train['unk'][1]
        else:
            total+=train['unk'][1]
    if(total<0):
        total = total*(-1)
    return total

ip=[]
i = input("Enter text:")
ip = i.split()
ip_bigrams=[]
ip_bigrams = list(nltk.bigrams(ip))
p0 = prob(cfd_bi[0],ip_bigrams)
p1 = prob(cfd_bi[1],ip_bigrams)
p2 = prob(cfd_bi[2],ip_bigrams)
p = [p0,p1,p2]
if(max(p) == p0):
    print("bryant")
elif(max(p) == p1):
    print("carroll")
else:
    print("shakespeare")