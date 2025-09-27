"""
Predictor 25
Generated on: 2025-09-09 12:57:53
Accuracy: 58.35%
"""


# PREDICTOR 25 - Accuracy: 58.35%
# Correct predictions: 5835/10000 (58.35%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C handling
    if C <= 12:
        if E >= 55 and D >= 40:
            return 4
        if (A + B) >= 165:
            return 1
        return 3

    # Very low C near 20: specific outcomes
    if C <= 22 and D >= 90 and E <= 20:
        return 1
    if C <= 25 and D >= 70 and E <= 5:
        return 4
    if C <= 20 and E >= 70 and D <= 55:
        return 4
    if C <= 20 and E <= 20 and D >= 30:
        return 3

    # Strong class 4 signatures
    if C >= 88 and E <= 25:
        return 4
    if C >= 80 and E <= 20:
        return 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4
    if C <= 45 and ed >= 35:
        return 4
    if 35 <= C <= 40 and 30 <= D <= 40 and 25 <= E <= 40:
        return 4
    if C <= 32 and B >= 95 and D >= 50:
        return 4

    # Prevent false class 2 when E is very low at high C with tiny D
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # Class 2 patterns
    if C >= 75 and D <= 10 and E >= 60:
        return 2
    if 70 <= C <= 75 and D <= 15 and E >= 80:
        return 2
    if C >= 80 and B >= 90 and D >= 80:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75:
        return 2
    if 45 <= C <= 60 and B >= 80 and D >= 50:
        return 2
    if 45 <= C <= 60 and D <= 20 and E >= 90:
        return 2
    if 30 <= C <= 40 and B >= 90 and D >= 60:
        return 2

    # Special class 3 pattern at high C with very low D and E
    if C >= 70 and D <= 10 and E <= 10:
        return 3

    return 1