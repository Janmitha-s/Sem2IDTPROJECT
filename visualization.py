import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d


def plot_partition(
    vor,
    drone_positions,
    drone_names,
    human_positions,
    assignments,
    area_bounds,
    out_path="outputs/voronoi_partition.png"
):

    fig, ax = plt.subplots(figsize=(7, 7))

    voronoi_plot_2d(
        vor,
        ax=ax,
        show_vertices=False,
        show_points=False,
        line_colors="gray",
        line_width=1.5
    )

    ax.scatter(
        drone_positions[:, 0],
        drone_positions[:, 1],
        c="blue",
        s=110,
        marker="^",
        label="Drone B"
    )

    for name, pos in zip(drone_names, drone_positions):
        ax.annotate(
            name,
            pos,
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=8
        )

    ax.scatter(
        human_positions[:, 0],
        human_positions[:, 1],
        c="red",
        s=90,
        marker="o",
        label="Human"
    )

    for i, pos in enumerate(human_positions):
        ax.annotate(
            f"H{i} -> {assignments[i]['assigned_drone']}",
            pos,
            textcoords="offset points",
            xytext=(6, -12),
            fontsize=8,
            color="red"
        )

    ax.set_xlim(area_bounds[0], area_bounds[1])
    ax.set_ylim(area_bounds[2], area_bounds[3])

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")

    ax.set_title(
        "Voronoi Coverage Partitioning"
    )

    ax.legend()
    ax.set_aspect("equal")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()