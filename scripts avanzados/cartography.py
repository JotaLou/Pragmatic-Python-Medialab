'''
Curso Pragmatic Python, Medialab. Autor: José Luis Muñiz Traviesas
Ejemplo de cartografía básica mediante python, muestra algunas capitales de sudamérica

Python dispone de muchas librerías para cartografía / GIS
https://hex.tech/templates/data-visualization/python-mapping-libraries/

'''
# Script basado en: https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from geodatasets import get_path   # Para descargar datasets de mapas
import mplcursors       # Para etiquetas interactivas (hover)

df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)
# Creamos un tipo de data geográfico
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

print(gdf.head())
# Descargamos el mapa
world = geopandas.read_file(get_path("naturalearth.land"))

# Lo centramos en Sudamérica
ax = world.clip([-90, -55, -25, 15]).plot(color="white", edgecolor="black")

# Dibujamos los puntos contenidos en el dataframe 
gdf.plot(ax=ax, color="red")

# Añadimos las etiquetas interactivas
cursor = mplcursors.cursor(hover=2)
cursor.connect(event="add",func=lambda sel: sel.annotation.set_text(df["City"][sel.index]))
# Mostramos el mapa
plt.show()