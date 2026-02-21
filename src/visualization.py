
import os
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import box
from matplotlib.lines import Line2D


def plot_stress_map_comparison(
    stress_index_maro,
    maroantsetra,
    occ_maro,
    stress_index_mora,
    moramanga,
    occ_mora,
    output_path
)

    fig, axes = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(17,7),
        constrained_layout=True
    )

    datasets = [
        (stress_index_maro, maroantsetra, occ_maro, "Maroantsetra"),
        (stress_index_mora, moramanga, occ_mora, "Moramanga")
    ]

    mappable = None

    for ax, (raster, region, occ, title) in zip(axes, datasets):

        ax.set_facecolor("white")

        
        im = raster.plot(
            ax=ax,
            cmap="RdYlGn_r",
            alpha=0.85,
            add_colorbar=False,
            zorder=1
        )
        mappable = im

        
        xmin, ymin, xmax, ymax = raster.rio.bounds()
        full_extent = box(xmin, ymin, xmax, ymax)

        mask = gpd.GeoDataFrame(
            geometry=[full_extent],
            crs=region.crs
        )
        mask["geometry"] = mask.geometry.difference(region.unary_union)
        mask.plot(ax=ax, color="white", zorder=2)

        
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

       
        region.boundary.plot(
            ax=ax,
            color="grey",
            linewidth=2,
            zorder=3
        )

      
        occ.plot(
            ax=ax,
            color="blue",
            markersize=35,
            edgecolor="white",
            linewidth=1,
            zorder=10
        )

        ax.set_title(
            f"Distribution of Bernieria madagascariensis and climate stress index in {title}",
            fontsize=11
        )
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")

    
    cbar = fig.colorbar(
        mappable,
        ax=axes,
        orientation="vertical",
        shrink=0.85,
        pad=0.02
    )

    cbar.set_label("Climate Stress Index", fontsize=11)

  
    legend_elements = [
        Line2D(
            [0], [0],
            marker='o',
            color='none',
            label='Bernieria madagascariensis',
            markerfacecolor='blue',
            markeredgecolor='white',
            markersize=10
        )
    ]

    fig.legend(
        handles=legend_elements,
        loc="lower center",
        ncol=1,
        frameon=True,
        fontsize=12
    )

   
    filename = "stress_climatique_distribution_Bernieria_madagascariensis.png"
    file_path = os.path.join(output_path, filename)

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()
