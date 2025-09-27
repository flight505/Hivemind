import csv
import random
import os
from termcolor import colored

# CONFIGURATION VARIABLES
NUM_ROWS = 10000
OUTPUT_FILE = 'complex_dataset.csv'
RANDOM_SEED = 42

def calculate_complex_output(A, B, C, D, E):
    """
    Complex formula that requires all 5 inputs to determine output.
    No shortcuts exist - all variables must be considered together.
    """

    # Intermediate calculations involving multiple variables
    sum_first_pair = A + B
    product_middle = C * D
    modulo_last = E % 10
    weighted_sum = A * 0.3 + B * 0.2 + C * 0.15 + D * 0.15 + E * 0.2

    # First level: Check sum of first two variables
    if sum_first_pair > 100:
        # Second level: Check product of middle two
        if product_middle > 2000:
            # Third level: Check modulo and weighted conditions
            if modulo_last >= 5 and weighted_sum > 60:
                return 1
            elif A > B and C > D:
                return 2
            elif modulo_last < 3:
                return 3
            else:
                return 4
        else:
            # Alternative path when product is smaller
            if C + D > 150 and E > 50:
                return 4
            elif sum_first_pair + modulo_last > 120:
                return 1
            else:
                return 2
    else:
        # Different logic when first sum is smaller
        if product_middle < 1000:
            if modulo_last < 4 and weighted_sum < 40:
                return 3
            elif B > C and D > E:
                return 4
            else:
                return 2
        else:
            if weighted_sum > 55 and modulo_last >= 6:
                return 1
            elif A + E > 80:
                return 4
            else:
                return 3

def generate_dataset():
    """Generate the complex CSV dataset"""

    random.seed(RANDOM_SEED)

    print(colored(f"Generating {NUM_ROWS} rows of complex dataset...", "blue"))

    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(['A', 'B', 'C', 'D', 'E', 'Output'])

        # Generate data rows
        for i in range(NUM_ROWS):
            # Generate 5 random integers from 1 to 100
            A = random.randint(1, 100)
            B = random.randint(1, 100)
            C = random.randint(1, 100)
            D = random.randint(1, 100)
            E = random.randint(1, 100)

            # Calculate output using complex formula
            output = calculate_complex_output(A, B, C, D, E)

            # Write row
            writer.writerow([A, B, C, D, E, output])

            # Progress indicator
            if (i + 1) % 1000 == 0:
                print(colored(f"Generated {i + 1}/{NUM_ROWS} rows...", "green"))

    print(colored(f"Dataset generated successfully! File: {OUTPUT_FILE}", "green"))
    print(colored(f"File size: {os.path.getsize(OUTPUT_FILE)} bytes", "yellow"))

if __name__ == "__main__":
    generate_dataset()
