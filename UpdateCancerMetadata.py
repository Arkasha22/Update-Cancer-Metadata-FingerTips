#Script created by Donald Maruta - 21 Feb 24

#Connect to AGOL
from arcgis.gis import GIS
gis = GIS("home")

#Import Required Modules
import requests, csv, shutil
import pandas as pd
from datetime import datetime

#Copy current metadata file to backup metadata file
shutil.copy2('/arcgis/home/CancerDashboard/Metadata.csv', '/arcgis/home/CancerDashboard/OldMetadata.csv')

#Variables Required to Import Updated Metadata from FingerTips
csv = "https://fingertips.phe.org.uk/api/indicator_metadata/csv/all"
selected_columns = ['Indicator ID', 'Date updated']
new_csv_path = '/arcgis/home/CancerDashboard/Metadata.csv'

#Open the URL Request
response = requests.get(csv)
response.raise_for_status()

#Write to the CSV file
with open(new_csv_path, 'wb') as file:
    file.write(response.content)

#Create Pandas dataframe
df_original = pd.read_csv(new_csv_path)

#Rejig dataframe columns and rename
df_selected_columns = df_original[selected_columns]
df_selected_columns.columns = ['IndicatorId', 'LastUpdatedDate']

# Write the resulting DataFrame to a new CSV file
df_selected_columns.to_csv(new_csv_path, index=False)
