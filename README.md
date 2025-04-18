# IMDB_2024_Movies
🎬 **IMDb 2024 Movie Visualization Dashboard**

  Welcome to the IMDb 2024 Dashboard, a fully interactive data visualization project that brings movie analytics to life! Built using Streamlit, Python, SQL, and Selenium, this dashboard allows users to explore, analyze, and compare IMDb movie data across multiple dimensions like genre, ratings, voting trends, and duration.

🚀 **Project Overview**

  In the age of streaming and cinema overload, finding meaningful insights about movies can be overwhelming. This project scrapes IMDb 2024 movies data for five genres and transforms it into an intuitive dashboard that highlights trends, patterns, and standout performances from the world of cinema.

Using Selenium, the collection of structured data from IMDb were automated. The data is cleaned and stored in a MySQL database, then dynamically visualized using Streamlit with rich interactive controls.

🧰 **Tech Stack**

Python (Pandas, Seaborn, Matplotlib, Plotly, SQLAlchemy)

Streamlit for dashboard development

MySQL for structured data storage

Selenium for web scraping


🔄 **Project Workflow**

⚡1. **Data Collection (Selenium Automation)**
IMDb pages were scraped programmatically using Selenium to fetch movie metadata including:

Title

Genre

Ratings

Duration

Voting Counts

The scraper navigates through genre-specific pages, extracting data and storing it in CSV format.

⚡2. **Data Cleaning & Preprocessing**
Cleaned and transformed raw data using Pandas.

⚡3. **Data Storage (SQL)**
Created a MySQL database (imdb_genre_2024) with a table movies_genre_2024 to store structured data.

Used SQLAlchemy to connect Python with MySQL for seamless querying and integration with the dashboard.

⚡4. **Interactive Dashboard with Streamlit**
Developed an engaging dashboard using Streamlit.

Implemented sidebar filters for genre, rating, votes, and duration.

Established Dynamic visualizations powered by Plotly, Matplotlib, and Seaborn.

📊 **Dashboard Features**

Each question was mapped to an interactive chart or table in the dashboard:

🏅 **Top 10 Movies by Rating & Voting Counts**

Bar chart of the highest-rated and most-voted movies.

📊 **Genre Distribution**

Bar chart showing the number of movies per genre.

⏱️ **Average Duration by Genre**

Horizontal bar chart displaying average duration across genres.

🗳️ **Voting Trends by Genre**

Bar chart comparing average voting counts per genre.

⭐ **Rating Distribution**

Histogram to explore the spread of movie ratings.

🏆 **Top-Rated Movies by Genre**

Table highlighting the best-rated movie in each genre.

🥧 **Most Popular Genres by Votes**

Pie chart showing total vote distribution among genres.

🎬 **Duration Extremes**

Cards displaying the shortest and longest movies.

🔥 **Ratings by Genre**

Heatmap of average ratings for each genre.

📈 **Correlation Analysis**

Scatter plot to examine the relationship between votes and ratings.

📁 **Repository Contents**

├── imdb.ipynb                  # Scraping & data preprocessing notebook
├── imdbvisuals.py             # Streamlit dashboard code
├── all_genres_2024_cleaned.csv # Cleaned dataset
└── README.md                  # Project documentation

🙌 **Acknowledgements**
IMDb for public movie data.

Open-source contributors and libraries used in this project.

📬 **Contact**
For queries, feel free to reach out via GitHub Issues or connect with me on https://www.linkedin.com/in/dr-sreeja-s-maths/
