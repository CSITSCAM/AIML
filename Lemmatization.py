#!pip install nltk
#!pip install wordnet
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from nltk import wordnet
wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer
 learning new skills from the comforts of their drawing rooms"
  
nltk.download('punkt')
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       print(w,wordnet_lemmatizer.lemmatize(w))
