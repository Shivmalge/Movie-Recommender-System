# import pickle
# import streamlit as st
# import pandas as pd

# def recommend(movie):
#     # Check if the movie exists
#     if movie.lower().strip() not in movies['title'].str.lower().str.strip().values:
#         st.error("Selected movie not found in the database.")
#         return []
    
#     # Normalize the titles
#     index = movies[movies['title'].str.lower().str.strip() == movie.lower().strip()].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     for i in distances[1:6]:
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names

# st.header('Movie Recommender System')

# # Load data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # Load as a dictionary
# movies = pd.DataFrame(movies_dict)  # Convert to a DataFrame
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Ensure movies DataFrame has a title column
# if 'title' not in movies.columns:
#     st.error("The 'movies' data is not structured correctly. Ensure it has a 'title' column.")
# else:
#     movie_list = movies['title'].values
#     selected_movie = st.selectbox(
#         "Type or select a movie from the dropdown",
#         movie_list
#     )

#     if st.button('Show Recommendation'):
#         recommended_movie_names = recommend(selected_movie)
#         if recommended_movie_names:
#             col1, col2, col3, col4, col5 = st.columns(5)
#             columns = [col1, col2, col3, col4, col5]
#             for i, col in enumerate(columns):
#                 if i < len(recommended_movie_names):
#                     with col:
#                         st.text(recommended_movie_names[i])

import pickle
import streamlit as st
import pandas as pd
import lzma  # Import lzma to load .xz files

def recommend(movie):
    # Check if the movie exists
    if movie.lower().strip() not in movies['title'].str.lower().str.strip().values:
        st.error("Selected movie not found in the database.")
        return []
    
    # Normalize the titles
    index = movies[movies['title'].str.lower().str.strip() == movie.lower().strip()].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.header('Movie Recommender System')

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # Load as a dictionary
movies = pd.DataFrame(movies_dict)  # Convert to a DataFrame

# Load the similarity.pkl.xz file using lzma
with lzma.open('similarity.pkl.xz', 'rb') as f:
    similarity = pickle.load(f)

# Ensure movies DataFrame has a title column
if 'title' not in movies.columns:
    st.error("The 'movies' data is not structured correctly. Ensure it has a 'title' column.")
else:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names = recommend(selected_movie)
        if recommended_movie_names:
            col1, col2, col3, col4, col5 = st.columns(5)
            columns = [col1, col2, col3, col4, col5]
            for i, col in enumerate(columns):
                if i < len(recommended_movie_names):
                    with col:
                        st.text(recommended_movie_names[i])
