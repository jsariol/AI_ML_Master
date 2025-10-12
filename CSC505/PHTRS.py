
DESCRIPTION = (
    "PHTRS is a web-based system where citizens report potholes and track status; "
    "dispatchers create work orders and assign crews; crew leads update repair status "
    "and log hours/materials; finance computes repair cost and reviews claims. "
    "Address and district are validated via an external GIS service."
)

ACTORS = [
    "Citizen",
    "Dispatcher / Intake",
    "Crew Lead",
    "Finance / Accounting",
    "Public Works Manager",
    "GIS / Geocoding Service (external)"
]

USE_CASES = [
    "Report Pothole",
    "Track Pothole Status",
    "Submit Damage Claim",
    "Create Work Order",
    "Assign Crew & Schedule",
    "Update Repair Status",
    "Log Hours/Materials/Equipment",
    "Compute Repair Cost",
    "Search & Analytics",
    "Manage Users/Roles",
    "Validate Address & District (include)"
]

RELATIONSHIPS = {
    "Citizen": [
        "Report Pothole",
        "Track Pothole Status",
        "Submit Damage Claim"
    ],
    "Dispatcher / Intake": [
        "Create Work Order",
        "Assign Crew & Schedule",
        "Search & Analytics"
    ],
    "Crew Lead": [
        "Update Repair Status",
        "Log Hours/Materials/Equipment"
    ],
    "Finance / Accounting": [
        "Compute Repair Cost",
        "Search & Analytics"
    ],
    "Public Works Manager": [
        "Search & Analytics",
        "Manage Users/Roles"
    ],
    "GIS / Geocoding Service (external)": [
        "Validate Address & District (include)"
    ]
}

def main():
    print("=== PHTRS — UML Use Case Overview ===\n")
    print("Brief Description:")
    print(f"  {DESCRIPTION}\n")

    print("Actors:")
    for a in ACTORS:
        print(f"  - {a}")
    print(f"Total actors: {len(ACTORS)}\n")

    print("Use Cases:")
    for uc in USE_CASES:
        print(f"  - {uc}")
    print(f"Total use cases: {len(USE_CASES)}\n")

    print("Actor → Use Cases:")
    for actor, ucs in RELATIONSHIPS.items():
        print(f"  {actor}:")
        for uc in ucs:
            print(f"    • {uc}")
    print("\n=== End ===")

if __name__ == "__main__":
    main()
