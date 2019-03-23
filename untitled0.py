import pandas as pa 
import math as a
dc={'day':[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
,'outlook':["sunny","sunny","overcast","Rain","Rain","Rain","overcast","sunny","sunny","Rain","sunny","overcast","overcast","Rain"]
,"temp":["Hot","Hot","Hot","Mild","cool","cool","cool","Mild","cool","Mild","Mild","Mild","Hot","Mild"]
,"Humidity":["HIGH","HIGH","HIGH","HIGH","NOrmal","NOrmal","NOrmal","HIGH","NOrmal","NOrmal","NOrmal","HIGH","NOrmal","HIGH"]
,"Wind":["weak","strong","weak","weak","weak","strong","weak","weak","weak","strong","strong","strong","weak","strong"]
,"play tennis":["NO","NO","YES","YES","YES","NO","YES","NO","YES","YES","YES","YES","YES","NO"]}
ds=pa.DataFrame(dc)
print(ds)
l=list(ds["play tennis"])
c=l.count("NO")
v=l.count("YES")
B=v+c
N=c/B
m=v/B
E=-N*a.log2(N)-m*a.log2(m)
print(E)
print(ds.transpose().describe())

