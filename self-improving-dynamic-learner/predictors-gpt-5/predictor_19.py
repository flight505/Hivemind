"""
Predictor 19
Generated on: 2025-09-09 12:48:25
Accuracy: 52.99%
"""


# PREDICTOR 19 - Accuracy: 52.99%
# Correct predictions: 5299/10000 (52.99%)

def predict_output(A, B, C, D, E):
    # Tiny C special cases
    if C <= 5:
        if E <= 10:
            return 1  # very low E -> 1
        if B >= 80 and E <= 60 and D >= 40:
            return 1  # strong B with moderate D and not-high E -> 1
        if C <= 2 and E >= 60:
            return 4  # ultra-tiny C with high E -> 4
        if E >= 80:
            return 4  # tiny C with very high E -> 4
    # Very low C default
    if C <= 12:
        return 3

    # Low C band (13-30)
    if C <= 30:
        if E >= 70 and D <= 30:
            return 4
        if 13 <= C <= 22 and E >= 70:
            return 4
        return 1

    # Low-mid region quick decisions
    if C < 50:
        if D <= 20 and E <= 20:
            return 3
        if D <= 30 and E >= 70:
            return 4

    # Class 3 patterns
    if 35 <= C <= 45 and D >= 70 and E <= 85:
        return 3
    if 50 <= C <= 60 and D >= 85:
        return 3
    if 45 <= C <= 50 and E >= 70 and D >= 40:
        return 3

    # Class 4 patterns
    if 40 <= C <= 55 and E >= 80 and D <= 50:
        return 4
    if 60 <= C <= 65 and D <= 35 and E <= 10:
        return 4
    if 65 <= C < 78 and E <= 40 and D <= 25:
        return 4
    if 70 <= C <= 78 and D <= 30 and E <= 50:
        return 4

    # Class 2 patterns
    if C >= 78 and (B >= 65 or D <= 10):
        return 2
    if B >= 95 and 45 <= C <= 65 and (D >= 50 or E <= 30):
        return 2
    if 50 <= C <= 60 and D <= 10 and E >= 80:
        return 2

    # Override: very high C with ultra-low D and high E -> 1
    if C >= 88 and D <= 5 and E >= 70:
        return 1

    # General tendencies
    if C >= 65:
        return 1
    if 50 <= C <= 64:
        return 1

    return 1