#Celine Yan and Amy Xu
#Period 6 Soft Dev

import csv
import random

hi = open("occupations.csv", "rb")
reader = csv.reader(hi)
dic = {}
L = []
out = "You consult the wizard about which job you should pursue...the answer is: "

def listify(L, readin):
    for occupation in readin:
        L.append(occupation)
    return L[1:len(L)-1]

def addToDict(L,D):
    for item in L:
        D[item[0]] = int(float(item[1]) * 10)
    return D


#out of 998
def modList(dic):
    master = []
    for key in dic:
         master += [key]*dic[key]
    return master

def randomizer(alist):
    return out + alist[random.randint(0,len(alist)-1)] 

L = listify(L,reader)
dic = addToDict(L, dic)

#print len(dic)
print randomizer(modList(dic))
print randomizer(modList(dic))
print randomizer(modList(dic))
print randomizer(modList(dic))
