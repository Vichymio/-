import pandas as pd

df=pd.read_excel("工作簿1.xlsx")
gjr=[];his=[];gjr2=[]
print(df)

#df=df.T

for i in df.columns:
    if i == df.columns[0]:
        continue
    for j in df.index:
        if len(gjr)<=20:
           gjr.append([j,i])
           #print(gjr)
        else:
            for x in range(20):
                if int(df.loc[j,i])>int(df.loc[gjr[x][0],gjr[x][1]]):
                    gjr[x][0]=j
                    gjr[x][1]=i
                    break
    for x in range(20):
        if df.loc[gjr[x][0],df.columns[0]] not in his:
            his.append(df.loc[gjr[x][0],df.columns[0]])
            gjr2.append(gjr[x][0])
    gjr=[]
print(his)


data=[]
for i in range(len(his)):
    mini=[]
    for j in range(24):
        mini.append(df.loc[gjr2[i],df.columns[j]])
    data.append(mini)
print(data)
a=['国家',2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
newdf=pd.DataFrame(data,columns=a)
newdf.to_excel("前20.xlsx",index=False)