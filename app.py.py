import streamlit as st
import pickle
import pandas as pd
import requests


# ✅ Function to fetch movie poster using OMDb API
def fetch_poster(movie_title):
    api_key = "c6feac92"
    url = f"http://www.omdbapi.com/?t={movie_title}?&apikey={api_key}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # If valid movie found
        if data.get("Response") == "True" and data.get("Poster") != "N/A":
            return data["Poster"]
        else:
            # if no poster found
            return "https://via.placeholder.com/500x750?text=Poster+Not+Found"
    except requests.exceptions.RequestException as e:
        st.warning(f"⚠️ Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Poster"


# ✅ Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        # fetch poster using OMDb API
        recommended_movies_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_movies_posters


# ✅ Load pre-trained data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ Streamlit App UI
st.title('🎬 Movie Recommendation System ')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
