import math
class Statistic:
    # return mean
    def mean(self,lst:list):
        try:
            iter=0
            for i in lst:
                if str(i)!="nan":
                    iter+=i
            return iter/len(lst)
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0
    
    # return max
    def max(self,lst:list):
        try:
            lst=[i for i in lst]
            lst.sort()
            return lst[-1]
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0
    
    # return mean
    def min(self,lst:list):
        try:
            lst=[i for i in lst]
            lst.sort()
            return lst[0]
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0
    
    # return dict of mode: 'key'= string, value = number of occurance 
    def mode(self,lst:list):
        try:
            # convert into lower
            lst=[i.lower() for i in lst]
            unique=dict().fromkeys(lst,0)
            # count
            for i in lst:
                if i in unique.keys():
                    unique[i]=unique[i]+1
            #sort
            unique={k:v for k,v in sorted(unique.items(),key=lambda item:item[1])}
            return list(unique.keys())[-1]
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return ""

    # return dict of mode: 'key'= string, value = number of occurance 
    def multiMode(self,lst:list):
        try:
            # convert into lower
            lst=[i.lower() for i in lst]
            unique=dict().fromkeys(lst,0)
            # count
            for i in lst:
                if i in unique.keys():
                    unique[i]=unique[i]+1
            #sort
            unique={k:v for k,v in sorted(unique.items(),key=lambda item:item[1])}
            #get result if more than one same value
            result=dict()
            for k,v in unique.items():
                if unique[list(unique.keys())[-1]] == v:
                    result[k]=v
            return list(result.keys())

        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return {}

    # find median return: median
    def median(self,lst:list):
        try:
            lst=[i for i in lst]
            lst.sort()
            pos=(len(lst)+1)/2
            return lst[int(pos)]
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0

    # get range : return: number
    def range(self,lst:list):
        try:
            lst.sort()
            return lst[-1] - lst[0]
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0

    # get standard deviation & variation : default return standard deviation, set false to get standard variation
    def getStdDevVer(self,data:list,stddev=True):
        try:
            n=len(data)
            x=self.mean(data)

            xix=[]
            sum_xix=0
            for i in data:
                xix.append(i-x)
                sum_xix+=i-x

            xi2=[]
            sum_xi2=0
            for i in xix:
                xi2.append(i**2)
                sum_xi2+=i**2

            if stddev==False:
                # return standard variation
                return (sum_xi2/(n-1))
            else:
                # return standard deviation
                return math.sqrt(sum_xi2/(n-1))

        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0

    # get postion for IRQ : fraction
    def getPos(self,val:float):
        try:
            frac=int(val)-val
            if frac==0:
                return int(val)
            else:
                return int(val+1)
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0

    # get IRQ quartilles: return dict of quartiles
    def getQuartiles(self,data:list):
        try:
            n=len(data)
            q2=self.median(data)
            q1=q3=q4=0
            if n%2==0:
                pos=int(n/4)
                q1=data[pos-1]
                q3=data[pos+pos+pos-1]        
                q4=data[pos+pos+pos+pos-1]
            else:
                pos=self.getPos(n/4)
                q1=data[pos-1]
                q3=data[pos+pos+pos-1]        
                if pos+pos+pos+pos-1 >=n:
                    q4=data[pos+pos+pos+pos-2]
            return {"Q1":q1,"Q2":q2,"Q3":q3,"Q4":q4}
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return {"Q1":0,"Q2":0,"Q3":0,"Q4":0}

    # get upper bound : default is upper bound, make upper=False return lower bound
    def outlier(self,data:list,upper=True):
        try:
            data=self.getQuartiles(data)
            q1=data['Q1']
            q2=data['Q2']
            q3=data['Q3']
            q4=data['Q4']

            # IRQ
            IRQ=q3-q1
            if upper==True:
                # return upper bound
                return q3+(1.5*IRQ)
            else:
                # return lower bound
                return q1-(1.5*IRQ)

        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return 0


    # return dict of mode: 'key'= string, value = number of occurance 
    def wordChoice(self,lst:list):
        try:
            # convert into lower
            lst=[i.lower() for i in lst]
            unique=dict().fromkeys(lst,0)
            # count
            for i in lst:
                if i in unique.keys():
                    unique[i]=unique[i]+1
            #sort
            unique={k:v for k,v in sorted(unique.items(),key=lambda item:item[1])}
            #get result if more than one same value
            result=dict()
            for k,v in unique.items():
                if unique[list(unique.keys())[-1]] == v:
                    result[k]=v
            return result
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return {}

    #------Bining methods----
    # list devider
    def listDivide(self,lst, n):
        for i in range(0, len(lst), n): 
            yield lst[i:i + n]
    
    def binParition(self,data:list):
        try:
            data.sort()
            min=data[0]
            max=data[-1]
            part=round((max-min)/len(data))
            # get divide position
            pos=int(len(data)/part)
    
            bins=list(self.listDivide(data,pos))
            
            return bins
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return []
    
    def binMean(self,data:list):
        try:
            bins=self.binParition(data)
            binM=[]
            for bin in bins:
                mean=self.mean(bin)
                binM.append([ mean for _ in bin])
            return binM
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return []
    
    def binBoundary(self,data:list):
        try:
            bins=self.binParition(data)

            for bin in bins:
                min=bin[0]
                max=bin[-1]
                pos=len(bin)-1

                for idx,val in enumerate(bin):
                    if pos==idx:
                        bin[pos]=max
                        break
                    if abs(min-bin[idx+1]) <= abs(max-bin[idx+1]):
                        bin[idx+1]=min
                    else:
                        bin[idx+1]=max
            return bins
        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return []
    
    def binMedian(self,data:list):
        try:
            bins=self.binParition(data)
            binM=[]
            for bin in bins:
                median=self.median(bin)
                binM.append([ median for _ in bin])
            return binM

        except Exception as e:
            print(e,"\nLine no: ",e.__traceback__.tb_lineno)
            return []
    
    def dispBin(self,data:list):
        for i,v in enumerate(data):
            print("Bin ",i+1,": ",end="")
            for e in v:
                print(e,end=",")
            print('')
