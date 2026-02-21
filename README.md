# Bioclimatic Stress Analysis (Madagascar)

## Description
This project computes bioclimatic variables clipped to selected districts
(Moramanga and Maroantsetra) using WorldClim data.

## Project structure
```
project/
├── data/           # Put raw data here
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

## Data preparation
Place the following inside `data/`:

- bioclimate rasters (WorldClim)
- administrative boundaries
- occurrence data

## Usage
Run the script:

```bash
python src/main.py
```

Or open the notebook in `notebooks/analysis.ipynb`.

## Notes
- Do NOT upload large raster files to GitHub.
- Use relative paths for portability.
