"""
MONTE CARLO SIMULATION - FILE B: ESTIMATING π WITH RANDOM POINTS

Building on File A, we'll now use Monte Carlo simulation to estimate π.
This demonstrates geometric probability and the power of random sampling.
"""

# IMPORT ALL NECESSARY LIBRARIES AT THE TOP
import random
import math
from termcolor import colored

# USER-DEFINED VARIABLES (ALL CAPS AS PER REQUIREMENTS)
NUMBER_OF_POINTS = 1000
SQUARE_SIZE = 1.0

def explain_pi_estimation_concept():
    """
    Explains how we can estimate π using random points
    """
    print(colored("\n" + "="*70, "cyan"))
    print(colored("MONTE CARLO SIMULATION - ESTIMATING π", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))

    print(colored("\nTHE DARTBOARD METHOD", "yellow", attrs=["bold"]))
    print("""
Imagine throwing darts at a square target that has a quarter circle
drawn inside it. Here's the brilliant idea:

1. Draw a square (1x1 units)
2. Draw a quarter circle with radius 1 inside the square
3. Randomly throw darts (points) at the square
4. Count how many land inside the quarter circle
5. Use this formula: π/4 = (points_inside_circle) / total_points
6. So: π ≈ 4 × (points_inside_circle / total_points)

Why does this work?
- Area of square = 1 × 1 = 1
- Area of quarter circle = π × r² / 4 = π × 1² / 4 = π/4
- Ratio of areas = (π/4) / 1 = π/4
- This ratio equals the probability that a random point lands in the circle!
    """)

    # Show the empty dartboard
    print(colored("\nHere's what our dartboard looks like:", "green", attrs=["bold"]))
    draw_dartboard_visualization(points_list=None, show_points=False)

def draw_dartboard_visualization(points_list=None, show_points=True):
    """
    Creates a terminal visualization of the quarter circle inside the square
    """
    # Grid size for visualization (make it wider to appear square since chars are taller than wide)
    GRID_HEIGHT = 15
    GRID_WIDTH = 35  # Wider to compensate for character aspect ratio

    print(colored("\n" + "="*60, "yellow"))
    print(colored("VISUALIZATION: QUARTER CIRCLE INSIDE SQUARE", "yellow", attrs=["bold"]))
    print(colored("="*60, "yellow"))

    # Create the grid
    grid = [[' ' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    # Draw the square border
    for i in range(GRID_WIDTH):
        grid[0][i] = '─'  # Top border
        grid[GRID_HEIGHT-1][i] = '─'  # Bottom border

    for i in range(GRID_HEIGHT):
        grid[i][0] = '│'  # Left border
        grid[i][GRID_WIDTH-1] = '│'  # Right border

    # Draw corners
    grid[0][0] = '┌'
    grid[0][GRID_WIDTH-1] = '┐'
    grid[GRID_HEIGHT-1][0] = '└'
    grid[GRID_HEIGHT-1][GRID_WIDTH-1] = '┘'

    # Draw the quarter circle (approximated with characters)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Calculate actual coordinates (0 to 1)
            actual_x = x / (GRID_WIDTH - 1)
            actual_y = (GRID_HEIGHT - 1 - y) / (GRID_HEIGHT - 1)  # Flip Y axis

            # Check if point is inside quarter circle
            distance = math.sqrt(actual_x**2 + actual_y**2)
            if distance <= 1.0 and actual_x >= 0 and actual_y >= 0:
                if grid[y][x] == ' ':  # Don't overwrite borders
                    grid[y][x] = '·'  # Quarter circle area

    # Mark some random points if provided
    if show_points and points_list:
        for i, (x, y, is_inside) in enumerate(points_list[:20]):  # Show first 20 points
            grid_x = int(x * (GRID_WIDTH - 1))
            grid_y = int((1 - y) * (GRID_HEIGHT - 1))  # Flip Y for display

            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                if grid[grid_y][grid_x] == ' ' or grid[grid_y][grid_x] == '·':
                    grid[grid_y][grid_x] = '●' if is_inside else '○'

    # Print the grid
    for row in grid:
        print(''.join(row))

    print(colored("\nLegend:", "cyan"))
    print("● = Point inside quarter circle (counts toward π)")
    print("○ = Point outside quarter circle")
    print("· = Quarter circle area")
    print("─│┌┐└┘ = Square border")

def create_simple_visualization(points_inside, points_outside, current_estimate):
    """
    Creates a simple text-based visualization of the dartboard
    """
    print(colored("\n" + "-"*50, "blue"))
    print(colored("CURRENT SIMULATION STATE", "blue", attrs=["bold"]))
    print(colored("-"*50, "blue"))

    total_points = points_inside + points_outside
    print(f"Total points thrown: {total_points}")
    print(f"Points inside quarter circle: {points_inside}")
    print(f"Points outside quarter circle: {points_outside}")
    print(colored(f"Current π estimate: {current_estimate:.6f}", "green"))
    print(colored(f"Actual π: {math.pi:.6f}", "magenta"))
    print(colored(f"Difference: {abs(current_estimate - math.pi):.6f}", "red"))

def simulate_pi_estimation():
    """
    Simulates throwing random points to estimate π
    """
    print(colored("\nTHROWING RANDOM POINTS...", "green", attrs=["bold"]))
    print("Each point represents a random dart thrown at our square target.\n")

    # Show empty dartboard first
    draw_dartboard_visualization(points_list=None, show_points=False)

    points_inside_circle = 0
    points_outside_circle = 0
    all_points = []  # Store all points for visualization

    # Show progress at different intervals
    checkpoints = [10, 50, 100, 500, NUMBER_OF_POINTS]

    for i in range(1, NUMBER_OF_POINTS + 1):
        # Generate random point in square (0,0) to (1,1)
        x = random.random() * SQUARE_SIZE
        y = random.random() * SQUARE_SIZE

        # Check if point is inside quarter circle
        # Distance from origin squared: x² + y²
        distance_squared = x*x + y*y

        # If distance ≤ 1, point is inside quarter circle
        is_inside = distance_squared <= SQUARE_SIZE
        if is_inside:
            points_inside_circle += 1
        else:
            points_outside_circle += 1

        # Store point for visualization
        all_points.append((x, y, is_inside))

        # Show progress at checkpoints
        if i in checkpoints:
            current_estimate = 4 * (points_inside_circle / i)
            print(colored(f"\nAfter {i} points:", "yellow", attrs=["bold"]))
            draw_dartboard_visualization(points_list=all_points, show_points=True)
            create_simple_visualization(points_inside_circle, points_outside_circle, current_estimate)

    print(colored("\n" + "="*50, "cyan"))
    print(colored("FINAL RESULTS", "cyan", attrs=["bold"]))
    print(colored("="*50, "cyan"))

    final_estimate = 4 * (points_inside_circle / NUMBER_OF_POINTS)
    accuracy = abs(final_estimate - math.pi) / math.pi * 100

    print(f"Total points thrown: {NUMBER_OF_POINTS}")
    print(f"Points inside quarter circle: {points_inside_circle}")
    print(f"Points outside quarter circle: {points_outside_circle}")
    print(colored(f"\nFinal π estimate: {final_estimate:.6f}", "green"))
    print(colored(f"Actual π value: {math.pi:.6f}", "magenta"))
    print(colored(f"Accuracy: {100 - accuracy:.2f}%", "blue"))

def demonstrate_convergence():
    """
    Shows how the estimate improves with more points
    """
    print(colored("\n" + "="*50, "cyan"))
    print(colored("CONVERGENCE DEMONSTRATION", "cyan", attrs=["bold"]))
    print(colored("="*50, "cyan"))

    print("""
Watch how our π estimate gets closer to the actual value as we use
more and more random points. This demonstrates the Law of Large Numbers!
    """)

    test_sizes = [10, 100, 1000, 10000]

    for size in test_sizes:
        points_inside = 0
        for _ in range(size):
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                points_inside += 1

        estimate = 4 * (points_inside / size)
        error = abs(estimate - math.pi)

        print(colored(f"Points: {size:5d} | π estimate: {estimate:.6f} | Error: {error:.6f}", "white"))

    print(colored("\nNotice how the error decreases as we use more points!", "yellow", attrs=["bold"]))

if __name__ == "__main__":
    explain_pi_estimation_concept()
    simulate_pi_estimation()
    demonstrate_convergence()

    print(colored("\n" + "="*70, "cyan"))
    print(colored("FILE B COMPLETE - READY FOR FILE C!", "cyan", attrs=["bold"]))
    print(colored("="*70, "cyan"))
