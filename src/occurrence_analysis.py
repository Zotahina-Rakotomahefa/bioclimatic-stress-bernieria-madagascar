
import geopandas as gpd

def extract_occurrences_by_districts(occ_gdf, moramanga, maroantsetra):
    occ_mora = extract_occurrences(occ_gdf, moramanga)
    occ_maro = extract_occurrences(occ_gdf, maroantsetra)

    return occ_mora, occ_maro
