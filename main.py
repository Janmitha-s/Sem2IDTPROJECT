from config import (
    AREA_BOUNDS,
    drone_positions,
    drone_names,
    human_positions
)

from partition import (
    build_partition,
    assign_targets
)

from visualization import plot_partition

from utils import save_assignments


def main():

    vor, tree = build_partition(drone_positions)

    assignments = assign_targets(
        tree,
        drone_names,
        drone_positions,
        human_positions
    )

    for a in assignments:
        print(
            f"Target {a['target_id']} at "
            f"{a['position_m']} -> "
            f"{a['assigned_drone']} "
            f"({a['distance_to_drone_m']:.1f} m)"
        )

    save_assignments(assignments)

    plot_partition(
        vor,
        drone_positions,
        drone_names,
        human_positions,
        assignments,
        AREA_BOUNDS
    )

    print("Done")


if __name__ == "__main__":
    main()