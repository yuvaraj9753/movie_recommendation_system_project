# 🎬 Movie Recommendation System

## 📖 Project Summary
This project is a **Content-Based Movie Recommendation System** that suggests movies similar to the one selected by the user. The recommendations are based on movie attributes such as **genre, cast, director, and overview text**, using the **TMDb (The Movie Database) dataset**. The system calculates similarity using **cosine similarity** on text-based features derived from the dataset.

---

## 🧩 Project Overview
The aim of this project is to help users discover movies they might like based on their preferences. The system uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to analyze the movie data and recommend similar movies. A **Streamlit web app** is used to make the system interactive and user-friendly.

---

## ❓ Problem Statement
Finding new movies that match a viewer’s taste can be challenging with the massive number of movies available. This project solves that problem by building a **content-based recommendation system** that automatically suggests similar movies based on textual and categorical features.

---

## 🎞️ Dataset Information
- **Dataset Source:** TMDb (The Movie Database)  
- **Dataset Type:** Movie Metadata  
- **Features Used:**  
  - Title  
  - Overview  
  - Genre  
  - Cast  
  - Director  
  - Keywords  

The dataset is preprocessed to remove missing values and merge multiple text columns into one combined feature for similarity computation.

---

## 🛠️ Tools and Technologies Used
| Category | Tools / Libraries |
|-----------|------------------|
| Programming Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn (TF-IDF, CountVectorizer, Cosine Similarity) |
| Web Framework | Streamlit |
| Dataset Source | TMDb / Kaggle |
| API Integration | TMDb API for movie posters |
| Version Control | Git, GitHub |

---

## ⚙️ Methods and Approach
1. **Data Preprocessing:** Clean the dataset and handle missing values  
2. **Feature Engineering:** Combine multiple features (overview, genres, cast, etc.) into a single text column  
3. **Vectorization:** Convert text data into numerical vectors using **TF-IDF** or **CountVectorizer**  
4. **Similarity Calculation:** Calculate **cosine similarity** between movie vectors  
5. **Recommendation Function:** Suggest top 5–10 similar movies based on similarity scores  
6. **Deployment:** Build a **Streamlit web app** for interactive user experience  

---

## 🔑 Key Insights
- Movies with similar genres, cast, and overviews are grouped together based on text similarity.  
- Cosine similarity provides an efficient way to compare movies.  
- Content-based systems perform well for new users without needing prior ratings.  

---

## 🖥️ Output
- Displays **top 5–10 similar movies** to the selected movie.  
- Fetches and shows **movie posters** using the TMDb API.  
- Interactive and visually appealing **Streamlit web interface**.

---

## ▶️ How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Movie-Recommendation-System.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Movie-Recommendation-System
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Open the link shown in your terminal to view the web app.

---

## 📊 Results
- Successfully recommends similar movies based on content features.  
- Provides a fast and efficient recommendation experience.  
- Demonstrates real-world application of NLP and Machine Learning.  

---

## 🔮 Future Scope
- Add **Collaborative Filtering** to create a hybrid system.  
- Integrate **User Login** for personalized recommendations.  
- Deploy the app on **Render / Streamlit Cloud** for public access.  
- Implement **Deep Learning-based Recommenders (Autoencoders)**.

---

## 👨‍💻 Authors
**Yuvraj Kushwaha**  
Data Science Enthusiast | Machine Learning Learner |   

---
