# 🎬 CineMatch: Netflix Movie Recommendation System

A Machine Learning-based movie recommendation engine that suggests 5 relatable movies based on your selection. Built with Python and featuring a modern, minimalistic UI.

## ✨ Features
* **Content-Based Filtering**: Recommends movies using cosine similarity on combined movie tags.
* **Modern Interface**: Clean, user-pleasing UI built with Streamlit and Shadcn UI components.
* **Fast Predictions**: Processes pre-trained data for instant recommendations.

## 🛠️ Tech Stack
* **Frontend**: Streamlit, Streamlit-Shadcn-UI
* **Machine Learning**: Scikit-Learn (CountVectorizer, Cosine Similarity)
* **Data Processing**: Pandas
* **Deployment**: Streamlit Community Cloud

## 🚀 Live Demo
[Click here to view the live app](https://your-app-url.streamlit.app) *(Update this link after deployment)*

## 💻 Local Installation

1. Clone the repository:
git clone [https://github.com/itsakshatsinghh/Netflix-Movie-Recommendation-System-.git](https://github.com/itsakshatsinghh/Netflix-Movie-Recommendation-System-.git)
cd "Netflix Movie Recommendation System"

Install the required dependencies:
pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Project Structure
app.py: The main Streamlit application code containing the UI and recommendation logic.

Model/movies.pkl: Pre-processed serialized dataset containing movie titles and tags.

requirements.txt: Required Python libraries to run the project.

How the Model Works
Vectorization: Uses CountVectorizer to convert textual movie tags (genres, keywords, cast, etc.) into numerical vectors.

Similarity Calculation: Applies cosine_similarity to measure the distance between vectors.

Recommendation: Retrieves and sorts the top 5 movies with the smallest distance (highest similarity) to the input movie.
