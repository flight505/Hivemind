"""
MONTE CARLO SIMULATION - FILE A: THE BASICS

This is the first file in our Monte Carlo learning journey.
We'll start with the absolute fundamentals.
"""

# IMPORT ALL NECESSARY LIBRARIES AT THE TOP
import random
from termcolor import colored

# USER-DEFINED VARIABLES (ALL CAPS AS PER REQUIREMENTS)
NUMBER_OF_SAMPLES = 10
MIN_RANDOM_VALUE = 1
MAX_RANDOM_VALUE = 6

def explain_monte_carlo_basics():
    """
    Explains what Monte Carlo simulation is in simple terms
    """
    print(colored("\n" + "="*60, "cyan"))
    print(colored("MONTE CARLO SIMULATION - THE BASICS", "cyan", attrs=["bold"]))
    print(colored("="*60, "cyan"))

    print(colored("\nWHAT IS MONTE CARLO SIMULATION?", "yellow", attrs=["bold"]))
    print("""
Monte Carlo simulation is a method that uses RANDOM SAMPLING
to solve problems or understand uncertainty.

The basic idea:
1. We have a problem that's difficult to solve directly
2. We use random numbers to simulate many possible outcomes
3. We analyze the results to understand what's likely to happen

Think of it like this: Instead of trying to predict the exact path
of a single raindrop, we watch thousands of raindrops and see
the overall pattern they create.
    """)

def demonstrate_random_sampling():
    """
    Shows the most basic form of random sampling
    """
    print(colored("\nRANDOM SAMPLING DEMONSTRATION", "green", attrs=["bold"]))
    print("Let's generate some random numbers and see what happens...")

    # Generate a list of random numbers
    random_samples = []
    for i in range(NUMBER_OF_SAMPLES):
        # Generate a random number between MIN and MAX
        sample = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
        random_samples.append(sample)

    print(f"\nGenerated {NUMBER_OF_SAMPLES} random samples between {MIN_RANDOM_VALUE} and {MAX_RANDOM_VALUE}")
    print(f"First 10 samples: {random_samples[:10]}")

    # Calculate basic statistics
    average = sum(random_samples) / len(random_samples)
    print(colored(f"\nAverage of all samples: {average:.2f}", "magenta"))

    # Count how many times each number appeared
    counts = {}
    for num in range(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE + 1):
        counts[num] = random_samples.count(num)

    print(colored("\nHow many times each number appeared:", "magenta"))
    for num, count in counts.items():
        percentage = (count / NUMBER_OF_SAMPLES) * 100
        print(f"Number {num}: {count} times ({percentage:.1f}%)")

def simulate_fair_dice():
    """
    Simulates rolling a fair six-sided die many times
    """
    print(colored("\n" + "="*60, "cyan"))
    print(colored("SIMULATING A FAIR DICE", "cyan", attrs=["bold"]))
    print(colored("="*60, "cyan"))

    print("""
For a FAIR six-sided die, each number (1-6) should appear
roughly the same number of times when rolled many times.

This is a perfect example of Monte Carlo simulation:
- We can't predict exactly what the next roll will be
- But we can simulate many rolls to see the overall pattern
- The more rolls we do, the closer we get to the expected 16.67% each
    """)

    # Run the dice simulation
    demonstrate_random_sampling()

    print(colored("\nKEY INSIGHT:", "red", attrs=["bold"]))
    print("""
The more samples we take, the more reliable our results become.
This is the foundation of all Monte Carlo simulations!
    """)

if __name__ == "__main__":
    explain_monte_carlo_basics()
    simulate_fair_dice()

    print(colored("\n" + "="*60, "cyan"))
    print(colored("FILE A COMPLETE - READY FOR FILE B!", "cyan", attrs=["bold"]))
    print(colored("="*60, "cyan"))
