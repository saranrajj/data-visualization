import codecs
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#read the csv with unicode support
text = codecs.open('./data/kural.csv', encoding='utf-8').read()
#can be used to stop some of the words
stopwords = {}
#create wordcloud object with params
wordcloud = WordCloud(
                width=800,
                height=800,
                background_color ='white',
                stopwords = stopwords,
                font_path='./fonts/tamil.ttf',  #mandatory to pass the font that supports the unicode
                min_word_length = 4, # minimum word length to show
                min_font_size = 2)
#generate the wordcloud
wc = wordcloud.generate_from_frequencies(wordcloud.process_text(text))
#plot the word cloud
plt.figure(figsize = (10, 10), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()