from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsive")
print stemmer.stem("unresponsive")  #trimming the un by this module would have been a lot better
