"""
Predictor 34
Generated on: 2025-09-09 13:23:38
Accuracy: 58.30%
"""


# PREDICTOR 34 - Accuracy: 58.30%
# Correct predictions: 5830/10000 (58.30%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B

    # Tiny C band
    if C <= 12:
        if E >= 55 and D >= 40:
            return 4
        if sumAB >= 165:
            return 1
        return 3

    # Very low C specifics
    if C <= 22 and D >= 90 and E <= 20:
        return 1
    if C <= 25 and ed >= 35:
        return 4
    if C <= 20 and E >= 70 and D <= 55:
        return 4
    if C <= 35 and D <= 20 and E <= 30:
        return 3

    # Very high C: low E -> 4, else -> 1
    if C >= 88:
        if E <= 25:
            return 4
        return 1

    # Strong class 4 patterns
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4
    if C <= 45 and ed >= 35:
        return 4

    # Prevent false class 2 when E is very low at high C with tiny D
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # Class 2 patterns
    if C >= 75 and D <= 10 and E >= 60:
        return 2
    if C >= 80 and B >= 90 and D >= 80:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75:
        return 2
    if 45 <= C <= 60 and B >= 80 and D >= 50:
        return 2
    if 45 <= C <= 60 and D <= 20 and E >= 90:
        return 2

    # Default
    return 1