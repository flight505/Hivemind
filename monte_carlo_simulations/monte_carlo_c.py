"""
MONTE CARLO SIMULATION - FILE C: BASIC STATISTICS & LAW OF LARGE NUMBERS

Building on Files A and B, we'll explore the statistical foundation
of Monte Carlo simulations and the Law of Large Numbers.
"""

# IMPORT ALL NECESSARY LIBRARIES AT THE TOP
import random
import math
import statistics
from termcolor import colored

# USER-DEFINED VARIABLES (ALL CAPS AS PER REQUIREMENTS)
NUMBER_OF_SAMPLES = 1000
DICE_SIDES = 6
COIN_FLIPS = 100

def explain_basic_statistics():
    """
    Explains fundamental statistical concepts used in Monte Carlo
    """
    print(colored("\n" + "="*70, "cyan"))
    print(colored("MONTE CARLO SIMULATION - BASIC STATISTICS", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))

    print(colored("\nWHY STATISTICS MATTER IN MONTE CARLO", "yellow", attrs=["bold"]))
    print("""
Monte Carlo simulation relies on STATISTICS to make sense of random results.

Key concepts we'll explore:
1. Sample Mean (average of our random samples)
2. Variance (how spread out our results are)
3. Standard Deviation (square root of variance)
4. Law of Large Numbers (why more samples = better estimates)

These concepts explain why Monte Carlo methods work and how reliable they are!
    """)

def demonstrate_sample_mean():
    """
    Shows how sample means converge to true means
    """
    print(colored("\n" + "="*50, "green"))
    print(colored("SAMPLE MEAN DEMONSTRATION", "green", attrs=["bold"]))
    print(colored("="*50, "green"))

    print("""
Let's roll dice and see how our average (sample mean) behaves:

For a fair 6-sided die:
- True mean = (1+2+3+4+5+6)/6 = 3.5
- Our sample mean should get closer to 3.5 as we roll more dice
    """)

    # Roll dice and track running averages
    rolls = []
    running_means = []

    print(colored("Rolling dice and tracking the average:", "white"))
    print("Roll# | Roll | Running Average")
    print("-" * 30)

    for i in range(1, NUMBER_OF_SAMPLES + 1):
        roll = random.randint(1, DICE_SIDES)
        rolls.append(roll)

        running_mean = sum(rolls) / len(rolls)
        running_means.append(running_mean)

        if i <= 20 or i % 100 == 0:  # Show first 20 and every 100th roll
            print(f"{i:6d} | {roll:4d} | {running_mean:14.3f}")

    print(colored(f"\nFinal Results after {NUMBER_OF_SAMPLES} rolls:", "magenta"))
    print(f"Sample Mean: {running_mean:.3f}")
    print(f"True Mean: {3.5:.3f}")

def demonstrate_variance():
    """
    Shows how variance measures the spread of our results
    """
    print(colored("\n" + "="*50, "green"))
    print(colored("VARIANCE & STANDARD DEVIATION", "green", attrs=["bold"]))
    print(colored("="*50, "green"))

    print("""
Variance measures how spread out our results are from the mean.
Standard deviation is the square root of variance.

High variance = results are spread out (unreliable)
Low variance = results are clustered around the mean (reliable)

Let's see this in action with coin flips:
    """)

    # Simulate coin flips
    flips = []
    for _ in range(COIN_FLIPS):
        flip = random.choice(['H', 'T'])
        flips.append(1 if flip == 'H' else 0)  # 1 for heads, 0 for tails

    # Calculate statistics
    mean_heads = sum(flips) / len(flips)
    variance = sum((x - mean_heads) ** 2 for x in flips) / len(flips)
    std_dev = math.sqrt(variance)

    print(f"Coin flips: {flips[:20]}{'...' if len(flips) > 20 else ''}")
    print(f"Mean (fraction of heads): {mean_heads:.3f}")
    print(f"Variance: {variance:.4f}")
    print(f"Standard Deviation: {std_dev:.4f}")

    # Show distribution
    heads_count = sum(flips)
    tails_count = len(flips) - heads_count

    print(colored(f"\nDistribution: {heads_count} heads, {tails_count} tails", "cyan"))
    print("Expected: ~50 heads, ~50 tails (for a fair coin)")

    print(colored("\nIMPORTANT NOTE:", "yellow", attrs=["bold"]))
    print("For a fair coin (p=0.5):")
    print("- Variance = p(1-p) = 0.5 × 0.5 = 0.25")
    print("- Standard Deviation = √variance = √0.25 = 0.5")
    print("- This is CORRECT! (not 0.05)")
    print("- SD of 0.5 means results vary by about ±0.5 from the mean")
    print("- This reflects the natural randomness of coin flips!")

def law_of_large_numbers_demo():
    """
    Demonstrates the Law of Large Numbers
    """
    print(colored("\n" + "="*50, "red"))
    print(colored("THE LAW OF LARGE NUMBERS", "red", attrs=["bold"]))
    print(colored("="*50, "red"))

    print("""
The Law of Large Numbers states:
"As the number of trials increases, the sample mean approaches the true mean."

This is why Monte Carlo simulations become more accurate with more samples!

Let's demonstrate with dice rolls:
    """)

    true_mean = (1 + 2 + 3 + 4 + 5 + 6) / 6  # 3.5
    sample_sizes = [10, 50, 100, 500, 1000, 5000]

    print("Sample Size | Sample Mean | Error | Accuracy")
    print("-" * 45)

    for size in sample_sizes:
        # Generate sample
        rolls = [random.randint(1, 6) for _ in range(size)]
        sample_mean = sum(rolls) / size
        error = abs(sample_mean - true_mean)
        accuracy = (1 - error/true_mean) * 100

        print(f"{size:11d} | {sample_mean:11.3f} | {error:5.3f} | {accuracy:8.1f}%")

    print(colored("\nNotice how the error decreases as sample size increases!", "yellow", attrs=["bold"]))

def monte_carlo_reliability_demo():
    """
    Shows how Monte Carlo estimates become more reliable with more samples
    """
    print(colored("\n" + "="*50, "red"))
    print(colored("MONTE CARLO RELIABILITY", "red", attrs=["bold"]))
    print(colored("="*50, "red"))

    print("""
Let's estimate π multiple times with different sample sizes to see
how reliability improves with more random points.
    """)

    def estimate_pi(samples):
        """Estimate π using Monte Carlo with given number of samples"""
        inside_circle = 0
        for _ in range(samples):
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                inside_circle += 1
        return 4 * (inside_circle / samples)

    # Test different sample sizes
    test_sizes = [100, 500, 1000, 5000, 10000]
    results = {}

    print("Testing π estimation with different sample sizes:")
    print("Samples | Estimate | Error | Standard Dev")
    print("-" * 45)

    for size in test_sizes:
        # Run multiple estimates for each sample size
        estimates = [estimate_pi(size) for _ in range(10)]

        mean_estimate = sum(estimates) / len(estimates)
        errors = [abs(est - math.pi) for est in estimates]
        mean_error = sum(errors) / len(errors)
        std_dev = statistics.stdev(estimates)

        results[size] = {
            'mean': mean_estimate,
            'error': mean_error,
            'std_dev': std_dev
        }

        print(f"{size:7d} | {mean_estimate:8.4f} | {mean_error:5.4f} | {std_dev:11.4f}")

    print(colored("\nKey Insights:", "yellow", attrs=["bold"]))
    print("1. More samples = smaller error (better accuracy)")
    print("2. More samples = smaller standard deviation (more consistent)")
    print("3. This is the Law of Large Numbers in action!")

def statistical_confidence_concept():
    """
    Introduces the concept of statistical confidence
    """
    print(colored("\n" + "="*50, "blue"))
    print(colored("STATISTICAL CONFIDENCE", "blue", attrs=["bold"]))
    print(colored("="*50, "blue"))

    print("""
Statistical confidence tells us how sure we can be about our results.

Example: If we estimate π as 3.14159 ± 0.01, we can be 95% confident
that the true value of π lies between 3.13159 and 3.15159.

This concept becomes crucial in advanced Monte Carlo applications.
    """)

    # Simple confidence interval demonstration
    estimates = [4 * sum(1 for _ in range(1000) if random.random()**2 + random.random()**2 <= 1) / 1000
                 for _ in range(20)]

    mean_estimate = sum(estimates) / len(estimates)
    std_dev = statistics.stdev(estimates)
    confidence_interval = 1.96 * std_dev / math.sqrt(len(estimates))  # 95% CI

    print(f"Mean estimate: {mean_estimate:.4f}")
    print(f"Standard deviation: {std_dev:.4f}")
    print(f"Confidence interval: ±{confidence_interval:.4f}")
    print(f"95% confidence range: {mean_estimate - confidence_interval:.4f} to {mean_estimate + confidence_interval:.4f}")
    print(f"Actual π: {math.pi:.4f}")
    print(colored("\nThis gives us confidence in our Monte Carlo results!", "green"))

if __name__ == "__main__":
    explain_basic_statistics()
    demonstrate_sample_mean()
    demonstrate_variance()
    law_of_large_numbers_demo()
    monte_carlo_reliability_demo()
    statistical_confidence_concept()

    print(colored("\n" + "="*70, "cyan"))
    print(colored("FILE C COMPLETE - READY FOR FILE D!", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))
