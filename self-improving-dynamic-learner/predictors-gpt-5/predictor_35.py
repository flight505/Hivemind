"""
Predictor 35
Generated on: 2025-09-09 13:26:35
Accuracy: 58.53%
"""


# PREDICTOR 35 - Accuracy: 58.53%
# Correct predictions: 5853/10000 (58.53%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B

    # Tiny C band
    if C <= 12:
        if E >= 55:
            return 4
        if D >= 80 and E <= 30:
            return 1
        if sumAB >= 165:
            return 1
        return 3

    # Very low C specifics
    if C <= 22 and D >= 90 and E <= 20:
        return 1
    if C <= 20 and E >= 70 and D <= 55:
        return 4
    if C <= 20 and E <= 25 and D >= 30:
        return 3
    if C <= 35 and D <= 20 and E <= 30:
        return 3

    # Low-mid C with tiny D and high E -> 2 (fix specific case)
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2

    # High C with strong B -> 2
    if C >= 95 and B >= 70:
        return 2
    if C >= 90 and B >= 90:
        return 2

    # Prevent false 4 at high C with tiny D and very low E
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # Very high C general
    if C >= 88:
        if E <= 25:
            return 4
        return 1

    # Class 2 patterns
    if C >= 80 and B >= 90 and D >= 80 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75:
        return 2
    if 45 <= C <= 60 and B >= 80 and D >= 50:
        return 2
    if 45 <= C <= 60 and D <= 20 and E >= 90:
        return 2

    # Strong class 4 patterns
    if 60 <= C <= 70 and D <= 20 and E >= 50 and sumAB <= 160:
        return 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4
    if C <= 45 and ed >= 35:
        return 4

    # Low D and low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    return 1