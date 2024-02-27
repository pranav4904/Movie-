# IMPORTING DEPENDENCIES :
    
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# READING THE DOWNLOADED DATA :
    
movie_data = pd.read_csv(r"C:\Users\ASUS\Desktop\Pranav\Machine Learning\Datasets\movies_dataset.csv")

#print(movie_data.head(10))
#print(movie_data.info())
#print(movie_data.isnull().sum())

# USING CountVectorizer TO CONVERT THE TEXTUAL GENRES OF MOVIES INTO NUMERICAL VALUES FOR COMPUTATION

function = CountVectorizer(max_features = 9742, stop_words = 'english')
transformed_movie_data = function.fit_transform(movie_data['genres'].values.astype('U')).toarray()

#print(transformed_movie_data.shape)

# USING cosine_similarity function TO FIND THE SIMILARITIES BETWEEN THE GIVEN MOVIE AND OTHER MOVIES
 
similarity_data = cosine_similarity(transformed_movie_data)

#print(similarity_data[0])

# FUNCTION TO PRINT THE TITLES OF THE MOVIES WHICH ARE MOST SIMILAR TO THE MENTIONED MOVIE BASED ON GENRES
 
def recommend(movie):
    idx = movie_data[movie_data['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity_data[idx])), reverse=True, key=lambda transformed_movie_data:transformed_movie_data[1])
    for d in distance[0:15]:
        print(movie_data.iloc[d[0]].title)
        
recommend('Train to Busan ')

# CREATING NEW FILES FOR THE STREAMLIT APP 

pickle.dump(movie_data, open('movie_data.pkl','wb'))
pickle.dump(similarity_data, open('similarity_data.pkl','wb'))



