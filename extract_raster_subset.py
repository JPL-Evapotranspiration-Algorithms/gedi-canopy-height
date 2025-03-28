# %%
from sentinel_tiles import sentinel_tiles
from gedi_canopy_height import GEDICanopyHeight

# %%
gedi = GEDICanopyHeight()
gedi

# %%
geometry = sentinel_tiles.grid("11SLT")
geometry

# %%
canopy_height = gedi.canopy_height_meters(geometry)
canopy_height

# %%
canopy_height.to_geotiff("GEDI_11SLT.tif")

# %%
canopy_height.cmap

# %%



