import pandas
df=pandas.read_csv("http://pythonhow.com/supermarkets.csv")
import geopy
from geopy.geocoders import ArcGIS
nom = ArcGIS()
n=nom.geocode("3995 23rd St, San Francisco, CA94114")
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
df["Coordinates"]=df["Address"].apply(nom.geocode)
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x !=None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.latitude if x !=None else None)
df
