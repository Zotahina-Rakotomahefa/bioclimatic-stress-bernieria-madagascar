
import os

BASE_PATH = "/content/drive/MyDrive/Bioclimatic_Analysis"

CLIMATE_PATH = os.path.join(BASE_PATH, "data/bioclimate")
ADMIN_PATH   = os.path.join(BASE_PATH, "data/admin")
OCC_PATH     = os.path.join(BASE_PATH, "data/occurrence")
OUTPUT_PATH  = os.path.join(BASE_PATH, "outputs")

VARIABLES = [1, 12, 15, 18, 19]

os.makedirs(OUTPUT_PATH, exist_ok=True)
