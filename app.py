import pickle
import streamlit as st
import numpy as np

# Load serialized data
model = pickle.load(open('model.pkl', 'rb'))
book_names = pickle.load(open('book_names.pkl', 'rb'))
final_rating = pickle.load(open('final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
book_sparse = pickle.load(open('book_sparse.pkl', 'rb'))

# Page settings
st.set_page_config(page_title="Book Recommender", layout="wide")
st.title('📚 Book Recommender System Using Machine Learning')

st.write(f"🔢 Total books available: **{len(book_names)}**")

# Book selector
selected_book = st.selectbox(
    "📖 Type or select a book from the dropdown", book_names
)

# --- Recommendation Function ---
def recommend_book(book_name):
    book_index = np.where(book_pivot.index == book_name)[0][0]
    _, suggestions = model.kneighbors(book_sparse[book_index], n_neighbors=6)

    # Skip the first item (the selected book itself)
    recommended_indices = suggestions[0][1:]
    recommended_books = book_pivot.index[recommended_indices].tolist()

    # Normalize image URLs
    final_rating['Image-URL-M'] = final_rating['Image-URL-M'].apply(
        lambda url: url.replace("http://", "https://") if url.startswith("http://") else url
    )

    poster_urls = []
    for book in recommended_books:
        idx = final_rating[final_rating['title'] == book].index[0]
        url = final_rating.loc[idx, 'Image-URL-M']
        poster_urls.append(url)

    return recommended_books, poster_urls

# --- Display Recommendations ---
if st.button("🔍 Show Recommendations"):
    recommended_books, poster_urls = recommend_book(selected_book)

    st.subheader("✨ Recommended Books for You")

    for title, img_url in zip(recommended_books, poster_urls):
        search_url = f"https://www.google.com/search?q={title.replace(' ', '+')}+book"
        
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin: 15px 0; background-color: #f9f9f9; padding: 10px 15px; border-radius: 12px;">
                <img src="{img_url}" width="80" style="border-radius: 8px; margin-right: 20px;">
                <a href="{search_url}" target="_blank" style="font-weight: bold; font-size: 16px; color: #333; text-decoration: none;" title="{title}">
                    {title}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
