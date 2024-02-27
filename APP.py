

# CREATING A WEB APPLICATION USING STREAMLIT AND PYTHON

import streamlit as st
import pickle

movie = pickle.load(open('movie_data.pkl','rb'))
movies_list = movie['title'].values

similar = pickle.load(open('similarity_data.pkl','rb'))

def recommend(movies):

    idx = movie[movie['title']==movies].index[0]
    distance = sorted(list(enumerate(similar[idx])), reverse=True, key=lambda transformed_movie_data:transformed_movie_data[1])
    recommended_movies=[]

    for d in distance[0:10]:
        recommended_movies.append(movie.iloc[d[0]].title)

    return recommended_movies

st.header("Find Similar Movies To Your Choices !!!!")
select_value = st.selectbox("Select Movie From Dropdown Box", movies_list)

if st.button("Show Recommendations"):
    movie_names = recommend(select_value)
    col1, col2, col3, col4, col5 , col6= st.columns(6)
    with col1:
        st.text(movie_names[0])
    with col2:
        st.text(movie_names[1])
    with col3:
        st.text(movie_names[2])
    with col4:
        st.text(movie_names[3])
    with col5:
        st.text(movie_names[4])
    with col6:
        st.text(movie_names[5])
    
    
