
import os
import pandas as pd
import geopandas as gpd
import rioxarray as rxr


def load_raster(var_number, climate_path):
    file_name = f"wc2.1_30s_bio_{var_number}.tif"
    raster = rxr.open_rasterio(
        os.path.join(climate_path, file_name),
        masked=True
    )
    raster.rio.write_crs("EPSG:4326", inplace=True)
    return raster


def load_clipped_raster(var_number, district, climate_path):
    file_name = f"bio{var_number}_{district.lower()}.tif"
    return rxr.open_rasterio(
        os.path.join(climate_path, file_name),
        masked=True
    ).squeeze()


def load_districts(admin_path):
    moramanga = gpd.read_file(
        os.path.join(admin_path, "moramanga.shp")
    ).to_crs("EPSG:4326")

    maroantsetra = gpd.read_file(
        os.path.join(admin_path, "maroantsetra.shp")
    ).to_crs("EPSG:4326")

    return moramanga, maroantsetra


def load_occurrences(occ_path):
    occ_file = os.path.join(occ_path, "species.csv")
    occ = pd.read_csv(occ_file, sep="\t")

    occ = occ[[
        "species",
        "decimalLatitude",
        "decimalLongitude",
        "year"
    ]].dropna(subset=["decimalLatitude", "decimalLongitude"])

    occ_gdf = gpd.GeoDataFrame(
        occ,
        geometry=gpd.points_from_xy(
            occ.decimalLongitude,
            occ.decimalLatitude
        ),
        crs="EPSG:4326"
    )

    return occ_gdf
