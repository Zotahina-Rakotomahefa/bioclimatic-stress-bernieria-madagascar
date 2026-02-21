
import numpy as np


def 
for var in VARIABLES:
    print(f"Clipping variable {var}...")

    safe_clip(var, moramanga, "Moramanga", CLIMATE_PATH, CLIMATE_PATH)
    safe_clip(var, maroantsetra, "Maroantsetra", CLIMATE_PATH, CLIMATE_PATH)

print("Clipping terminé.")


bio12_mora = load_clipped_raster(12, "Moramanga", CLIMATE_PATH)
bio15_mora = load_clipped_raster(15, "Moramanga", CLIMATE_PATH)
bio19_mora = load_clipped_raster(19, "Moramanga", CLIMATE_PATH)


bio12_maro = load_clipped_raster(12, "Maroantsetra", CLIMATE_PATH)
bio15_maro = load_clipped_raster(15, "Maroantsetra", CLIMATE_PATH)
bio19_maro = load_clipped_raster(19, "Maroantsetra", CLIMATE_PATH)


print("Moramanga humid mean:",
      float(bio19_mora.mean(dim=["x", "y"])))

print("Maroantsetra humid mean:",
      float(bio19_maro.mean(dim=["x", "y"])))



thresholds_mora = compute_thresholds(
    bio12_mora,
    bio15_mora,
    bio19_mora
)

print("\nMoramanga thresholds:")
print("Bio12 low:", thresholds_mora[0])
print("Bio15 high:", thresholds_mora[1])
print("Bio19 low:", thresholds_mora[2])


thresholds_maro = compute_thresholds(
    bio12_maro,
    bio15_maro,
    bio19_maro
)

print("\nMaroantsetra thresholds:")
print("Bio12 low:", thresholds_maro[0])
print("Bio15 high:", thresholds_maro[1])
print("Bio19 low:", thresholds_maro[2])

stress_index_mora = compute_stress_index(
    bio12_mora,
    bio15_mora,
    bio19_mora,
    *thresholds_mora
)

stress_index_maro = compute_stress_index(
    bio12_maro,
    bio15_maro,
    bio19_maro,
    *thresholds_maro
)
