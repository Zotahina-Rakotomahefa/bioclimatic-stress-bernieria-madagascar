# Bioclimatic Stress Analysis of Bernieria madagascariensis

A geospatial climate stress modeling project combining raster-based bioclimatic variables and species occurrence data to assess environmental vulnerability patterns in Madagascar.

---

##  Overview

This project computes a **Climate Stress Index (CSI)** using selected bioclimatic variables and evaluates its spatial relationship with occurrences of *Bernieria madagascariensis* across two districts:

- Moramanga
- Maroantsetra

The workflow integrates raster processing, threshold modeling, spatial clipping, and geospatial visualization.

---

## Objectives

- Clip bioclimatic rasters to district boundaries
- Compute climate thresholds dynamically
- Generate a composite Climate Stress Index
- Overlay species occurrences
- Produce comparative stress maps

---

## Project structure
```
project/
├── outputs/        # Generated rasters
├── notebooks/      # Jupyter notebooks
├── src/            # Python scripts
├── requirements.txt
└── README.md
```

## Installation
```bash
pip install -r requirements.txt
```
---

## Data Sources

The datasets used in this project are not included in this repository due to size and licensing constraints.

### Bioclimatic Variables
Source: WorldClim Version 2.1  
https://www.worldclim.org/data/worldclim21.html  
Variables used: BIO12 (Annual Precipitation), BIO15 (Precipitation Seasonality), BIO19 (Precipitation of Coldest Quarter)

### Administrative Boundaries
Source: GADM (Global Administrative Areas)  
https://gadm.org/

### Species Occurrence Data
Source: GBIF (Global Biodiversity Information Facility)  
https://www.gbif.org/  
Species searched: *Bernieria madagascariensis*

Users must download the datasets directly from the official sources and place them in the `data/raw/` directory before running the analysis.

---

##  Methodology

### Data Loading
- Administrative boundaries
- Species occurrence records
- Bioclimatic raster variables (BIO12, BIO15, BIO19)

### Spatial Processing
- District-level clipping using `geopandas` and `rioxarray`
- Raster masking outside district boundaries

### Threshold Computation
Dynamic thresholds are calculated per district:

- Low precipitation (BIO12)
- High precipitation seasonality (BIO15)
- Low humidity in coldest quarter (BIO19)

### Climate Stress Index (CSI)

The CSI is computed as a composite raster integrating threshold exceedances.

### Visualization

The final output includes:

- Comparative stress maps
- Species occurrence overlay
- Shared colorbar
- Clean cartographic layout

Output example:
stress_climatique_distribution_Bernieria_madagascariensis.png

---

##  Key Output

The project produces a high-resolution comparative visualization of climate stress distribution and species presence across two ecological contexts.

The map highlights potential environmental pressure zones influencing species distribution.

---

##  Scientific Relevance

This workflow can support:

- Climate vulnerability assessment
- Biodiversity risk modeling
- Habitat suitability studies
- Conservation planning
- Ecological impact reporting

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software for academic, research, or commercial purposes, provided that proper attribution is given to the original author.

See the `LICENSE` file for full details
