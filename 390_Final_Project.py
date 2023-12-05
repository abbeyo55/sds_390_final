# import packages
import pandas as pd

# Load and view raw data
url = 'https://raw.githubusercontent.com/abbeyo55/sds_390_final/main/REMS_Mars_Dataset.csv'
mars = pd.read_csv(url)
mars



# Data cleaning

# Create properly formatted datetime index
mars['earth_date_time'] = mars['earth_date_time'].astype(str)
mars['date'] = mars['earth_date_time'].str.replace('Earth, ', '').str.replace(' UTC', '') # remove unnecessary info to get just the date
mars['date'] = pd.to_datetime(mars['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

mars