import pandas as pd

if __name__ == "__main__":
  coffee_sales = pd.DataFrame({
    'Americano': [562, 623], 
    'Latte': [812, 925], 
    'Espresso': [426, 384], 
    'Cappuccino': [852, 756]},
    index=['2021 Sales', '2022 Sales'])

  print(coffee_sales)

  ######################## DATA MANIPULATION ########################

  # Calculate Sales for each beverage across the two years
  total_sales_df = coffee_sales.sum()

  # print(total_sales_df)
  # Americano     1185
  # Latte         1737
  # Espresso       810
  # Cappuccino    1608
  # 
  # It seems that Lattes and Cappucinos are the 2 most popular drinks sold at the cafe!


  # Find the year-over-year grwoth rate for each beverage type
  # print(coffee_sales.describe())
  growth_df = coffee_sales.diff()
  # I decided to use .diff() function since it would show the difference year by year
  # If there had been more year sales, it would probably keep going and makes sense that the
  # first year is NaN because there is no previous value to compare it to

  # print(growth_df)
  #               Americano  Latte  Espresso  Cappuccino
  # 2021 Sales        NaN    NaN       NaN         NaN
  # 2022 Sales       61.0   113.0     -42.0       -96.0
  # 
  # -138 + 174 = 36, there is an overall positive increase in sales from the previous year!
  # Also maybe people started moving towards lattes and americanos! 

  ######################## BUSINESS INSIGHTS ########################

  # Identify the best-selling and least-selling beverage for each year
  best_worst_df = pd.DataFrame({
    'Best Seller': coffee_sales.apply(pd.Series.idxmax, axis=1),
    'Worst Seller': coffee_sales.apply(pd.Series.idxmin, axis=1)
  })
  # The previous DataFrame retrieves the index of the max value and min value for each column and combines them together

  # print(best_worst_df)
  #            Best Seller Worst Seller
  # 2021 Sales  Cappuccino     Espresso
  # 2022 Sales       Latte     Espresso
  # 
  # Straight regular espresso doesn't seem to be very popular drink! 


  # Brief Analysis of what these sales figures might suggest for JavaBeans' marketing product strategy
  # From the sales figures, it seems that JavaBeans is doing pretty well as there an increase in drink
  # sales from 2021 to 2022 figures. From overall sales from 2021, there was an increase of 31 drinks bought
  # I think their product marketing strategy is going well if it is an overall positive increase. Even though
  # some of the drinks had a negative difference, they might have just decided to go for another drink than
  # their usual. Without more data and information, this is probably the extent of what I can analyze.



