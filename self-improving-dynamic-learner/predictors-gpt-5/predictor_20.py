"""
Predictor 20
Generated on: 2025-09-09 12:50:19
Accuracy: 41.04%
"""


# PREDICTOR 20 - Accuracy: 41.04%
# Correct predictions: 4104/10000 (41.04%)

def predict_output(A, B, C, D, E):
    # Targeted overrides from observed patterns
    if C >= 95 and D <= 40 and E <= 50:
        return 4
    if C >= 88 and D >= 80 and E <= 70:
        return 3
    if C >= 80 and D <= 10 and E >= 90:
        return 4
    if C >= 80 and D <= 10 and E <= 30:
        return 1
    if 50 <= C <= 60 and B >= 75 and E <= 30:
        return 2
    if 45 <= C <= 60 and D >= 85:
        return 3
    if C <= 50 and D <= 10 and E <= 20:
        return 1
    if C <= 30 and D <= 5 and E <= 25:
        return 3
    if C <= 30 and D >= 90 and E >= 60:
        return 3
    if 30 <= C <= 40 and D >= 70:
        return 1

    # Core rules learned from the sample
    if C <= 12:
        return 3

    if 13 <= C <= 22:
        if E >= 80:
            return 4
        if D >= 85:
            return 1
        return 1

    if C >= 78:
        return 2

    if 65 <= C < 78:
        return 1

    if 50 <= C <= 64:
        return 1

    return 1