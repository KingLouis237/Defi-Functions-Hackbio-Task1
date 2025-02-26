# Simplified Bioinformatics Toolkit

## Overview
This repository contains a set of Python functions designed for common bioinformatics tasks. These include:

1. **DNA to Protein Translation**: Converts a DNA sequence into a simplified protein sequence.
2. **Logistic Population Growth Simulation**: Models population growth with randomized lag and exponential phases.
3. **Generating Multiple Growth Curves**: Creates a dataset with 100 different growth curves.
4. **Finding Time to Reach 80% of Maximum Growth**: Determines when population growth reaches 80% of its carrying capacity.
5. **Hamming Distance Calculation**: Computes the difference between two strings, useful for comparing usernames.

## Features
- **Efficient and concise** implementations of bioinformatics functions.
- **Randomized growth curve generation**, simulating biological population dynamics.
- **Easy-to-use visualization** for population growth curves.
- **Simple string analysis tool** for calculating Hamming distance.

## Installation
To run this project, you need Python 3 installed along with the following dependencies:

```bash
pip install pandas numpy matplotlib
```

## Usage

### 1. DNA to Protein Translation
```python
from toolkit import translate_dna

dna_sequence = "AACCCGTTG"
protein_sequence = translate_dna(dna_sequence)
print(protein_sequence)  # Output: ACX
```

### 2. Logistic Growth Simulation
```python
from toolkit import generate_growth_curves

growth_data = generate_growth_curves(num_curves=100)
print(growth_data.head())
```

### 3. Time to Reach 80% of Maximum Growth
```python
from toolkit import find_80_percent_time

time_to_80 = find_80_percent_time(growth_data)
print(time_to_80)
```

### 4. Hamming Distance Calculation
```python
from toolkit import calculate_hamming_distance

distance = calculate_hamming_distance("biodata_user", "data_science")
print(distance)  # Output: Hamming distance value
```

## Example Execution
Run the example script to see all functions in action:
```bash
python toolkit.py
```

## Contributors
This project was developed as part of the **HackBio Internship**.


