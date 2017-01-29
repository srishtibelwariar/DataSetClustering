# points.py
# Srishti Belwariar

"""K MEANS CLUSTERING"""
import copy
import math
import random
import numpy


class Dataset(object):
    
    def __init__(self, dimension, contents=None):
        """
        Creates a DataSet object, which contains lists of points of any specified dimension (all points must be of same dimension) 
        """
        
        assert isinstance(dimension,int) and dimension>0
        assert (isinstance(contents,list) and len(contents[0])==dimension) or (contents==None)
        
        self._dimension=dimension
        
        
        if contents==None:
            clist=list()
            self._contents=clist
            
            
        else:
            clist = copy.deepcopy(contents)
            self._contents=clist
        
    
    def getDimension(self):
        return self._dimension
    
    def getSize(self):
        if self._contents==None:
            size=0

        size=len(self._contents)
        return size
    
    def getContents(self):
        return self._contents
    
    def getPt(self, i):
        pt=self._contents[i]
        return list(pt)
        
    
    def addPt(self,point):
        assert isinstance(point,list) and len(point)==self._dimension
        return self._contents.append(list(point))
        
        
   
class Cluster(object):
   
    
    def __init__(self, data, centroid):
        """ 
        A Cluster is a group of data points in the dataset.  This is represented as a list of the indicies of points in the dataset that belong to the respective cluster.
        This class will also provide a centroid for the respective cluster
        
        """
        assert isinstance(data,Dataset)
        assert isinstance(centroid,list) and len(centroid)==data.getDimension()
        self._centroid=list(centroid)
        self._dataset= data
        self._index=list()
        

    def getCentroid(self):
        return self._centroid
    
    def getIndex(self):
        return self._index
    
    def addIndex(self, index):
        assert isinstance(index,int) and (index>=0 and index<=self._dataset.getSize()-1)
        if not (index in self._indices):
            self._index.append(index)
  
    def clear(self):
        self._index=list()
            
    
    def getContents(self):
        listing=list(self._dataset.getContents())
        
        new=list()
        for x in self._index:
            new.append(listing[x])
        return new
    
        """
        new=list()
        for x in sorted(self._indices):
            i=self._indices[x]
            poi=self._dataset.getPoint(i)
            new.append(poi)
        return new
        
        
            #poi=self._dataset[i]
    
        
        
            ind=self._indices[x]
            poi=listing[ind]
            new.append(poi)
        return new
        """
        
        
   
    def distance(self, point):
        
        assert isinstance(point,list) and len(point)==self._dataset.getDimension()
        
        cent=self._centroid
        counts=0.00
        Dimensions=len(point)
        
        for r in range(0,Dimensions):
            x= float(point[r])-float(cent[r])
            fx= x**2
            counts=counts+fx
        
        dis= float(math.sqrt(counts))
        return dis
    
    def updateCentroid(self):
        """cent=self._centroid
        dataset=self.getContents()
        #print dataset
    
        ran=len(dataset)
        ranpt=len(dataset[0])
        #print ran
        #print ranpt
        worklist=list([])
        
        for x in range(0,ranpt):
            num=0
            for y in range(0,ran):
                num+=(dataset[y])[x]
                #print num
            
            num=num/ran
            worklist.append(num)
            #print worklist
        
        newlist=list(worklist)
        """
        cent=self._centroid
        worklist=list([])
        r=self.getContents()
        for x in range(len(r[0])):
            num=0.0
            for y in range(len(r)):
                fp=r[y][x]
                num+=fp
            
            num=num/len(self.getContents())
            worklist.append(num)
        
        work2=list(worklist)
        
        if  numpy.allclose(cent, work2)==True:
            return numpy.allclose(cent,work2)
        if  numpy.allclose(cent, work2)==False:
            self._centroid=work2
            return numpy.allclose(cent,work2)
            
   

class ClusterGroup(object):
    
    def __init__(self, data, k, seed_index=None):
        """
        Creates a group of k clusters
        seed_inds are the list of indicies in the dataset that the user selects before hand if they want to make those the points of cluster centroids
        """
        
        assert isinstance(data,Dataset)
        assert isinstance(k,int) and (k>=0 and k<=data.getSize())
        
        assert (isinstance(seed_inds,list) and len(seed_inds)==k) or (seed_inds==None)
       
        
        self._dataset= data
        
        
        cl=list()
        datal=data.getContents()
        d=len(datal[0])
        if seed_index==None:
            #silist=list()
            
            
            #workinglist=list(data)
            #print data
            #print d
            
            
            #(self, ds, centroid)
            #for x in range(0,len(dataset)):
            #for y in range(0,len(data)-1):
            t=random.sample(datal, k)
            #print t
            
            
            for x in range(0,len(t)):
                #u=t[x]
                #a=data[u]
                
                cl.append(Cluster(data,t[x]))
            #self._clusters=cl
            #print self._clusters
            #return self._clusters
            
        else:
            #silist=list(seed_inds.getIndicies())
            for x in seed_index:
                #u=t[x]
                #a=data[u]
                
                cl.append(Cluster(data,data.getContents()[x]))
        
        self._clusters=cl
        
        
        
        
    def getClusters(self):
        return self._clusters
       
            

    def _nearest_cluster(self, point):
        assert isinstance(point,list) and len(point)==self._dataset.getDimension()
        
        distances=dict()
        cluster=None
        
        #print len(self._clusters)
        for x in range(0,len(self._clusters)):
            centroid=self._clusters[x].getCentroid()
            d=self._clusters[x].distance(point)
            distances[x]=d
        #print distances
        #print min(distances)
        #print distances[min(distances)]
        q= min(distances.values())
        #print q
        #print distances[0]
        #print distances[1]
        #print distances.get(1)
        #return self._clusters[min(distances.values())]
        
        for i in range(0,len(distances)):
            if distances[i]==q:
                return self._clusters[i]
            
          
            
    
    
    def _partition(self):
        
        datam=self._dataset.getContents()
        
        #data=list(self._dataset)
        #print data
        for x in range(0,len(self._clusters)):
            self._clusters[x].clear()
            
        #print self._clusters
        #print len(data)
        for y in range(0,len(datam)):
            point=datam[y]
            t=self._nearest_cluster(point)
            t.addIndex(y)
            #addIndex(self, index):
            #l=t._dataset.append(point)
            #print point
            #print t
            #print l
    
    def _update(self):
        
        # bool=True
        changes=0
        #return self._clusters[0].updateCentroid()
        a=self.getClusters()
        for x in range(0,len(a)):
            m=a[x]
            if m.updateCentroid()==False:
                changes+=1
        
        if (changes==0):
            return True
        else:
            return False
        """
            #print t
            #print t.updateCentroid()
            #print self._clusters[x].getCentroid()
            #print 
            #if t==True:
                #bool==True
            #elif t==False:
                #bool=False
                
       
        return bool
        """
    def step(self):
        self._partition()
        return self._update()
    
   
    def run(self, maxstep):
        assert isinstance(maxstep,int) and maxstep>=0
        counts=0
        
        while(counts<maxstep):
            r=self.step()
            if r==True:
                counts=1+maxstep
            else:
                self.step()
        
