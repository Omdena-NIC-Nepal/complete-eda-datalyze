# import pandas as pd
# print(pd.__version__)

# import sys
# print(sys.executable)


# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot styling
plt.style.use('seaborn-whitegrid')
sns.set_palette('viridis')
# %matplotlib inline



# Load the dataset
df = pd.read_csv('data/Climate_Change_Indicators.csv') # Place the correct path to the file you are reading here (Make sure to load using the relative path)

# Display the first few rows of the dataset
df.head()




# Check for missing values and basic information about the dataset
print("Dataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())




# TODO: Aggregate data by year to create a 124-year time series
# Your code here
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

df_yearly = df.groupby('Year').mean().reset_index()

df_yearly.head()