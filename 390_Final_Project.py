# import packages
import pandas # import packages
import pandas as pd

# Load and view raw data
url = 'https://raw.githubusercontent.com/abbeyo55/sds_390_final/main/REMS_Mars_Dataset.csv'
mars = pd.read_csv(url)
mars