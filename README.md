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

Simple Example:

```python
from wyckoff import WyckoffDatabase

wyckoff = WyckoffDatabase()
data = wyckoff.data

for items in data["2"].wyckoff_positions:
    print(items)

print("Spacegroup 3:") # which is 3-b varient
print(data["3"].wyckoff_positions)
```

for more complex example checkout the [example](https://github.com/anoopkcn/wyckoff/blob/main/examples/usage.py) file

## Info

This implementation uses a standard JSON file for the wyckoff data and implements a dataclass for the Wyckoff positions, add additional checks and validations to ensure data integrity, etc,.

```python
@dataclass
class Wyckoff:
    """Represents a single Wyckoff position with its properties and coordinates."""
    letter: str
    multiplicity: int
    site_symmetry: str = ""
    label: Optional[str] = None
    positions: List[List[Any]] = field(default_factory=list)
    coordinates: List[List[Any]] = field(default_factory=list)

@dataclass
class SpaceGroup:
    """Represents a space group with its Wyckoff positions and additional positions."""
    number: str
    additional_positions: List[List[Any]] = field(default_factory=list)
    wyckoff_positions: List[Wyckoff] = field(default_factory=list)
```

**IMPORTANT: If variations are available for a spacegroup, and functions/dictionary are called/indexed without specifying the variation then first available variation will be returned.**

Following variation types are included in the database:

1. **Unique axis settings**: Suffixes like "-b" and "-c" typically indicate which crystallographic axis is chosen as the unique axis, especially in monoclinic and orthorhombic systems. For example:

   - "3-b" means space group 3 with b-axis as the unique axis
   - "3-c" means space group 3 with c-axis as the unique axis

   Example:

   ```python
   data["3-b"]  # Space group 3 with b-axis as the unique axis
   ```

2. **Origin choice**: Suffixes like "-1" and "-2" usually indicate different origin choices for the same space group:

   - "48-1" is space group 48 with origin choice 1
   - "48-2" is space group 48 with origin choice 2

   Example:

   ```python
   data["48-1"]  # Space group 48 with origin choice 1
   ```

3. **Cell choices**: Some suffixes may represent different conventional cell choices (hexagonal vs. rhombohedral settings in trigonal groups, for example).

   Example:

   ```python
   data["148-hexagonal"]  # Space group 148 with hexagonal cell
   ```

## Data Source

This implementation is inspierd by a utility fuction in [doped](https://github.com/SMTG-Bham/doped/tree/main) project. That version used a non-standard datafile and string parsing the Wyckoff positions from [bilbao crystallographic server](https://www.cryst.ehu.es/).

## License

MIT
