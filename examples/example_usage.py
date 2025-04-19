#!/usr/bin/env python
# Example script demonstrating how to use the wyckoff package

from wyckoff import WyckoffDatabase

def main():
    print("Example usage of the Wyckoff package\n")

    wycoff = WyckoffDatabase()
    data = wycoff.data

    def wyckoff_positions(sgn):
        try:
            space_group = data[str(sgn)]
            return {pos.label: pos.positions for pos in space_group.wyckoff_positions if pos.label is not None}
        except KeyError:
            return {}

    available_groups = list(data.keys())
    total_space_groups = len(available_groups)
    print(f"Number of space groups: {total_space_groups} (230 standard + {len(available_groups) - 230} variations)")

    print("\nSpace group 1(unformatted):")
    print(data["1"]) # Type SpaceGroup

    print("\nSpace group 1(formatted):")
    print(f"\t{data['1'].wyckoff_positions[0].label}: {data['1'].wyckoff_positions[0].positions}")

    print("\nSpace group 2:")
    for item in data["2"].wyckoff_positions:
        print(f"\t{item.label}: {item.positions}")

    # space group for 5 is variant 5-b
    for sg in [3, 5]:
        print(f"\nSpace group {sg}:")
        positions = wyckoff_positions(sg)
        for label, position_data in positions.items():
            print(f" \t{label}: {position_data}")

    print("\nSpace group 3 first label:")
    print(data["3"].wyckoff_positions[0].label)

    # print("\nSpace group 48-1:")
    # positions = wyckoff_positions("48-1")
    # for label, position_data in positions.items():
    #     print(f"\t{label}: {position_data}")


    # print("\nSpace group 148-hexagonal:")
    # positions = wyckoff_positions("148-hexagonal") #148
    # for label, position_data in positions.items():
    #     print(f"\t{label}: {position_data}")

    # # Try a non-existent space group
    print("\nNon-existent space group 999:")
    print(wyckoff_positions(999))

if __name__ == "__main__":
    main()
