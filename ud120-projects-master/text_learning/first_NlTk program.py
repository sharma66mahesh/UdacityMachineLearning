from nltk.corpus import stopwords
sw = stopwords.words("english") #load all stop words from english language. If using nltk for first time in your computer, exception might be thrown. To solve that, use nltk.download() on command prompt
print sw[0]	#"I"
print sw[10]	#"yours"
print len(sw)
