"""
Predictor 14
Generated on: 2025-09-09 12:37:35
Accuracy: 51.28%
"""


# PREDICTOR 14 - Accuracy: 51.28%
# Correct predictions: 5128/10000 (51.28%)

def predict_output(A, B, C, D, E):
    # Specific override to avoid misrouting some high-C, very-low-D, very-high-E cases
    if C >= 70 and D <= 5 and E >= 85:
        return 1

    # Very small C
    if C <= 12:
        if E >= 70:
            return 4
        return 3

    # Low C band
    if C <= 25:
        if E >= 85 and D <= 40:
            return 4
        return 1

    # Strong class 4 signals
    if D <= 10 and E >= 55 and C < 70:
        return 4
    if 55 <= C <= 65 and D <= 20 and E <= 30:
        return 4
    if C >= 78 and E <= 10:
        return 4
    if C >= 88 and E <= 25 and D <= 80:
        return 4
    if 45 <= C <= 60 and E >= 70 and D <= 40:
        return 4
    if 30 <= C <= 40 and B >= 90 and 40 <= D <= 60:
        return 4

    # Class 2 patterns
    if C >= 95 and B >= 70 and E > 25:
        return 2
    if C >= 78 and (B >= 65 or D <= 10 or E >= 70):
        return 2
    if C <= 40 and D <= 30 and E >= 90 and B >= 40:
        return 2
    if 35 <= C <= 40 and B >= 65 and E >= 70 and D <= 20:
        return 2
    if B >= 95 and 60 <= C <= 70 and E <= 30:
        return 2

    # Default
    return 1