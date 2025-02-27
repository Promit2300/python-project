
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)



df = pd.read_csv('data.csv')

print(df.to_string()) 

print(pd.options.display.max_rows) 