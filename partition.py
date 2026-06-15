from scipy.spatial import Voronoi, cKDTree


def build_partition(drone_positions):
    vor = Voronoi(drone_positions)
    tree = cKDTree(drone_positions)
    return vor, tree


def assign_targets(tree,
                   drone_names,
                   drone_positions,
                   human_positions):

    distances, zone_idx = tree.query(human_positions)

    assignments = []
    for i, (pos, zone, dist) in enumerate(
        zip(human_positions, zone_idx, distances)
    ):

        assignments.append({
            "target_id": i,
            "position_m": pos.tolist(),
            "assigned_drone": drone_names[zone],
            "drone_position_m": drone_positions[zone].tolist(),
            "distance_to_drone_m": float(dist),
            "recording_file":
                f"reflected_signal_{drone_names[zone]}.csv"
        })

    return assignments