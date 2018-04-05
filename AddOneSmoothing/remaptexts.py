from nltk.corpus import gutenberg
from nltk import *
import nltk
import math
from nltk.util import ngrams
import pickle

vocablist=[]

def findNC(cfd,c):
    nc=0
    retcfd={}
    for i in cfd:
        retcfd[i]=set([j for j in cfd[i] if cfd[i][j]==c])
        nc+=len(retcfd[i])
    return nc,retcfd

        
def GoodTuring(cfd,filenum,ngram,N):
    ncp1,cfd1=findNC(cfd,0)
    n6,cfd_6=findNC(cfd,6)
    n1,cfd_1=findNC(cfd,1)
    rescfd=cfd    
    factor=float(6*n6/n1)
    for count in range(6):
        nc=ncp1
        cfd0=cfd1
        ncp1,cfd1=findNC(cfd,count+1)
        val=math.ceil(((count+1)*(ncp1/nc)-count*factor)/(1-factor))
        for j in cfd:
            rescfd[j].update(dict.fromkeys(cfd0[j],val))
    for j in cfd:
        rescfd[j]={k:[rescfd[j][k],math.log(rescfd[j][k]/N,2)] for k in rescfd[j]}
       
    #file=open('cfd_'+ngram+'_'+str(filenum)+'.txt','wb')
    file=open('cfd_'+ngram+'_2.txt','wb')
    pickle.dump(rescfd,file)
    file.close()
    

makeunk={'delay', 'search', 'peering', 'currants', 'tumbled', 'remain', 'account', 'drinking', 'houses', 'hollow', 'roughly', 'crawling', 'pleasing', 'attended', 'share', 'burning', 'warning', 'swallowed', 'grant'}

noOfFiles=1
#fileids=['bryant-stories.txt','carroll-alice.txt','shakespeare-hamlet.txt']
fileids=['shakespeare-hamlet.txt']

lenFirstSent=[len(gutenberg.sents(fileids[i])[0])-1 for i in range(noOfFiles)]
C=[list(gutenberg.words(fileids[i])[lenFirstSent[i]:]) for i in range(noOfFiles)]
lenC=[len(C[i]) for i in range(noOfFiles)]


S=[list(gutenberg.sents(fileids[i])[1:]) for i in range(noOfFiles)]

'''
for i in range(noOfFiles):
    #file=open('words_new_'+str(i)+'.txt','ab+')
    #file_sents=open('sents_new_'+str(i)+'.txt','ab+')
    #file=open('words_new_0.txt','ab+')
    #file_sents=open('sents_new_0.txt','ab+')
    C[i]=['unk' if word in makeunk else word for word in C[i]]
    pickle.dump(C[i],file)
    file.close()
    for k in range(len(S[i])):
        S[i][k]=['unk' if word in makeunk else word for word in S[i][k]]
    pickle.dump(S[i],file_sents)
    file_sents.close()
'''
#7 seconds
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
    vocab=set(C[i])
    vocablist=['<s>']+list(vocab)+['<e>']                          
    for j in cfd_bi[i]:
        newval=vocab-set(cfd_bi[i][j].keys())
        cfd_bi[i][j].update(dict.fromkeys(newval,0))
    print(cfd_bi[i]['the'].values())
#GoodTuring(cfd_bi[i],i,'bi',N)

'''
#generate trigram counts
trigram_iter=[]
trigram=[]
cfd_tri=[]
for i in range(noOfFiles):
    trigram.append([])
    trigram_iter.append([])
    for j in S[i]:
        trigram_iter[i].append(ngrams(j,3,pad_left=True,pad_right=True,left_pad_symbol='<s1>',right_pad_symbol='<e1>'))
    for j in trigram_iter[i]:
        for k in j:   
            trigram[i].append(k)
    N=len(trigram[i])
    condition_pairs = (((w0, w1), w2) for w0, w1, w2 in trigram[i])        
    cfd_tri.append(nltk.ConditionalFreqDist(condition_pairs))
    vocab=set(C[i])
    for j in cfd_tri[i]:
        newval=vocab-set(cfd_tri[i][j].keys())
        cfd_tri[i][j].update(dict.fromkeys(newval,0))
      
    GoodTuring(cfd_tri[i],i,'tri',N)
    
    
'''