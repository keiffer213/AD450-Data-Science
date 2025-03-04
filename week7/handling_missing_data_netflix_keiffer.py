import pandas as pd
import numpy as np

file_path = './netflix_titles.csv'

if __name__ == "__main__":

  netflix_titles = pd.read_csv(file_path)
  # print(netflix_titles.head())

  ##################################### IDENTIFY MISSING DATA #####################################

  missing_data_value_counts = netflix_titles.isnull().sum() 
  # Above will find if the cells are True/False, and then sum() will count the amount of cells that are 
  # True for each column which is commented below
  print(f'Missing Data in each column: \n{missing_data_value_counts}')

  # Column          # missing
  # show_id            0
  # type               0
  # title              0
  # director        2634
  # cast             825
  # country          831
  # date_added        10
  # release_year       0
  # rating             4
  # duration           3
  # listed_in          0
  # description        0

  ################################ CALCULATE TOTAL MISSING VALUES ################################

  # Below returns the sum of the missing cells in each column
  total_missing_data = missing_data_value_counts.sum()
  print(f'There are {total_missing_data} cells missing')

  # There is a total of "4307" cells of missing data

  ################################## PERCENTAGE OF MISSING DATA ##################################

  # netflix_titles.shape = (8807, 12)
  total_cells = np.product(netflix_titles.shape) #np.prod or product will return product of array elemnts over given axis
  print(f'There is a total of {total_cells} cells')
  percent_missing =  (total_missing_data / total_cells) * 100
  print(f"There is a total of {percent_missing:.2f}% missing cells in the DataFrame")















