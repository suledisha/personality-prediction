import io
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
import os
import nltk
import collections
from nltk.corpus import stopwords
from nltk.corpus import verbnet 
import operator
from decimal import *
import math



# Name of the token file
filename='C:/Users/Disha/Desktop/NLP/Proj/austen.tokens' 
# filename='C:/Users/Disha/Desktop/NLP/Proj/dickens.oliver.tokens'
# filename='C:/Users/Disha/Desktop/NLP/Proj/twain.tom.sawyer.74.tokens'

# File with extrovert action words
extfile='C:/Users/Disha/Desktop/NLP/Proj/ext.txt'

# File with introvert action verbs
intfile='C:/Users/Disha/Desktop/NLP/Proj/int.txt'


fr=open(filename,'r')
# Dictionary to store the story by sentence Id and character name
story=collections.OrderedDict()
# Dictionary to store characters and their actions
bagOfWords=collections.OrderedDict()
# Training set for extrovert action words
extList=collections.OrderedDict()
# Training set for introvert action words
intList=collections.OrderedDict()

# Data set preparation

for line in fr:
	tokens=line.split()
	sentenceId=tokens[1]
	if sentenceId not in story:
		story[sentenceId]={}
	NER= tokens[11]
	name= tokens[7]
	deprel=tokens[12]
	pos=tokens[10]
	lemma=tokens[9].lower()
	# Extracting characters
	if NER=="PERSON" and deprel=="nsubj":
		story[sentenceId][name]=[]
		# Extracting actions for the characters
	if "VB" in pos or 'JJ' in pos or 'adv' in deprel:
		if lemma not in stopwords.words('english'):
			for n in story[sentenceId]:
				story[sentenceId][n].append(lemma)
		
# print story

# Creating dictionary of characters and their action
for s in story:
	for n in story[s]:
		if n not in bagOfWords:
			bagOfWords[n]={}
		for term in story[s][n]:
			if term not in bagOfWords[n]:
				bagOfWords[n][term]=1
			else:
				bagOfWords[n][term]+=1
		
maxCount=0
maxTerm=""
l=len(bagOfWords)/4
total=0
avg=0
for name in bagOfWords:
	for term in bagOfWords[name]:
		if bagOfWords[name][term]>maxCount:
			maxCount=bagOfWords[name][term]
			maxTerm=term
	# print name, maxTerm, maxCount
	total+=maxCount
	maxCount=0
avg= total/l
# print bagOfWords["elizabeth"]
# print avg

allverbs=[]

# Creating training set
fr=open(extfile,'r')
for line in fr:
	token= line.strip("\n")
	extList[token]=avg
	words= verbnet.classids(token)
	for w in words:
		finalWord= w.decode("UTF-8","ignore")
		allverbs+=verbnet.lemmas(finalWord)

for v in allverbs:
	extList[v]=avg/2
# print len(extList)

allverbs=[]

fr=open(intfile,'r')
for line in fr:
	token= line.strip("\n")
	intList[token]=avg
	words= verbnet.classids(token)
	for w in words:
		finalWord= w.decode("UTF-8","ignore")
		allverbs+=verbnet.lemmas(finalWord)

for v in allverbs:
	intList[v]=avg
# print len(intList)

# Naive Bayes Code

# calculating the total number of words(non unique in the extrovert and introvert list)
extList_total= sum(extList.values())
intList_total = sum(intList.values())

# print extList_total
# print intList_total

for name in bagOfWords:
		likelihood_score=0
		pe=1
		pi=1
		ln= len(bagOfWords[name])
		for term in bagOfWords[name]:
			f=bagOfWords[name][term]
			if term in extList:
				# Smoothing factor
				e=extList[term]+0.1
			else:
				e=0.1
			ex= Decimal(e)/ Decimal(extList_total+(0.1*ln))

			if term in intList:
				i=intList[term]+0.1
			else:
				i=0.1
			it=Decimal(i)/Decimal (intList_total+(0.1*ln))

		# calculating the log likelihood ratio
			lg=float (math.log(ex/it))
			lgf= float (f)*lg
			likelihood_score=likelihood_score+lgf
			pe=pe* pow(ex,f)
			pi=pi *pow(it,f)


		#  calculating the extrovert and introvert score

		extro_score=Decimal(0.5)*pe
		intro_score=Decimal(0.5)*pi
		
		# Computing the Class of the character - whether he/she is an extrovert or an introvert
		# If likelihood ratio is greater than zero, classify as extrovert else an introvert
		Ptype=""
		if extro_score>intro_score :
			Ptype='E'
		else :
			Ptype='I'
		# Printing the output Character Name, Type
		# E for Extrovert and I for Introvert
		print(name, Ptype)
			

