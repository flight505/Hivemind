"""
Predictor 2
Generated on: 2025-09-09 03:33:09
Accuracy: 41.15%
"""


# PREDICTOR 2 - Accuracy: 41.15%
# Correct predictions: 4115/10000 (41.15%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor for the four output classes.
    Uses only basic arithmetic comparisons and logical ordering.
    """
    # 1. Category 3 – low B values
    if B <= 15:
        return 3

    # 2. Very low E – exceptional case for class 4
    if E < 5:
        return 4

    # 3. High B with low C → mostly class 4 (unless E is very high)
    if B > 80 and C < 30:
        return 4 if E < 95 else 2

    # 4. High A together with low C → class 4
    if A > 80 and C < 30:
        return 4

    # 5. High D, low C and moderate E → class 4
    if D > 80 and C < 30 and E < 95:
        return 4

    # 6. Moderate B with high D and low E → class 3
    if 50 <= B <= 80 and D > 80 and E < 40:
        return 3

    # 7. High B (but not captured above) → class 2
    if B > 70:
        return 2

    # 8. Default fallback
    return 1