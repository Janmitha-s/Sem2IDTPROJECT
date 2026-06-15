import json


def save_assignments(assignments,
                     out_path="outputs/zone_assignments.json"):

    with open(out_path, "w") as f:
        json.dump(assignments, f, indent=2)