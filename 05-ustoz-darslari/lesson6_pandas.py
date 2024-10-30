# # Import all libraries needed for the tutorial

# # General syntax to import specific functions in a library: 
# ##from (library) import (specific library function)
# from pandas import DataFrame, read_csv

# # General syntax to import a library but no functions: 
# ##import (library) as (give the library a nickname/alias)
# import matplotlib.pyplot as plt
# import pandas as pd #this is how I usually import pandas
# import sys #only needed to determine Python version number
# import matplotlib #only needed to determine Matplotlib version number

# # Enable inline plotting
# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
# print('Matplotlib version ' + matplotlib.__version__)


# # The initial set of baby names and birth rates
# names = ['Bob','Jessica','Mary','John','Mel']
# births = [968, 155, 77, 578, 973]

# BabyDataSet = list(zip(names,births))
# BabyDataSet
# print(BabyDataSet)




import pandas as pd
from csv import reader as csv_reader

def csv_to_json(csv_path: str, headers: bool) -> list:
  '''Convert data from a csv to json'''
  # store json data
  json_data = []
  
  try:
    with open(csv_path, 'r') as file:
      reader = csv_reader(file)
      # set column names using first row
      if headers:
        columns = next(reader)
      
      # convert csv to json
      for row in reader:
        row_data = {}
        for i in range(len(row)):
          # set key names
          if headers:
            row_key = columns[i].lower()
          else: 
            row_key = i
          # set key/value
          row_data[row_key] = row[i]
        # add data to json store 
        json_data.append(row_data)
        
  # error handling
  except Exception as e:
    print(repr(e))
    
  return json_data


df = pd.read_csv('uzum.csv')
dfhead = df.head()

print(csv_to_json(df, dfhead))