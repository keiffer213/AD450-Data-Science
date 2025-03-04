import pandas as pd
import numpy as np

file_path = './netflix_titles.csv'

if __name__ == "__main__":

  netflix_titles = pd.read_csv(file_path)
  # print(netflix_titles.head())


  ##################################### DATA TYPE ANALYSIS #####################################
  date_added_col_d_type = netflix_titles.date_added.dtype
  print('\n****** DATA TYPE ANALYSIS ******')
  print(f'date_added column data type: {date_added_col_d_type} ')
  # print(f'{netflix_titles.date_added.info()}')

  # It is important to ensure the correct data type for datetime data because it will allow for efficient and accurate manipuation of date values. The original column is going to be an 'object' data type because all strings are considered objects. Once we convert it to the proper datetime format, pandas will be able to extract components like days, months, years, and performing date-based calculations. Overall, datetime objects are also more efficient than string objects in the long run!

  ##################################### DATETIME CONVERSION #####################################
  print('\n****** DATETIME CONVERSION ******')

  # Need to data clean the column first by making it all lower case and stripping extra spaces
  netflix_titles['date_added'] = netflix_titles['date_added'].str.lower()
  netflix_titles['date_added'] = netflix_titles['date_added'].str.strip()

  netflix_titles_dropped_date = netflix_titles.dropna(subset='date_added', axis=0).copy()
  print(f'Number of NaN cells after cleaning: {netflix_titles_dropped_date.date_added.isnull().sum()}')


  # The following code was just used to check the lengths of each string value
  # date_added_lengths = netflix_titles['date_added'].str.len()
  # print(date_added_lengths.value_counts())

  # indices = np.where([date_added_lengths == 17])
  # print(indices)


  # Convert all datatype in column into datetime type
  netflix_titles_dropped_date['date_added_parsed'] = pd.to_datetime(netflix_titles_dropped_date['date_added'], format='%B %d, %Y', errors='coerce')

  # Find how many of the rows is NaT after converting
  # print(netflix_titles_dropped_date['date_added_parsed'].isnull().sum())

  # I used this to find which indices if any were empty or null
  # indices = np.where(netflix_titles_dropped_date['date_added_parsed'].isnull())
  # print('HERE --------------------------------------------------->', indices[0])
  # cols = ('show_id', 'type', 'date_added', 'date_added_parsed')
  # print(netflix_titles_dropped_date.loc[indices[0], cols])

  print(f'Data type of \'date_added_parsed\' column: {netflix_titles_dropped_date['date_added_parsed'].dtype}')
  print(f'date_added_parsed column: \n{netflix_titles_dropped_date[['date_added', 'date_added_parsed']].head()}')


  ##################################### DAY EXTRACTION #####################################
  print('\n****** DAY EXTRACTION ******')

  # I can extract day, month, and year from a datetime64[ns] data type by using "dt.___" (day, month, year in ____)
  day_series = pd.Series(netflix_titles_dropped_date.date_added_parsed.dt.day)
  # print(f'Exract day as a series: \n{day_series}')

  # I can also accomplish it this way as well an assign another column in the DF
  netflix_titles_dropped_date['day_of_month'] = netflix_titles_dropped_date['date_added_parsed'].dt.day
  print(f'Exract day as a series: \n{netflix_titles_dropped_date[['date_added', 'date_added_parsed', 'day_of_month']].head()}')











