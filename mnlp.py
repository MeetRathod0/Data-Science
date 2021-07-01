"""
By Meet Rathod
Enrollmentno: 201806100610013
IMCA
"""
import math
from nltk.corpus import stopwords
import nltk
import pandas

class Text:
    specialChars=["\/",",","\\","*","!",".",";","\"","@","'","(",")","`",":","``"," ","%","&","$","''","�"]
    #  generate custom data frame param [list of docs, all words list,header name list(list must be same as docs length)]
    def getVector(self,docs:list,words:list,header:list): # return : pandas data frame
        doc=self.getDictZero(words)
        tmpDoc={}
        for i,docs in enumerate(docs):
            tmpLst=[0 for _ in range(len(doc))]
            for k,v in docs.items():
                flg=0
                for k1,v1 in doc.items():
                    if k == k1:
                        tmpLst[flg]=v
                    flg+=1 
            tmpDoc[header[i]]=tmpLst.copy()
            tmpLst.clear()
            
        df=pandas.DataFrame(tmpDoc,index=doc.keys())
        return df

    # find unique words param: (words list) 
    def getUniqueWords(self,wordlst:list): # return : dict
        udict={}
        for i in wordlst:
            i=i.lower()
            if i not in udict.keys():
                if i not in self.specialChars:
                    udict[i]=0  
            if i in udict.keys():
                udict[i]+=1
        return udict
    
    # find long sentance param: (list of sentences)
    def findLongSent(self,docSent): # return : list [doc num, length,sentence number]
        longSents={}
        for i,sents in enumerate(docSent):
            lst=[]
            for sent in sents:
                lst.append(len([i for i in sent]))
            longSents[str(i+1)]=lst.copy()
            lst.clear()

        value=0
        key=""
        for k,v in longSents.items():
            tmp=v
            v.sort()
            high=v[-1]
            if high > value:
                value=high
                key=k
                index=tmp.index(high)
        return [key,value,index]

    # remove empty character param: (list)
    def rmEmpty(self,lst:list): # return : list
        while '' in lst:
            lst.remove('')
        return lst

    # remove similar words param: (list)
    def rmSimilar(self,lst:list): # return : list
        dt=dict()
        for i in lst:
            dt[i]=0
        return list(dt.keys())

    # count number of words occurs
    def countWordsOccur(self,doc): # return : dict (word:number of occurence)
        dt=dict()
        for i in doc:
            if i not in dt.keys():
                dt[i]=0
            if i in dt.keys():
                dt[i]+=1
        return dt
    # remove stopwords param: (string)
    def rmStopWords(self,doc:str): # return : list
        lst=[]
        stop=stopwords.words("english")
        doc=nltk.word_tokenize(doc)
        for i in doc:
            if i.lower() not in stop:
                if i not in self.specialChars:
                    lst.append(i.lower())
        return self.rmEmpty(lst)
    
    # generate empty dict with 0 value param: (string)
    def getDictZero(self,lst:list): # return : dict
        wordDoc = dict.fromkeys(self.rmSimilar(lst),0)
        return wordDoc

    # comute TF param: (document , all document list)
    def computeTF(self,wordDict:list, doc:list): # return dict
        tfDict = {}

        wordDict=self.getDictZero(wordDict)
        # remove similar words
        doc=self.rmSimilar(doc)
    
        corpusCount = len(doc)
        # count num of  words occur in doc
        for i in doc:
            for k in wordDict.keys():
                if i == k:
                    wordDict[k]=0+1
        # count tf
        for word, count in wordDict.items():
            tfDict[word] = count/float(corpusCount)
        
        return tfDict

    # compute IDF param: (number of documents)
    def computeIDF(self,docList): # return : dict
        idfDict = {}
        # num of docs
        N = len(docList)

        lst=[]
        # merge all docs
        for doc in docList:
            lst+=doc

        # convert dict from list with 0 value
        idfDict = dict.fromkeys(lst, 0)
        
        # count number of words occur in doc
        for key in lst:
            for i in idfDict.keys():
                if i==key:
                    idfDict[key]+=1

        # generate idf
        for word, val in idfDict.items():
            idfDict[word] = math.log10(N / float(val))
    
        return idfDict

    # compute term weight param: (TF dict,IDF dict)
    def computeTW(self,tf,idf): # return : dict
        TW={}
        for k,v in idf.items():
            for tk,tv in tf.items():
                if k==tk:
                    TW[k]=v*tv
        return TW

    def computeCosineSimilarity(self,tw1,tw2,alldoc):
        wordDoc1=self.getDictZero(self.rmSimilar(alldoc))
        wordDoc2=self.getDictZero(self.rmSimilar(alldoc))
    
        for tk,tv in tw1.items():
            wordDoc1[tk]=tv
            
        for tk,tv in tw2.items():
            wordDoc2[tk]=tv

        l1=[i for i in wordDoc1.values()]
        l2=[i for i in wordDoc2.values()]

        N=len(l1)  

        tmpa=0
        asqrt = 0
        bsqrt = 0
        for i in range(N):
            tmpa += l1[i]*l2[i]
            asqrt += l1[i]**2
            bsqrt += l2[i]**2

        cosine = tmpa / (math.sqrt(asqrt)*math.sqrt(bsqrt))
        return cosine

    def computeJaccardSimilarity(self,list1, list2):
        s1 = set(list1)
        s2 = set(list2)
        return float(len(s1.intersection(s2)) / len(s1.union(s2)))