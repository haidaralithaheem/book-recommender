# 📚 Book Recommender System

This project is a Book Recommender System built using machine learning and cosine similarity-based K-Nearest Neighbors (KNN) algorithm. The system recommends similar books to the user based on a selected book using collaborative filtering techniques. It is deployed with a Streamlit interface and can be easily accessed through a web browser.

## 🔍 Features

Recommends books based on user ratings.

Uses KNN with cosine similarity to find similar books.

Interactive and clean Streamlit UI for easy access.

Displays book cover images with clickable links to Google search.

Model trained using a sparse pivot matrix for efficiency.


## 🔍 What It Does

- Suggests books similar to the one you choose
- Uses collaborative filtering (KNN)
- Shows book cover images
- Easy-to-use web app made with Streamlit


  ![image](https://github.com/user-attachments/assets/a2cdc9cd-d858-488c-8765-b480df8a3094)
## 🚀 How to Use

1. Clone the Project

git clone https://github.com/haidaralithaheem/book-recommender.git

cd book-recommender

2. Install Dependencies

pip install -r requirements.txt

3. Run the App
   
streamlit run app.py

Open http://localhost:8501 in your browser.



## 🌐 Live Demo

Try the app here:

https://book-recomender-ae18baf14e53.herokuapp.com/

## 📁 Dataset link: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data

The system is trained on a dataset that includes:

-books.csv — Book details (title, author, image URL)

-ratings.csv — User ratings for books

-users.csv — User demographic data

## 🛠 Tools Used

-Python

-Pandas, NumPy

-Scikit-learn (KNN)

-Streamlit

-Pickle

-Heroku

## 📞 Contact

Haidar Ali Thaheem

📧 haidaralithaheem111@gmail.com


