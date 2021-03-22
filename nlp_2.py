from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd
from pathlib import Path

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
print("juliet", blob.word_counts["juliet"])
print("romeo", blob.word_counts["romeo"])
print("thou", blob.word_counts["thou"])
print("joy", blob.words.count("joy"))
# print("lady capulet", blob.noun_phrases.count("lady capulet"))

stops = stopwords.words("english")
more_stopwords = ["thee", "thy", "thou", "’"]
# romeo and juliet specific stop words to add into our removal list
stops += more_stopwords

items = blob.word_counts.items()
print(items)
# before we eliminate stop words
# showcases word and its frequency
items = [item for item in items if item[0] not in stops]
# must tell it to identify the item[0] which is the word component for each tuple
print(items[:10])

from operator import itemgetter


# retrieves alphabetically
sorted_items = sorted(items)
print(sorted_items[:10])

# retrieves the second index (number) and reverse = descending order
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

# list slicing, where we grab the top 20 from sorted_items list!
top20 = sorted_items[:20]
print()
print("top 20 list")
print()
print(top20)

df = pd.DataFrame(top20, columns=["word", "count"])
print(df)

import matplotlib.pyplot as plt


df.plot.bar(
    x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)
plt.gcf().tight_layout()
plt.show()

from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("done)")
