# Wyckoff

A Python package for working with Wyckoff positions in crystallography.

## Installation

```bash
pip install wyckoff
```

## Usage

```python
from wyckoff import get_wyckoff_dict_from_sgn, get_wyckoff_database

# Get Wyckoff positions for a specific space group
wyckoff_positions = get_wyckoff_dict_from_sgn(1)  # Space group 1
print(wyckoff_positions)

# Get the entire database
database = get_wyckoff_database()
print(list(database.keys())[:5])  # Print first 5 space group numbers
```

## Data Source

This package is based on crystallographic data from the International Tables for Crystallography.
The original implementation is derived from the [doped](https://github.com/SMTG-Bham/doped/tree/main) project:
S. R. Kavanagh et al. doped: Python toolkit for robust and repeatable charged defect supercell calculations. Journal of Open Source Software 9 (96), 6433, 2024.

## License

MIT