import pandas as pd
import numpy as np

file_path = './netflix_titles.csv'

if __name__ == "__main__":

  netflix_titles = pd.read_csv(file_path)
  # Next few print statements is just for self checking to make sure that the correct rows have been dropped
  # print(netflix_titles)
  # print(netflix_titles[['show_id', 'director']])


  ##################################### DROP ROWS WITH MISSING 'DIRECTOR' VALUES #####################################
  missing_data_value_counts_director = netflix_titles.director.isnull().sum() 
  # Above will find if the cells are True/False, and then sum() will count the amount of cells that are True for the director column
  
  print('DROP ROWS WITH MISSING \'DIRECTOR\' VALUES')
  print(f'Missing Data in director column: {missing_data_value_counts_director} \nNumber of rows: {netflix_titles.shape[0]}')
        # OUTPUT: Missing Data in director column: 2634 
        #         Number of rows: 8807

  # DROPPING rows where director cell is NaN
  netflix_titles_drop1 = netflix_titles.dropna(subset=['director'], axis=0)

  missing_data_value_counts_director_after = netflix_titles_drop1['director'].isnull().sum() 
  # Above will find if the cells are True/False, and then sum() will count the amount of cells that are True for the director column

  print(f'Missing Data in director column after dropna: {missing_data_value_counts_director_after} \nNumber of rows left: {netflix_titles_drop1.shape[0]}\n\n')
        # OUTPUT: Missing Data in director column after dropna: 0
        #         Number of rows left: 6173
  # print(netflix_titles[['show_id', 'director']])


  # THIS SECTION IS JUST PERSONAL TESTING TO SEE HOW MANY ROWS ARE LEFT AFTER EMPTY DIRECTOR ROWS ARE REMOVED
  # missing_data = netflix_titles_drop1['cast'].isnull().sum() 
  # print(missing_data)
  # netflix_titles_drop2 = netflix_titles_drop1.dropna(subset=['cast'], axis=0)
  # print(netflix_titles_drop2.shape)
  # OUTPUT: 473 \n (5700, 12)



  ############################### DROP ROWS WITH MISSING 'DIRECTOR' AND 'CAST' VALUES ###############################
  missing_data_value_counts_dir_cast = netflix_titles[['director', 'cast']].isnull().sum() 

  print('DROP ROWS WITH MISSING \'DIRECTOR\' AND \'CAST\'VALUES')
  print(f'Missing Data columns column: {missing_data_value_counts_dir_cast.sum()} \n{missing_data_value_counts_dir_cast} \nNumber of rows: {netflix_titles.shape[0]}')

  # Drop rows where the director and cast cell is NaN
  netflix_titles_drop2 = netflix_titles.dropna(subset=['director', 'cast'], axis=0)
  print(f'Number of rows left after dropna() for director and cast: {netflix_titles_drop2.shape[0]} \nSome of the rows had both director and cast values as NaN\n')




  #################################### CREATE A DATAFRAME WITH NO MISSING VALUES ####################################

  print('\nDROP ALL ROWS WITH MISSING VALUES')

  # Drop all NaN values in the entire DataFrame since there is no subset
  netflix_titles_drop_all = netflix_titles.dropna(axis=0)
  print(f'Number of rows after dropna() for all NaN: {netflix_titles_drop_all.shape[0 ]}')

  # Below shows that there are no more null values in the DataFrame
  print(netflix_titles_drop_all.isnull().sum())







