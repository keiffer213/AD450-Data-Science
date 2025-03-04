import pandas as pd
import numpy as np

file_path = './video_game_sales.csv'

"""
Student: Keiffer Tan
AD450 - Data Science Winter 2025

Assignment: Exploring Video Game Sales Correlations

Objective:
Analyze a dataset of video game sales to find out which regional sales variables share the strongest and weakest correlations. This exercise will help you understand the relationship between different market performances of video games.

"""

if __name__ == "__main__":

  ################## LOAD DATA ###################
  video_game_sales = pd.read_csv(file_path) # Read from CSV file
  # print(video_game_sales.head())



  ################## HANDLE MISSING DATA ###################
  missing_data_value_counts = video_game_sales.isnull().sum() 
  print(f'\n\nMissing Data in each column: \n{missing_data_value_counts}')

  # Column          # missing
  # Rank              0
  # Name              0
  # Platform          0
  # Year            271
  # Genre             0
  # Publisher        58
  # NA_Sales          0
  # EU_Sales          0
  # JP_Sales          0
  # Other_Sales       0
  # Global_Sales      0



  ################## CALCULATE TOTAL MISSING VALUES ###################
  total_missing_data = missing_data_value_counts.sum()
  print(f'There are {total_missing_data} cells missing\n\n')

  # There are 329 cells missing



  ################## FIND INDICES OF MISSING DATA ###################

  # Find the indices of the missing data
  indices = np.where(video_game_sales.isnull())
  # print('INDICES OF MISSING DATA', indices[0])
  print(video_game_sales.loc[indices[0], ('Rank', 'Name', 'Publisher', 'Year')])
  
  #         Rank                             Name                               Publisher    Year
  # 179      180                  Madden NFL 2004                         Electronic Arts     NaN
  # 377      378                 FIFA Soccer 2004                         Electronic Arts     NaN
  # 431      432       LEGO Batman: The Videogame  Warner Bros. Interactive Entertainment     NaN
  # 470      471       wwe Smackdown vs. Raw 2006                                     NaN     NaN
  # 470      471       wwe Smackdown vs. Raw 2006                                     NaN     NaN
  # ...      ...                              ...                                     ...     ...
  # 16427  16430                     Virtua Quest                                 Unknown     NaN
  # 16493  16496                       The Smurfs                                 Unknown     NaN
  # 16494  16497  Legends of Oz: Dorothy's Return                                     NaN  2014.0
  # 16543  16546           Driving Simulator 2011                                     NaN  2011.0
  # 16553  16556                   Bound By Flame                                     NaN  2014.0



  ################## REPLACE ROWS WITH MISSING 'PUBLISHER' / 'YEAR' VALUES ###################

  # Replace NaN values with 'Unknown'
  cleaned_video_game_sales = video_game_sales.fillna({'Publisher': 'Unknown', 'Year': 'Unknown'})

  # Print the cleaned DataFrame to check that there are no more missing values
  cleaned_data_value_counts = cleaned_video_game_sales.isnull().sum() 
  total_missing_data = cleaned_data_value_counts.sum()
  print(f'\n\nThere are {total_missing_data} cells missing in the cleaned dataframe')
  # There are 0 cells missing in the cleaned dataframe

  print(cleaned_video_game_sales.loc[indices[0], ('Rank', 'Name', 'Publisher', 'Year')])

  #         Rank                             Name                               Publisher     Year
  # 179      180                  Madden NFL 2004                         Electronic Arts  Unknown
  # 377      378                 FIFA Soccer 2004                         Electronic Arts  Unknown
  # 431      432       LEGO Batman: The Videogame  Warner Bros. Interactive Entertainment  Unknown
  # 470      471       wwe Smackdown vs. Raw 2006                                 Unknown  Unknown
  # 470      471       wwe Smackdown vs. Raw 2006                                 Unknown  Unknown
  # ...      ...                              ...                                     ...      ...
  # 16427  16430                     Virtua Quest                                 Unknown  Unknown
  # 16493  16496                       The Smurfs                                 Unknown  Unknown
  # 16494  16497  Legends of Oz: Dorothy's Return                                 Unknown   2014.0
  # 16543  16546           Driving Simulator 2011                                 Unknown   2011.0
  # 16553  16556                   Bound By Flame                                 Unknown   2014.0



  ################### CORRELATION ANALYSIS ###################
  ### Calculate the correlation Coefficient matric for the sales columns: (NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)

  # Using .corr() I can calculate the correlation coefficient matrix between the different sales columns
  correlation_matrix = cleaned_video_game_sales[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()
  print('\nCorrelation Matrix for Sales Columns:\n', correlation_matrix)

  #               NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales
  # NA_Sales      1.000000  0.767727  0.449787     0.634737      0.941047
  # EU_Sales      0.767727  1.000000  0.435584     0.726385      0.902836
  # JP_Sales      0.449787  0.435584  1.000000     0.290186      0.611816
  # Other_Sales   0.634737  0.726385  0.290186     1.000000      0.748331
  # Global_Sales  0.941047  0.902836  0.611816     0.748331      1.000000


  ### Identify the pair of distinct variables (excluding one-to-one correlations like NA_Sales with NA_Sales) that have the strongest correlation.

  # Using .abs() I can get the absolute value of the correlation matrix, and combined with .unstack() I can get the correlation values as a series with multiple indices
  correlation_matrix_unstacked = correlation_matrix.abs().unstack()
  correlation_matrix_unstacked = correlation_matrix_unstacked[correlation_matrix_unstacked != 1] # Remove the self correlation values ( 1.000000 )

  print('\nUnstacked Correlation Matrix:\n', correlation_matrix_unstacked)
  # Unstacked Correlation Matrix:
  # NA_Sales      EU_Sales        0.767727
  #               JP_Sales        0.449787
  #               Other_Sales     0.634737
  #               Global_Sales    0.941047
  # EU_Sales      NA_Sales        0.767727
  #               JP_Sales        0.435584
  #               Other_Sales     0.726385
  #               Global_Sales    0.902836
  # JP_Sales      NA_Sales        0.449787
  #               EU_Sales        0.435584
  #               Other_Sales     0.290186
  #               Global_Sales    0.611816
  # Other_Sales   NA_Sales        0.634737
  #               EU_Sales        0.726385
  #               JP_Sales        0.290186
  #               Global_Sales    0.748331
  # Global_Sales  NA_Sales        0.941047
  #               EU_Sales        0.902836
  #               JP_Sales        0.611816
  #               Other_Sales     0.748331

  strongest_pair = correlation_matrix_unstacked.idxmax() # retrieve the index of the strongest correlation
  strongest_pair_value = correlation_matrix_unstacked[strongest_pair] #retrieve the value of the strongest correlation
  print(f'Strongest Pair of Distinct Variables: {strongest_pair}, {strongest_pair_value}')
  # Strongest Pair of Distinct Variables: ('NA_Sales', 'Global_Sales'), 0.9410473571255572


  ### Identify the pair of distinct variables that have the weakest correlation (the value closest to 0).

  weakest_pair = correlation_matrix_unstacked.idxmin() # retrieve the index of the weakest correlation
  weakest_pair_value = correlation_matrix_unstacked[weakest_pair] #retrieve the value of the weakest correlation
  print(f'Weakest Pair of Distinct Variables: {weakest_pair}, {weakest_pair_value}')
  # Weakest Pair of Distinct Variables: ('JP_Sales', 'Other_Sales'), 0.2901862496015262


  #################### INTERPRETATION ###################
  ### Provide a brief interpretation of the correlation findings. Discuss why you think these particular pairs of variables have the strongest and weakest correlations

  """
  
  It does make sense that the strongest collection pair is NA_Sales with Global_Sales with a correlation value of 0.941473571255572. I can probably assume that games made in the NA region are the most popular globablly, and probably that most of the largest game studios are from the NA region. Since the NA region is one of the largest and predominantly english speaking, I can assume the games made in this region are already in English with a possiblility of being translated into other languages. This would make it accessible for other countries that don't speak english to buy and play the games, and it would contribute to NA_Sales high correlation value.

  The weakest pair of variables is JP_sales with Other_Sales with a correlation value of 0.2901862496015262. I can most likely assume that unless a game from japan is translated to english, it will not be popular globally. I do not know how much of the world population can speak japanese, but the language barrier can be a factor that leads to low sales.


  """


