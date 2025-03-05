import pandas as pd
import numpy as np

"""

Student: Keiffer Tan
AD450 - Data Science Winter 2025

Assignment: Analysis of Coffee Production Types (1990 - 2020)

Overview
In this assignment, you will explore the coffee production data from 1990 to 2020, focusing on different types of coffee, such as Robusta, Arabica, and blends like Arabica/Robusta and Robusta/Arabica. Your task will involve data aggregation, transformation, and correlation analysis to uncover patterns and relationships in coffee production over three decades.

Objectives
- Aggregate coffee production data by type over a 30-year period.
- Transpose the aggregated data to facilitate correlation analysis.
- Calculate and analyze the correlation matrix to identify the strength of relationships between different coffee types

"""

# coffee_domestic_consumption = './coffee_data/coffee_domestic_consumption.csv'
# coffee_export = './coffee_data/coffee_export.csv'
# coffee_green_coffee_inventories = './coffee_data/coffee_green_coffee_inventories.csv'
# coffee_import = './coffee_data/coffee_import.csv'
# coffee_importers_consumption = './coffee_data/coffee_importers_consumption.csv'
coffee_production = './coffee_data/coffee_production.csv'
# coffee_re_export = './coffee_data/coffee_re_export.csv'

if __name__ == "__main__":

  # I actaully only needed the coffee production data

  ############################### LOAD DATA ###############################
  # c_domestic_consumption = pd.read_csv(coffee_domestic_consumption)
  # c_export = pd.read_csv(coffee_export)
  # c_green_coffee_invetories = pd.read_csv(coffee_green_coffee_inventories)
  # c_import = pd.read_csv(coffee_import)
  # c_importers_consumption = pd.read_csv(coffee_importers_consumption)
  c_production = pd.read_csv(coffee_production)
  # c_re_export = pd.read_csv(coffee_re_export)

  # print(c_domestic_consumption.head())
  # print(c_export.head())
  # print(c_green_coffee_invetories.head())
  # print(c_import.head())
  # print(c_importers_consumption.head())
  print(c_production.head())
  # print(c_re_export.head())

  ############################# IDENTIFY MISSING DATA ###############################
  missing_data = c_production.isnull().sum().sum()
  print(f'\n\nTotal Missing Data: {missing_data}')

  # Missing Data in each column: 0

  # Identify the year columns (columns that are int64 dtypes) to make sure each cell is a number
  year_columns = c_production.columns.difference(['country', 'coffee_type'], sort=False)

  # .map tries to convert each cell to a number, if it can't, it will return NaN
  # Count the number of non-numeric values
  non_numeric_values = c_production[year_columns].map(lambda x: pd.to_numeric(x, errors='coerce')).isna().sum().sum()
  print(f'Total Non-Numeric Values: {non_numeric_values}\n\n')

  # Should be fine since there are no missing data cells

  ################################ DATA AGGREGATION ###############################
  # Group the coffee production data by type for each year from 1990 to 2020.
  # Summarize the data to reflect total production volumes for each coffee type per year.

  coffee_production_by_type = c_production.groupby(['coffee_type']).sum() # Aggregate coffee production data by type of coffee
  coffee_production_by_type = coffee_production_by_type.drop(columns='country') # Drop the 'country' column
  print(coffee_production_by_type.head())

  #                      1990_1991   1991_1992   1992_1993   1993_1994  ...   2016_2017   2017_2018   2018_2019   2019_2020  total_production        
  # coffee_type                                                         ...
  # Arabica             1807140000  2073960000  1895580000  1593720000  ...  2429880000  2431260000  2445300000  2341020000       57968520000        
  # Arabica/Robusta     2399820000  2409960000  2787060000  2492700000  ...  4042620000  3822840000  4603500000  4122780000       96668400000        
  # Robusta              266400000   354840000   228840000   198840000  ...   153240000   185940000   214800000   200100000        7617780000        
  # Robusta/Arabica     1120440000  1237380000   999780000  1220280000  ...  3113340000  3381540000  3084180000  3239280000       63480120000



  ############################## DATA TRANSFORMATION ###############################
  # Transpose the aggregated data so that coffee types become the rows and years become the columns.
  # This reorientation will prepare your data for the next step of correlation analysis.

  coffee_production_by_type_transposed = coffee_production_by_type.transpose()
  print(coffee_production_by_type_transposed.head())

  # coffee_type     Arabica  Arabica/Robusta    Robusta  Robusta/Arabica
  # 1990_1991    1807140000       2399820000  266400000       1120440000
  # 1991_1992    2073960000       2409960000  354840000       1237380000
  # 1992_1993    1895580000       2787060000  228840000        999780000
  # 1993_1994    1593720000       2492700000  198840000       1220280000
  # 1994_1995    1715940000       2503560000  269700000       1109640000



  ############################## CORRELATION ANALYSIS ###############################
  # Using the Pandas library in Python, apply the corr() method to your transposed dataset to compute the correlation matrix.
  # The correlation matrix should show the relationship coefficients between each pair of coffee types.

  # Using .corr() I can calculate the correlation coefficient matrix between the different sales columns
  correlation_matrix = coffee_production_by_type_transposed.corr()
  print('\nCorrelation Matrix for Coffee Types:\n', correlation_matrix)

  # coffee_type       Arabica  Arabica/Robusta   Robusta  Robusta/Arabica
  # coffee_type
  # Arabica          1.000000         0.999478  0.997664         0.998687
  # Arabica/Robusta  0.999478         1.000000  0.996951         0.999219
  # Robusta          0.997664         0.996951  1.000000         0.994697
  # Robusta/Arabica  0.998687         0.999219  0.994697         1.000000

  # Using .abs() I can get the absolute value of the correlation matrix, and combined with .unstack() I can get the correlation values as a series with multiple indices
  correlation_matrix_unstacked = correlation_matrix.abs().unstack()
  correlation_matrix_unstacked = correlation_matrix_unstacked[correlation_matrix_unstacked != 1] # Remove the self correlation values ( 1.000000 )

  print('\nUnstacked Correlation Matrix:\n', correlation_matrix_unstacked)
  # Unstacked Correlation Matrix:
  # coffee_type      coffee_type
  # Arabica          Arabica/Robusta    0.999478
  #                  Robusta            0.997664
  #                  Robusta/Arabica    0.998687
  # Arabica/Robusta  Arabica            0.999478
  #                  Robusta            0.996951
  #                  Robusta/Arabica    0.999219
  # Robusta          Arabica            0.997664
  #                  Arabica/Robusta    0.996951
  #                  Robusta/Arabica    0.994697
  # Robusta/Arabica  Arabica            0.998687
  #                  Arabica/Robusta    0.999219
  #                  Robusta            0.994697


  ################################ QUESTIONS ###############################
  ### Examine the correlation matrix. Which two coffee types have the strongest correlation in production volumes over the years? What might this imply about their production dynamics?

  strongest_pair = correlation_matrix_unstacked.idxmax() # retrieve the index of the strongest correlation
  strongest_pair_value = correlation_matrix_unstacked[strongest_pair] #retrieve the value of the strongest correlation
  print(f'Strongest Pair of Distinct Variables: {strongest_pair}, {strongest_pair_value}')
  # Strongest Pair of Distinct Variables: ('Arabica', 'Arabica/Robusta'), 0.9994776649144114

  ### Identify the two coffee types with the weakest correlation. Discuss possible reasons for this weak relationship and any external factors that might influence these production types differently.

  weakest_pair = correlation_matrix_unstacked.idxmin() # retrieve the index of the weakest correlation
  weakest_pair_value = correlation_matrix_unstacked[weakest_pair] #retrieve the value of the weakest correlation
  print(f'Weakest Pair of Distinct Variables: {weakest_pair}, {weakest_pair_value}')

  # Weakest Pair of Distinct Variables: ('Robusta', 'Robusta/Arabica'), 0.9946972881075378



