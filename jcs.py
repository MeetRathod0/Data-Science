from mnlp import Text
import pandas as pd

doc1="I like python"
doc2="I like JavaScript more than Python"
doc3="But i like java more than JavaScript"

obj=Text()

doc1words=obj.rmStopWords(doc1)
doc2words=obj.rmStopWords(doc2)
doc3words=obj.rmStopWords(doc3)

allDocs=doc1words+doc2words+doc3words

#TF
tfD1=obj.computeTF(doc1words,allDocs)
tfD2=obj.computeTF(doc2words,allDocs)
tfD3=obj.computeTF(doc3words,allDocs)

#IDF
idf=obj.computeIDF([doc1words,doc2words,doc3words])

#TW
twD1=obj.computeTW(tfD1,idf)
twD2=obj.computeTW(tfD2,idf)
twD3=obj.computeTW(tfD3,idf)

#COSINE
cosD12=obj.computeCosineSimilarity(twD1,twD2,allDocs)
cosD23=obj.computeCosineSimilarity(twD2,twD3,allDocs)
cosD13=obj.computeCosineSimilarity(twD1,twD3,allDocs)


doc1words=doc1.split(" ")
doc2words=doc2.split(" ")
doc3words=doc3.split(" ")

#JCS
jcs12=obj.computeJaccardSimilarity(doc1words,doc2words)
jcs23=obj.computeJaccardSimilarity(doc2words,doc3words)
jcs13=obj.computeJaccardSimilarity(doc1words,doc3words)

df=pd.DataFrame(
    {
    "Cosine":[cosD12,cosD23,cosD13],
    "Jaccard":[jcs12,jcs23,jcs13]
    },
    index=["Set 1: (s1,s2)","Set 1: (s2,s3)","Set 1: (s1,s3)"]
)

print(df)
