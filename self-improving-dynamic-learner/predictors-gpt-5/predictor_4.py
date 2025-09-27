"""
Predictor 4
Generated on: 2025-09-09 12:09:14
Accuracy: 58.60%
"""


# PREDICTOR 4 - Accuracy: 58.60%
# Correct predictions: 5860/10000 (58.60%)

def predict_output(A, B, C, D, E):
    # Tiny C handling
    if C <= 12:
        if E >= 55:
            return 4
        if A + B >= 170:
            return 1
        return 3

    # Very high C
    if C >= 88:
        if E <= 25:
            return 4
        return 1

    # Special case: very small A with high E tends to 1
    if A <= 10 and E >= 80:
        return 1

    # Low D with low-to-mid C tends to 3, unless strong signals for 1
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    # High D with mid C tends to 3
    if D >= 90 and 50 <= C <= 70:
        return 3

    # Strong patterns for class 2
    if A <= 35 and B >= 65 and C >= 65:
        return 2
    if B >= 90 and 70 <= C <= 85 and D >= 50:
        return 2
    if B >= 90 and D >= 80 and C <= 40 and E >= 90:
        return 2

    # Low C with high E -> 4; low C with low E and high A -> 3
    if C <= 30:
        if E >= 85:
            return 4
        if D <= 20 and E >= 60:
            return 4
        if A >= 80 and E <= 30:
            return 3

    # Moderate D and high E with not-too-high C -> 4
    if D <= 30 and E >= 70 and C < 70:
        return 4

    # Specific small-A small-E mid-C -> 4
    if A <= 15 and E <= 15 and 50 <= C <= 65:
        return 4

    return 1