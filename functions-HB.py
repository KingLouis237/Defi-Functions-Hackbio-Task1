# Simplified Bioinformatics Toolkit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Part 1: DNA to Protein Translation
def translate_dna(dna_sequence):
    """
    Translates a DNA sequence to a protein using a simplified genetic code
    with just 4 amino acids (A, C, L, S).
    """
    # Simplified genetic code with just 4 amino acids
    genetic_code = {
        "AAA": "A", "AAC": "A", # Alanine
        "CCG": "C", "CCC": "C", # Cysteine
        "TTG": "L", "TTA": "L", # Leucine
        "AGT": "S", "AGC": "S", # Serine
        "TAA": "*", "TAG": "*", "TGA": "*" # Stop codons
    }
    
    # Make the sequence uppercase and remove spaces
    dna_sequence = dna_sequence.upper().replace(" ", "")
    
    # Start with an empty protein
    protein_sequence = ""
    
    # Go through the DNA sequence in chunks of 3 (codons)
    for i in range(0, len(dna_sequence), 3):
        # Get a chunk of 3 nucleotides
        codon = dna_sequence[i:i+3]
        
        # Skip if we don't have a full 3-letter codon
        if len(codon) < 3:
            break
        
        # Look up the amino acid for this codon
        amino_acid = genetic_code.get(codon, "X")  # X means "unknown"
        protein_sequence += amino_acid
        
        # Stop if we hit a stop codon (*)
        if amino_acid == "*":
            break
    
    return protein_sequence

# Part 2: Logistic Population Growth Simulation
def simple_logistic_growth(time, initial_pop, max_pop, growth_rate, lag_time):
    """
    Calculates population size at a given time point using a simplified logistic growth model.
    """
    # Adjust growth based on lag time
    if time < lag_time:
        # During lag phase, grow very slowly
        adjusted_time = time * 0.1
    else:
        # After lag phase, grow normally
        adjusted_time = time
    
    # Standard logistic equation
    denominator = 1 + ((max_pop / initial_pop) - 1) * np.exp(-growth_rate * adjusted_time)
    population = max_pop / denominator
    
    return population

def generate_growth_curves(num_curves=100):
    """
    Generates multiple growth curves with different parameters.
    """
    # Create 50 time points from 0 to 20
    times = np.linspace(0, 20, 50)
    
    # Create an empty DataFrame
    df = pd.DataFrame()
    df['Time'] = times
    
    # Generate different growth curves
    for i in range(num_curves):
        # Random parameters for this curve
        initial_pop = random.uniform(1, 10)         # Starting population between 1-10
        max_pop = random.uniform(100, 1000)         # Maximum population between 100-1000
        growth_rate = random.uniform(0.2, 0.8)      # Growth rate between 0.2-0.8
        lag_time = random.uniform(2, 5)             # Lag phase between 2-5 time units
        
        # Calculate population at each time point
        populations = []
        for t in times:
            # Get population at this time point
            pop = simple_logistic_growth(t, initial_pop, max_pop, growth_rate, lag_time)
            # Add some random noise (±5%)
            noise = random.uniform(-0.05, 0.05) * pop
            populations.append(pop + noise)
        
        # Add this curve to the DataFrame
        df[f'Curve_{i+1}'] = populations
    
    return df

# Part 3: Time to Reach 80% of Maximum Growth
def find_80_percent_time(growth_curve):
    """
    Finds when each growth curve reaches 80% of its maximum value.
    """
    # Get the time values
    times = growth_curve['Time'].values
    
    # Dictionary to store results
    results = {}
    
    # Check each curve (skip the Time column)
    for column in growth_curve.columns:
        if column == 'Time':
            continue
        
        # Get the data for this curve
        curve_data = growth_curve[column].values
        
        # Find the maximum value
        max_value = max(curve_data)
        
        # Calculate 80% of maximum
        threshold = 0.8 * max_value
        
        # Find when we cross the threshold
        for i, value in enumerate(curve_data):
            if value >= threshold:
                results[column] = times[i]
                break
    
    return results

# Part 4: Hamming Distance Function
def calculate_hamming_distance(string1, string2):
    """
    Calculates how many characters are different between two strings.
    """
    # Make strings equal length by adding spaces to the shorter one
    if len(string1) < len(string2):
        string1 = string1 + ' ' * (len(string2) - len(string1))
    elif len(string2) < len(string1):
        string2 = string2 + ' ' * (len(string1) - len(string2))
    
    # Count positions where characters are different
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    
    return distance

# Generate a sample DNA sequence with only A, T, G, C
def generate_sample_dna(length=45):
    """Creates a random DNA sequence of specified length."""
    nucleotides = ['A', 'T', 'G', 'C']
    return ''.join(random.choice(nucleotides) for _ in range(length))

# Example usage
def run_simple_example():
    # Part 1: DNA Translation Example
    print("\n===== DNA TRANSLATION =====")
    dna = generate_sample_dna(45)
    protein = translate_dna(dna)
    print(f"DNA sequence: {dna}")
    print(f"Protein: {protein}")
    
    # Part 2: Growth Curves
    print("\n===== POPULATION GROWTH CURVES =====")
    growth_data = generate_growth_curves(num_curves=3)
    print("First few rows of growth data:")
    print(growth_data.head())
    
    # Plot growth curves
    plt.figure(figsize=(10, 5))
    plt.plot(growth_data['Time'], growth_data['Curve_1'], label='Population 1')
    plt.plot(growth_data['Time'], growth_data['Curve_2'], label='Population 2')
    plt.plot(growth_data['Time'], growth_data['Curve_3'], label='Population 3')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.title('Logistic Growth Curves')
    plt.legend()
    plt.grid(True)
    
    # Part 3: Finding 80% threshold time
    print("\n===== TIME TO REACH 80% OF MAXIMUM =====")
    threshold_times = find_80_percent_time(growth_data)
    for curve, time in threshold_times.items():
        print(f"{curve} reaches 80% at time: {time:.2f}")
    
    # Part 4: Hamming Distance
    print("\n===== HAMMING DISTANCE =====")
    username1 = "biodata_user"
    username2 = "data_science"
    distance = calculate_hamming_distance(username1, username2)
    print(f"String 1: {username1}")
    print(f"String 2: {username2}")
    print(f"Hamming distance: {distance}")

if __name__ == "__main__":
    run_simple_example()