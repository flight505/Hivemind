"""
Predictor 13
Generated on: 2025-09-09 12:34:55
Accuracy: 55.35%
"""


# PREDICTOR 13 - Accuracy: 55.35%
# Correct predictions: 5535/10000 (55.35%)

def predict_output(A, B, C, D, E):
    # Specific override: very low D with very high E at high C -> 1 (fixes a known miscase)
    if C >= 70 and D <= 5 and E >= 85:
        return 1

    # Very low C handling
    if C <= 12:
        if E >= 70:
            return 4
        return 3
    if C <= 15:
        return 3

    # Strong class 4 signals
    if D <= 10 and E >= 55 and C < 70:
        return 4
    if D <= 30 and E >= 90 and C <= 85:
        return 4
    if C <= 40 and E >= 70 and B >= 90:
        return 4
    if 55 <= C <= 65 and D <= 20 and E <= 30:
        return 4
    if 24 <= C <= 30 and E <= 15 and 40 <= D <= 70:
        return 4

    # Class 3 signals
    if C >= 80 and D >= 95 and E <= 60:
        return 3
    if 30 <= C <= 40 and D >= 60 and E >= 85:
        return 3

    # Class 2 signals
    if C >= 95 and B >= 70:
        return 2
    if C >= 72 and D <= 15 and E >= 70:
        return 2
    if C >= 78 and B >= 70:
        return 2

    # General high C tends to 1
    if C >= 65:
        return 1

    # Default
    return 1