import streamlit as st
import pickle
import streamlit_shadcn_ui as ui
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="CineMatch", page_icon="", layout="wide")

movies = pickle.load(open(r'E:\Netflix Movie Recommendation System\Model\movies.pkl', 'rb'))

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.markdown("<h1 style='text-align: center; color: #E50914;'> CineMatch</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: gray;'>Discover your next favorite movie</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_movie = st.selectbox(' Search for a movie you love:', movies['title'].values)
    st.markdown("<br>", unsafe_allow_html=True)
    submit = ui.button(" Get Recommendations", key="rec_btn", variant="default")

if submit:
    st.markdown("<br><h3 style='text-align: center;'>Top Picks For You</h3><br>", unsafe_allow_html=True)
    recommendations = recommend(selected_movie)
    
    cols = st.columns(5)
    for i, movie in enumerate(recommendations):
        with cols[i]:
            st.markdown(f"<div style='text-align: center; padding: 20px 10px; background-color: #1e1e1e; border-radius: 10px; border: 1px solid #333;'><b>{movie}</b></div>", unsafe_allow_html=True)