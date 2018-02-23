import itertools
import csv
import numpy
def counter(x):
	unique, counts = numpy.unique(result,return_counts=True)
	list1= numpy.asarray((unique, counts)).T
        return list1
def findsubsets(S,m):
    return list(itertools.combinations(S, m))
	
sup=input("enter min support\n")
reader = csv.reader(open("test.csv", "rb"), delimiter=",")
X = list(reader)
result = numpy.array(X).astype("string")
print(result)
(m,n)=result.shape

list1=counter(result)
print("deleting items which have less support")
print(list1)
(a,b)=list1.shape
l=[]
for x in range(a):
		a=int(list1[x][1])
		sup1=int(sup)
                if(a>=sup):
			l.append(list1[x][0])
print"after deleting"
print(l)

print("making sets")
list2=[]

print(X)
print("=============================")
print"the rules are"
for i in range(2,len(l)):
	o=(findsubsets(l,2))
	print(o)
	print("======================")
	for x in o:
		count=0
		for y in X:
				if((x[0] in y) and (x[1] in y)):
					count=count+1
	       
		if(count>=2):
			
			list2.append(x)
print(list2)		
print(X)
minco=input("enter minimum confidence")

for a in list2:
	print(a[0]),
	print("========>"),
	print(a[1]),
	count=0
	count2=0
	for y in X:
		if(a[0]in y):
			count2=count2+1
			
		if((a[0] in y) and a[1]in y):
			count=count+1
	d=count/count2
	print(d),
	if(d>=minco):
		print("ok rule")
	else:
		print("not a rule")
	
					

