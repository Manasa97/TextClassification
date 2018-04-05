from nltk.corpus import gutenberg
from nltk import *
import nltk
import math
from nltk.util import ngrams
import pickle

def compute_prob(cfd,fileno,N,mod_count):
    rescfd = cfd
    for i in cfd.keys():
        for j in cfd[i].keys():
            rescfd[i][j]=[cfd[i][j],math.log((cfd[i][j]/N),2)]
    rescfd['unk']=[mod_count,(mod_count/N)]

    pickle.dump(rescfd,open('op_tri_2.txt','wb'))

noOfFiles=1
#fileids=['bryant-stories.txt','carroll-alice.txt','shakespeare-hamlet.txt']
fileids=['shakespeare-hamlet.txt']

lenFirstSent=[len(gutenberg.sents(fileids[i])[0])-1 for i in range(noOfFiles)]
C=[list(gutenberg.words(fileids[i])[lenFirstSent[i]:]) for i in range(noOfFiles)]
lenC=[len(C[i]) for i in range(noOfFiles)]

v = len(set(C[0]))
mod_count = 1/(len(C[0])+len(set(C[0])))


S=[list(gutenberg.sents(fileids[i])[1:]) for i in range(noOfFiles)]
'''
bigram_iter=[]
bigram=[]
cfd_bi=[]
for i in range(noOfFiles):
    bigram_iter.append([])
    bigram.append([])
    for j in S[i]:
        bigram_iter[i].append(ngrams(j,2))
    for j in bigram_iter[i]:
        for k in j:
            bigram[i].append(k)
    N=len(bigram[i])
    cfd_bi.append(nltk.ConditionalFreqDist(bigram[i]))
    compute_prob_bi(cfd_bi[i],i,N,mod_count)
'''
#generate trigram counts
trigram_iter=[]
trigram=[]
cfd_tri=[]
for i in range(noOfFiles):
    trigram.append([])
    trigram_iter.append([])
    for j in S[i]:
        trigram_iter[i].append(ngrams(j,3))
    for j in trigram_iter[i]:
        for k in j:
            trigram[i].append(k)
    N=len(trigram[i])
    condition_pairs = (((w0, w1), w2) for w0, w1, w2 in trigram[i])
    cfd_tri.append(nltk.ConditionalFreqDist(condition_pairs))
    compute_prob(cfd_tri[i],i,N,mod_count)

'''
ip=[]
i = input("Enter text:")
ip = i.split()
ip_bigrams=[]
ip_bigrams = list(nltk.bigrams(ip))
prob(res,ip_bigrams)
'''
