# loading libraries
import pandas as pd

# Reading csv file
data = pd.read_csv('movie_dataset.csv')

# to visualize
data.head(10)
print(data)

nullCheck = data.isnull().sum()
print(nullCheck)

duplicateCheck = data.duplicated().sum()
print(duplicateCheck)

genre = data.iloc[4].genre
print(genre)

movieTitle = data['title'][2]
print(movieTitle)

data['title'] = data['title'].str.lower()
print(data['title'][2])

data['keyword'] = data['genre'] + '' + data['crew']
print(data['keyword'])

new_data = data[['image', 'title', 'keyword']]
print(new_data)

from sklearn.feature_extraction.text import CountVectorizer

#  stop words Remove all english  such as 'the', 'a'

cv = CountVectorizer(max_features=1000, stop_words='english')

vector = cv.fit_transform(new_data['keyword']).toarray()
v = vector.shape
print(vector)
length = cv.get_feature_names()
print(length)

# stemming: including a common word for words same in meaning like play, playing

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def stem(text):
    a = []
    for i in text.split():
        a.append(ps.stem(i))
    return " ".join(a)


new_data['keyword'] = new_data['keyword'].apply(stem)
print(new_data['keyword'])

# implementing cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
print(similarity[100][100])

def recommend(title):


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
