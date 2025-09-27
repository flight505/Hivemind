"""
MONTE CARLO SIMULATION - FILE D: STOCK PRICE SIMULATION

Building on Files A-C, we'll simulate stock prices using random walks.
This demonstrates Monte Carlo in financial modeling and risk analysis.
"""

# IMPORT ALL NECESSARY LIBRARIES AT THE TOP
import random
import math
import statistics
from termcolor import colored

# USER-DEFINED VARIABLES (ALL CAPS AS PER REQUIREMENTS)
INITIAL_STOCK_PRICE = 100.0
DAILY_VOLATILITY = 0.02  # 2% daily volatility
DAILY_DRIFT = 0.0005     # Small upward drift (0.05% per day)
SIMULATION_DAYS = 252    # One trading year
NUMBER_OF_SIMULATIONS = 1000

def explain_random_walk_concept():
    """
    Explains the concept of random walks in stock price modeling
    """
    print(colored("\n" + "="*70, "cyan"))
    print(colored("MONTE CARLO SIMULATION - STOCK PRICE MODELING", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))

    print(colored("\nRANDOM WALKS IN FINANCE", "yellow", attrs=["bold"]))
    print("""
Stock prices don't follow predictable patterns, but they do follow
certain statistical properties. The Random Walk model captures this:

1. Each day, stock price can go UP or DOWN by a random amount
2. The probability of going up vs down might be slightly biased
3. The size of the daily change follows a normal distribution
4. Over time, this creates realistic stock price paths

This is the foundation of modern financial modeling!
    """)

def simple_random_walk_simulation():
    """
    Demonstrates a simple random walk stock price simulation
    """
    print(colored("\n" + "="*50, "green"))
    print(colored("SIMPLE RANDOM WALK SIMULATION", "green", attrs=["bold"]))
    print(colored("="*50, "green"))

    print("""
Let's simulate a stock price over 30 days using simple random walk:
- Start price: $100
- Each day: ±$1 change (50% up, 50% down)
    """)

    # Simple random walk
    price = INITIAL_STOCK_PRICE
    prices = [price]

    print(f"Day 0: ${price:.2f}")
    print("-" * 25)

    for day in range(1, 31):
        # Random change: +1 or -1 with equal probability
        change = random.choice([1, -1])
        price += change
        prices.append(price)

        if day <= 10 or day % 10 == 0:  # Show first 10 days and every 10th day
            print(f"Day {day:2d}: ${price:.2f}")

    print(colored(f"\nFinal price after 30 days: ${price:.2f}", "magenta"))
    print(colored(f"Total change: ${price - INITIAL_STOCK_PRICE:.2f}", "magenta"))
    print(f"Price range: ${min(prices):.2f} to ${max(prices):.2f}")

    # Draw the price chart for simple random walk
    draw_stock_chart(prices, "30-Day Simple Random Walk Chart")

def draw_stock_chart(prices, title="Stock Price Chart"):
    """
    Creates a simple ASCII chart of stock prices over time
    """
    if not prices:
        return

    print(colored("\n" + "="*60, "yellow"))
    print(colored(title, "yellow", attrs=["bold"]))
    print(colored("="*60, "yellow"))

    # Chart dimensions
    chart_width = 50
    chart_height = 15

    # Find min and max prices for scaling
    min_price = min(prices)
    max_price = max(prices)
    price_range = max_price - min_price

    # Avoid division by zero
    if price_range == 0:
        price_range = max_price * 0.1

    # Create chart grid
    chart = [[' ' for _ in range(chart_width)] for _ in range(chart_height)]

    # Plot points
    for i, price in enumerate(prices):
        if i >= chart_width:
            break  # Limit to chart width

        # Scale price to chart height
        if price_range > 0:
            y_pos = int((price - min_price) / price_range * (chart_height - 1))
            y_pos = min(y_pos, chart_height - 1)  # Ensure within bounds
        else:
            y_pos = chart_height // 2

        # Mark the point (use different symbols for trend)
        if i > 0:
            prev_price = prices[i-1]
            if price > prev_price:
                chart[chart_height - 1 - y_pos][i] = '▲'  # Up arrow
            elif price < prev_price:
                chart[chart_height - 1 - y_pos][i] = '▼'  # Down arrow
            else:
                chart[chart_height - 1 - y_pos][i] = '─'  # Flat line
        else:
            chart[chart_height - 1 - y_pos][i] = '●'  # Starting point

    # Draw connecting lines
    for i in range(1, min(len(prices), chart_width)):
        y1 = int((prices[i-1] - min_price) / price_range * (chart_height - 1))
        y2 = int((prices[i] - min_price) / price_range * (chart_height - 1))
        y1 = min(y1, chart_height - 1)
        y2 = min(y2, chart_height - 1)

        # Draw line between points
        if abs(y2 - y1) <= 1:
            # Horizontal or diagonal connection
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if chart[chart_height - 1 - y][i-1] == ' ':
                    chart[chart_height - 1 - y][i-1] = '─'

    # Print the chart
    for row in chart:
        print(''.join(row))

    # Print price scale
    print(colored("\nPrice Scale:", "cyan"))
    print(f"High: ${max_price:.2f}")
    print(f"Low:  ${min_price:.2f}")
    print(colored("▲ = Price up  ▼ = Price down  ─ = Flat  ● = Start", "white"))

def demonstrate_gbm_formula():
    """
    Step-by-step demonstration of the GBM formula
    """
    print(colored("\n" + "="*50, "cyan"))
    print(colored("STEP-BY-STEP GBM CALCULATION", "cyan", attrs=["bold"]))
    print(colored("="*50, "cyan"))

    # Parameters
    current_price = 100.0
    mu = 0.08  # 8% annual return
    sigma = 0.20  # 20% annual volatility
    delta_t = 1/252  # One trading day (252 trading days per year)
    Z = 1.5  # Random shock (this would normally be random.gauss(0,1))

    print(f"Current stock price: ${current_price}")
    print(f"Expected annual return (μ): {mu*100}%")
    print(f"Annual volatility (σ): {sigma*100}%")
    print(f"Time period (Δt): {delta_t:.6f} years (1 trading day)")
    print(f"Random shock (Z): {Z} (from N(0,1) distribution)")
    print()

    # Step 1: Calculate drift term
    drift_term = mu * delta_t
    print("STEP 1 - DRIFT TERM:")
    print(f"μ × Δt = {mu} × {delta_t:.6f} = {drift_term:.6f} ({drift_term*100:.3f}%)")
    print("This is the expected upward movement over one day.")
    print()

    # Step 2: Calculate volatility term
    volatility_term = sigma * math.sqrt(delta_t) * Z
    sqrt_dt = math.sqrt(delta_t)
    sigma_sqrt_dt = sigma * sqrt_dt

    print("STEP 2 - VOLATILITY TERM:")
    print(f"√Δt = √{delta_t:.6f} = {sqrt_dt:.6f}")
    print(f"σ × √Δt = {sigma} × {sqrt_dt:.6f} = {sigma_sqrt_dt:.6f}")
    print(f"σ × √Δt × Z = {sigma_sqrt_dt:.6f} × {Z} = {volatility_term:.6f} ({volatility_term*100:.3f}%)")
    print("This is the random price movement (could be + or -).")
    print()

    # Step 3: Total percentage change
    total_change_pct = drift_term + volatility_term
    print("STEP 3 - TOTAL PERCENTAGE CHANGE:")
    print(f"ΔS/S = {drift_term:.6f} + {volatility_term:.6f} = {total_change_pct:.6f} ({total_change_pct*100:.3f}%)")
    print()

    # Step 4: New price calculation
    new_price = current_price * (1 + total_change_pct)
    price_change = new_price - current_price

    print("STEP 4 - NEW PRICE:")
    print(f"New price = ${current_price} × (1 + {total_change_pct:.6f}) = ${new_price:.2f}")
    print(f"Price change = ${price_change:.2f}")
    print()

    print(colored("KEY INSIGHTS:", "yellow", attrs=["bold"]))
    print("• Drift term provides consistent upward pressure")
    print("• Volatility term creates realistic market fluctuations")
    print("• Time scaling (√Δt) prevents extreme volatility over long periods")
    print("• Normal distribution (Z) creates natural price movements")
    print("• Formula works with PERCENTAGES, not dollar amounts")

def geometric_brownian_motion_simulation():
    """
    Demonstrates geometric Brownian motion (more realistic stock model)
    """
    print(colored("\n" + "="*50, "green"))
    print(colored("GEOMETRIC BROWNIAN MOTION", "green", attrs=["bold"]))
    print(colored("="*50, "green"))

    print("""
Geometric Brownian Motion is a more realistic stock price model:
- Percentage changes (not absolute dollar amounts)
- Volatility: how much prices swing daily
- Drift: long-term upward trend
- Multiplicative nature: good for compounding

LET'S BREAK DOWN THE FORMULA: ΔS/S = μΔt + σ√Δt × Z

ΔS/S (left side):
  - ΔS = Change in stock price (S_final - S_initial)
  - S = Current stock price
  - So ΔS/S = Percentage change in price (like +2% or -1.5%)

μΔt (drift term):
  - μ = Expected annual return (e.g., 0.08 for 8% annual return)
  - Δt = Time period (e.g., 1/252 for one trading day)
  - This pushes prices upward over time (the trend)

σ√Δt × Z (volatility/randomness term):
  - σ = Annual volatility (e.g., 0.20 for 20% annual swings)
  - √Δt = Square root of time (makes volatility scale properly)
  - Z = Random shock from normal distribution (N(0,1))
  - This creates realistic up/down price movements

WHY THIS WORKS:
- Prices change by PERCENTAGES (realistic for stocks)
- Time scaling: √Δt prevents unrealistic volatility over long periods
- Normal distribution Z creates natural price movements
- Drift μ creates long-term upward trend
- Volatility σ creates realistic market swings

EXAMPLE:
Stock at $100, μ=8%, σ=20%, Δt=1 day:
- Drift: 8% × (1/252) ≈ +0.032% per day
- Volatility: 20% × √(1/252) × Z ≈ ±0.89% × Z per day
- Total daily change: ±0.032% + random shock
    """)

    # First demonstrate the formula step by step
    demonstrate_gbm_formula()

    # Single GBM simulation
    price = INITIAL_STOCK_PRICE
    prices = [price]

    print(f"Starting price: ${price:.2f}")
    print("Daily changes with volatility and drift...")
    print("-" * 40)

    for day in range(1, 31):
        # Generate random normal variable
        random_shock = random.gauss(0, 1)  # Normal distribution with mean 0, std dev 1

        # Geometric Brownian Motion formula (simplified)
        daily_return = DAILY_DRIFT + DAILY_VOLATILITY * random_shock

        # Update price multiplicatively
        price *= (1 + daily_return)
        prices.append(price)

        if day <= 10 or day % 10 == 0:
            print(f"Day {day:2d}: ${price:.2f} ({((price/INITIAL_STOCK_PRICE - 1) * 100):+.1f}%)")

    print(colored(f"\nFinal price after 30 days: ${price:.2f}", "magenta"))
    print(colored(f"Total return: {((price/INITIAL_STOCK_PRICE - 1) * 100):.1f}%", "magenta"))

    # Draw the price chart
    draw_stock_chart(prices, "30-Day Stock Price Chart")

def multiple_simulation_analysis():
    """
    Runs multiple simulations to analyze probability distributions
    """
    print(colored("\n" + "="*50, "blue"))
    print(colored("MULTIPLE SIMULATIONS ANALYSIS", "blue", attrs=["bold"]))
    print(colored("="*50, "blue"))

    print(f"""
Running {NUMBER_OF_SIMULATIONS} simulations of 1-year stock performance...
This shows the PROBABILITY DISTRIBUTION of possible outcomes.
    """)

    final_prices = []

    # Progress indicator
    print("Progress: ", end="")

    for sim in range(NUMBER_OF_SIMULATIONS):
        if sim % 100 == 0:
            print(f"{sim//100}", end="")

        price = INITIAL_STOCK_PRICE

        # Simulate one year (252 trading days)
        for _ in range(SIMULATION_DAYS):
            # Geometric Brownian Motion
            random_shock = random.gauss(0, 1)
            daily_return = DAILY_DRIFT + DAILY_VOLATILITY * random_shock
            price *= (1 + daily_return)

        final_prices.append(price)

    print(" ✓")

    # Analyze results
    mean_final_price = sum(final_prices) / len(final_prices)
    median_final_price = statistics.median(final_prices)
    min_price = min(final_prices)
    max_price = max(final_prices)
    std_dev = statistics.stdev(final_prices)

    print(colored("\nSimulation Results (after 1 year):", "yellow", attrs=["bold"]))
    print(f"Mean final price: ${mean_final_price:.2f}")
    print(f"Median final price: ${median_final_price:.2f}")
    print(f"Minimum price: ${min_price:.2f}")
    print(f"Maximum price: ${max_price:.2f}")
    print(f"Standard deviation: ${std_dev:.2f}")

    # Show probability ranges
    print(colored("\nProbability Analysis:", "cyan", attrs=["bold"]))
    percentiles = [10, 25, 50, 75, 90]
    for p in percentiles:
        price = statistics.quantiles(final_prices, n=100)[p-1]
        print(f"{p:2d}th percentile: ${price:.2f}")

    # Risk analysis
    print(colored("\nRisk Analysis:", "red", attrs=["bold"]))
    probability_loss = sum(1 for p in final_prices if p < INITIAL_STOCK_PRICE) / len(final_prices) * 100
    probability_double = sum(1 for p in final_prices if p > INITIAL_STOCK_PRICE * 2) / len(final_prices) * 100

    print(f"Probability of loss: {probability_loss:.1f}%")
    print(f"Probability of doubling: {probability_double:.1f}%")

    # Expected return
    expected_return = (mean_final_price / INITIAL_STOCK_PRICE - 1) * 100
    print(f"Expected annual return: {expected_return:.2f}%")

def visualize_price_paths():
    """
    Shows a few example price paths
    """
    print(colored("\n" + "="*50, "magenta"))
    print(colored("EXAMPLE PRICE PATHS", "magenta", attrs=["bold"]))
    print(colored("="*50, "magenta"))

    print("Here are 5 example stock price paths over 1 year:")

    for path_num in range(1, 6):
        price = INITIAL_STOCK_PRICE
        prices = [price]

        for _ in range(SIMULATION_DAYS):
            random_shock = random.gauss(0, 1)
            daily_return = DAILY_DRIFT + DAILY_VOLATILITY * random_shock
            price *= (1 + daily_return)
            prices.append(price)

        # Show start, middle, and end
        start_price = prices[0]
        mid_price = prices[SIMULATION_DAYS // 2]
        end_price = prices[-1]

        print(colored(f"Path {path_num}:", "white", attrs=["bold"]))
        print(f"  Start: ${start_price:.2f}")
        print(f"  Middle: ${mid_price:.2f}")
        print(f"  End: ${end_price:.2f}")

        # Show chart for first path
        if path_num == 1:
            draw_stock_chart(prices, f"Path {path_num} - Full Year Chart")

        if path_num < 5:
            print()

def monte_carlo_option_pricing_intro():
    """
    Introduces the concept of Monte Carlo in option pricing
    """
    print(colored("\n" + "="*50, "yellow"))
    print(colored("MONTE CARLO IN OPTION PRICING", "yellow", attrs=["bold"]))
    print(colored("="*50, "yellow"))

    print("""
The techniques you've learned form the foundation of:

1. **Stock Price Simulation** (what we just did)
2. **Portfolio Risk Analysis** (Value at Risk)
3. **Option Pricing** (Black-Scholes alternative)
4. **Credit Risk Modeling**
5. **Insurance Risk Assessment**

Example: European Call Option Pricing
- Simulate many stock price paths to expiration
- Calculate payoff for each path: max(S - K, 0)
- Average the payoffs and discount to present value
- This gives the option's fair price!

This is how Wall Street uses Monte Carlo every day.
    """)

    # Simple option pricing example
    print(colored("\nSimple Option Pricing Example:", "cyan", attrs=["bold"]))
    strike_price = 105.0
    risk_free_rate = 0.03
    time_to_expiry = 1.0

    # Simulate payoffs
    payoffs = []
    for _ in range(100):
        # Simulate final stock price
        final_price = INITIAL_STOCK_PRICE
        for _ in range(SIMULATION_DAYS):
            random_shock = random.gauss(0, 1)
            daily_return = DAILY_DRIFT + DAILY_VOLATILITY * random_shock
            final_price *= (1 + daily_return)

        # Calculate option payoff
        payoff = max(final_price - strike_price, 0)
        payoffs.append(payoff)

    # Calculate option price
    average_payoff = sum(payoffs) / len(payoffs)
    option_price = average_payoff * math.exp(-risk_free_rate * time_to_expiry)

    print(f"Stock price: ${INITIAL_STOCK_PRICE}")
    print(f"Strike price: ${strike_price}")
    print(f"Average payoff: ${average_payoff:.2f}")
    print(colored(f"Option price: ${option_price:.2f}", "green"))

if __name__ == "__main__":
    explain_random_walk_concept()
    simple_random_walk_simulation()
    geometric_brownian_motion_simulation()
    multiple_simulation_analysis()
    visualize_price_paths()
    monte_carlo_option_pricing_intro()

    print(colored("\n" + "="*70, "cyan"))
    print(colored("FILE D COMPLETE - READY FOR FILE E!", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))
