
import os
import gc
import rioxarray as rxr


def safe_clip(var_number, district_gdf, district_name,
              climate_path, output_path):

    file_name = f"wc2.1_30s_bio_{var_number}.tif"
    file_path = os.path.join(climate_path, file_name)

    raster = rxr.open_rasterio(
        file_path,
        masked=True,
        chunks=True
    ).rio.write_crs("EPSG:4326")

    minx, miny, maxx, maxy = district_gdf.total_bounds

    cropped = raster.rio.clip_box(
        minx=minx,
        miny=miny,
        maxx=maxx,
        maxy=maxy
    )

    clipped = cropped.rio.clip(
        district_gdf.geometry,
        district_gdf.crs,
        drop=True
    )

    output_file = os.path.join(
        output_path,
        f"bio{var_number}_{district_name.lower()}.tif"
    )

    clipped.rio.to_raster(output_file)

    del raster, cropped, clipped
    gc.collect()
