import geopandas as gpd
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg

# Create an empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()

# Create a new column called 'geometry' to the GeoDataFrame
newdata['geometry'] = None

# Coordinates of the Helsinki Senate square in Decimal Degrees
coordinates = [(68.286203,27.887253),(68.339318,27.888519),(68.339854,27.859459),(68.268450,27.861073)]

# Create a Shapely polygon from the coordinate-tuple list
poly = Polygon(coordinates)

# Insert the polygon into 'geometry' -column at index 0
newdata.loc[0, 'geometry'] = poly

# Add a new column and insert data
newdata.loc[0, 'NAME'] = 'XYZ'

# Set the GeoDataFrame's coordinate system to WGS84 (i.e. epsg code 4326)
newdata.crs = from_epsg(4326)

# Determine the output path for the Shapefile
outfp = r"D:\Shapefiles\file.shp"

# Write the data into that Shapefile
newdata.to_file(outfp)