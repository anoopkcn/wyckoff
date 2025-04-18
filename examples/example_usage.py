#!/usr/bin/env python
# Example script demonstrating how to use the wyckoff package

from wyckoff import get_wyckoff_dict_from_sgn, get_wyckoff_database


def main():
    print("Example usage of the Wyckoff package\n")
    
    # Get the entire database
    print("Loading the entire Wyckoff database...")
    database = get_wyckoff_database()
    available_groups = list(database.keys())
    print(f"Available space groups: {available_groups}\n")
    
    # Get Wyckoff positions for specific space groups
    for sg in [1, 2]:
        print(f"\nSpace group {sg}:")
        wyckoff_positions = get_wyckoff_dict_from_sgn(sg)
        for label, positions in wyckoff_positions.items():
            print(f"  {label}: {positions}")

    # Try a non-existent space group
    print("\nNon-existent space group 999:")
    print(get_wyckoff_dict_from_sgn(999))


if __name__ == "__main__":
    main()