import pandas as pd

file_path = "./netflix_titles.csv"

if __name__ == "__main__":

  netflix_titles = pd.read_csv(file_path)

  ########################## READ & EXPLORE DATASET ##########################
  
  # Display the first 5 rows of the DataFrame
  first_five_rows = netflix_titles.head()
  # print(first_five_rows)

  # Display basic information about the DataFrame
  # netflix_titles_info = netflix_titles.info()
  # print(netflix_titles_info)


  ######################### BUSINESS CONTEXT ANALYSIS #########################

  # Count the number of titles per country
  titles_per_country = netflix_titles.country.value_counts()
  # print(titles_per_country)


  # Find the top 5 countries in terms of number of titles
  top_five_titles_per_country = titles_per_country.head()
  # print(top_five_titles_per_country)


  # Identify the year with the highest number of releases
  num_per_year = netflix_titles.release_year.value_counts()
  num_releases_per_year = num_per_year.sort_values(ascending=False)
  # print(num_releases_per_year)


  ########################## ADVANCED DATA FILTERING ##########################

  # Create a new DataFrame that contains only entries where the type is 'Movie' including all relevant columns from original dataset

  movies = netflix_titles.loc[netflix_titles.type == 'Movie']
  # print(movies)


  ########################## UNIQUE DIRECTORS ANALYSIS ##########################

  # Lists the unique directors from the DF
  unique_netflix_directors = netflix_titles.director.unique()
  # print(unique_netflix_directors)

  # Lists the unique directors in the DF and shows how many times each director shows up
  unique_netflix_directors = netflix_titles.director.value_counts()
  # print(unique_netflix_directors)


  ################################ DATA CLEANING ################################

  # Directors from the original DF
  # print(netflix_titles.director)

  # Replace directors with "NaN" to "Unknown"
  cleaned_netflix_directors = netflix_titles.fillna("Unknown")

  print(cleaned_netflix_directors.director) 
  print(cleaned_netflix_directors) 



