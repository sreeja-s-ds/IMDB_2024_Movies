import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import mysql.connector
import re
from sqlalchemy import create_engine

# Page Configuration
st.set_page_config(page_title="IMDb 2024 Dashboard", layout="wide", page_icon="🎬")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B;'>🎬 IMDb 2024 Movie Visualisation Dashboard</h1>
    <hr style='border: 1px solid #f63366;'>
""", unsafe_allow_html=True)


# Connection to MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5455",
    port=3306
)

db_cursor = db_connection.cursor()

engine = create_engine("mysql+mysqlconnector://root:5455@localhost:3306/imdb_genre_2024")
connection=engine.connect()

df=pd.read_sql("select * from movies_genre_2024",con=connection)
df = pd.read_sql("SELECT * FROM movies_genre_2024", connection)
df.rename(columns={'Voting Counts': 'Votes'}, inplace=True)


# Sidebar Filters
st.sidebar.header("📊 Filters")
selected_genres = st.sidebar.multiselect("🎭 Select Genre(s)", df['Genre'].dropna().unique())
min_rating = st.sidebar.slider("⭐ Minimum Rating", 0.0, 10.0, 0.0, 0.1)
min_votes = st.sidebar.slider("🗳️ Minimum Votes", 0, int(df['Votes'].max()), 0, 1000)
duration_option = st.sidebar.selectbox("⏱️ Duration (minutes)", ['All', '< 2 hrs', '2–3 hrs', '> 3 hrs'])

# Applying Filters
filtered_df = df.copy()
if selected_genres:
    filtered_df = filtered_df[filtered_df['Genre'].isin(selected_genres)]
if min_rating:
    filtered_df = filtered_df[filtered_df['Ratings'] >= min_rating]
if min_votes:
    filtered_df = filtered_df[filtered_df['Votes'] >= min_votes]
if duration_option == '< 2 hrs':
    filtered_df = filtered_df[filtered_df['Duration'] < 120]
elif duration_option == '2–3 hrs':
    filtered_df = filtered_df[(filtered_df['Duration'] >= 120) & (filtered_df['Duration'] <= 180)]
elif duration_option == '> 3 hrs':
    filtered_df = filtered_df[filtered_df['Duration'] > 180]

# To Display Filtered Data
st.subheader("🎯 Filtered Movies")
st.dataframe(filtered_df, use_container_width=True, height=350)

# 1. Top 10 Movies by Rating & Votes
st.subheader("🏅 Top 10 Movies by Rating & Votes")
top_movies = filtered_df.sort_values(by=['Ratings', 'Votes'], ascending=False).head(10)
fig1 = px.bar(top_movies, x='Movie Name', y='Ratings', color='Votes', title="Top 10 Movies",
              labels={"Rating": "IMDb Ratings", "Votes": "Vote Count"},
              color_continuous_scale='reds')
st.plotly_chart(fig1, use_container_width=True)

# 2. Genre Distribution
st.subheader("📊 Genre Distribution")
genre_counts = filtered_df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'count']
fig2 = px.bar(genre_counts, x='Genre', y='count', title="Number of Movies by Genre",
              color='count', color_continuous_scale='blues')
st.plotly_chart(fig2, use_container_width=True)

# 3. Average Duration by Genre
st.subheader("⏱️ Average Duration by Genre (mins)")
avg_duration = filtered_df.groupby('Genre')['Duration'].mean().sort_values()
fig3, ax3 = plt.subplots()
avg_duration.plot(kind='barh', ax=ax3, color='skyblue')
ax3.set_xlabel("Average Duration (mins)")
st.pyplot(fig3)

# 4. Average Voting by Genre
st.subheader("🗳️ Voting Trends by Genre")
avg_votes = filtered_df.groupby('Genre')['Votes'].mean().sort_values()
fig4, ax4 = plt.subplots()
avg_votes.plot(kind='bar', ax=ax4, color='orange')
ax4.set_ylabel("Average Votes")
st.pyplot(fig4)

# 5. Rating Distribution
st.subheader("⭐ Rating Distribution")
fig5, ax5 = plt.subplots()
sns.histplot(filtered_df['Ratings'], bins=10, kde=True, ax=ax5, color='green')
ax5.set_xlabel("Ratings")
st.pyplot(fig5)

# 6. Top-Rated Movies by Genre
if not filtered_df.empty:
    st.subheader("🏆 Top-Rated Movies by Genre")
    top_by_genre = filtered_df.loc[filtered_df.groupby('Genre')['Ratings'].idxmax()]
    st.dataframe(top_by_genre[['Genre', 'Movie Name', 'Ratings']], use_container_width=True)
else:
    st.warning("⚠️ No data to display top-rated movies.")

# 7. Most Popular Genres by Votes (Pie Chart)
if not filtered_df.empty:
    st.subheader("🥧 Most Popular Genres by Voting")
    total_votes = filtered_df.groupby('Genre')['Votes'].sum().reset_index()
    fig7 = px.pie(total_votes, names='Genre', values='Votes', title="Total Votes per Genre",
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig7, use_container_width=True)

# 8. Duration Extremes
if not filtered_df.empty:
    st.subheader("🎬 Duration Extremes")
    shortest = filtered_df.loc[filtered_df['Duration'].idxmin()]
    longest = filtered_df.loc[filtered_df['Duration'].idxmax()]
    st.metric("Shortest Movie", f"{shortest['Movie Name']} ({shortest['Duration']} mins)")
    st.metric("Longest Movie", f"{longest['Movie Name']} ({longest['Duration']} mins)")
else:
    st.warning("⚠️ No duration data found for filtered movies.")

# 9. Ratings by Genre (Heatmap)
if not filtered_df.empty:
    st.subheader("🔥 Average Ratings by Genre")
    heatmap_data = filtered_df.pivot_table(values='Ratings', index='Genre', aggfunc='mean')
    fig9, ax9 = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', ax=ax9)
    ax9.set_title("Genre-wise Average Ratings")
    st.pyplot(fig9)

# 10. Correlation - Rating vs Votes
if not filtered_df.empty:
    st.subheader("📈 Correlation: Ratings vs Votes")
    fig10 = px.scatter(filtered_df, x='Votes', y='Ratings', color='Genre',
                       title="Ratings vs Votes", hover_data=['Movie Name'],
                       color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig10, use_container_width=True)

# Footer
st.markdown("""
---
<div style='text-align: center;'>
    <em>📌 Made using Streamlit | IMDb 2024 Data</em>
</div>
""", unsafe_allow_html=True)
