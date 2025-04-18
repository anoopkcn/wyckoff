# Wyckoff

A Python package for working with Wyckoff positions in crystallography.

## Installation

```bash
pip install wyckoff
```
OR
```bash
uv add wyckoff
```

## Usage

```python
from wyckoff import wyckoff_positions, wyckoff_database

# Get Wyckoff positions for a specific space group
positions = wyckoff_positions(1)  # Space group 1
print(positions)

# Get the entire database
database = wyckoff_database()
print(list(database.keys())[:5])  # Print first 5 space group numbers
```

# Info

If spacegroup variations are available, and functions are called without specifying the variabtion then first variation will be returned.

**Following variation types are included in the database:**

1. **Unique axis settings**: Suffixes like "-b" and "-c" typically indicate which crystallographic axis is chosen as the unique axis, especially in monoclinic and orthorhombic systems. For example:
   - "3-b" means space group 3 with b-axis as the unique axis
   - "3-c" means space group 3 with c-axis as the unique axis

Example:
```python
positions = wyckoff_positions("3-b")  # Space group 3 with b-axis as the unique axis
print(positions)
```

2. **Origin choice**: Suffixes like "-1" and "-2" usually indicate different origin choices for the same space group:
   - "48-1" is space group 48 with origin choice 1
   - "48-2" is space group 48 with origin choice 2

Example:
```python
positions = wyckoff_positions("48-1")  # Space group 48 with origin choice 1
print(positions)
```
3. **Cell choices**: Some suffixes may represent different conventional cell choices (hexagonal vs. rhombohedral settings in trigonal groups, for example).

Example:
```python
positions = wyckoff_positions("148-hexagonal")  # Space group 148 with hexagonal cell
print(positions)
```

## Data Source

This package is based on crystallographic data from the International Tables for Crystallography.
The original implementation is derived from the [doped](https://github.com/SMTG-Bham/doped/tree/main) project:
S. R. Kavanagh et al. doped: Python toolkit for robust and repeatable charged defect supercell calculations. Journal of Open Source Software 9 (96), 6433, 2024.

## License

MIT
