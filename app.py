import streamlit as st
import pickle
import pandas as pd
import requests

url = "https://api.themoviedb.org/3/movie/116?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNGE2OWU1MGI1MzI2MjI1N2Y5YzkwZTBiNzIwOTRjZiIsInN1YiI6IjY0ZGY2YTdjZDEwMGI2MTRiNGNkNmVkNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.J4x9aXg5tKLjSKwvcEjtrTK5fqYrTuduDj3LUGs-N4g"
}

response = requests.get(url, headers=headers)

print(response.text)

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id) , headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3,= st.columns(3)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])


    col1, col2, col3, = st.columns(3)

    with col1:
        st.subheader(names[3])
        st.image(posters[3])

    with col2:
        st.subheader(names[4])
        st.image(posters[4])

    with col3:
        st.subheaderf(names[5])
        st.image(posters[5])

