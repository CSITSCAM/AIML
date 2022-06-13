#!pip install nltk

text=['This is introduction to NLP','It is likely to be useful,to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
      
import pandas as pd

#convert list to data frame
df = pd.DataFrame({'tweet':'text'})

print(df)

!pip install nltk
import nltk
nltk.download()
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

stop = stopwords.words('english')

df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

df['tweet']
