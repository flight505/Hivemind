"""
Predictor 37
Generated on: 2025-09-09 13:32:30
Accuracy: 57.53%
"""


# PREDICTOR 37 - Accuracy: 57.53%
# Correct predictions: 5753/10000 (57.53%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B

    # Tiny C band (C <= 12)
    if C <= 12:
        # Tiny C with high E and modest D and decent B -> 2
        if E >= 70 and 15 <= D <= 30 and B >= 45:
            return 2
        if E >= 55:
            return 4
        if D >= 80 and E <= 30:
            return 1
        if sumAB >= 165:
            return 1
        return 3

    # Very low C region
    if C <= 25:
        if E >= 85:
            return 4
        if C <= 22 and D >= 90 and E <= 20:
            return 1
        if C <= 20 and E >= 70:
            return 4
        if C <= 35 and D <= 20 and E <= 30:
            return 3

    # Mid-low C: low E with low D -> 3
    if 40 <= C <= 50 and D <= 25 and E <= 30:
        return 3

    # Mid-low C: moderate E dominating D with modest D -> 4
    if 40 <= C <= 50 and D <= 40 and E >= 35 and E >= D:
        return 4

    # Mid C with high D -> 3
    if 50 <= C <= 70 and D >= 75 and E >= 40:
        return 3

    # High C with very low D and low E -> 3
    if C >= 70 and D <= 12 and E <= 40:
        return 3

    # Class 2 patterns
    if C >= 75 and D <= 10 and E >= 60:
        return 2
    if C >= 80 and B >= 90 and D >= 70 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75 and E >= 60:
        return 2
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2

    # Very high C with very low E -> 1
    if C >= 88 and E <= 25:
        return 1

    # Mid C with low D and moderate E -> 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4

    # Low D and low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    return 1