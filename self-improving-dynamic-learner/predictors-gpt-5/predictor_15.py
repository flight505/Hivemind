"""
Predictor 15
Generated on: 2025-09-09 12:40:12
Accuracy: 52.27%
"""


# PREDICTOR 15 - Accuracy: 52.27%
# Correct predictions: 5227/10000 (52.27%)

def predict_output(A, B, C, D, E):
    # Specific exception: tiny C but extreme B/D/E -> 1
    if C <= 5 and B >= 90 and D >= 80 and E <= 20:
        return 1

    # Override: high C with ultra-low D and very high E -> 1
    if C >= 70 and D <= 5 and E >= 85:
        return 1

    # Very small C -> mostly 3 in sample
    if C <= 12:
        return 3
    if C <= 15:
        return 3

    # Low C band (13-25)
    if C <= 25:
        if E >= 85 and D <= 30:
            return 4
        return 1

    # Strong class 4 patterns
    if C <= 28 and E <= 20 and D >= 50:
        return 4
    if D <= 10 and E >= 55 and C < 70:
        return 4
    if 45 <= C <= 60 and D <= 40 and E >= 70:
        return 4
    if 30 <= C <= 40 and B >= 90 and 40 <= D <= 60:
        return 4
    if C >= 94 and D <= 30 and E <= 40:
        return 4
    if C >= 80 and E <= 10:
        return 4
    if C >= 85 and D <= 20 and E >= 90:
        return 4

    # Class 3 patterns
    if 50 <= C <= 60 and D <= 20 and 15 <= E <= 35:
        return 3
    if D >= 95 and C >= 80:
        return 3

    # Class 2 patterns
    if 70 <= C < 75 and D <= 15 and E >= 70 and B <= 30:
        return 2
    if B >= 95 and 60 <= C <= 70 and E <= 30:
        return 2
    if B >= 80 and 45 <= C <= 60 and E >= 80 and D >= 50:
        return 2
    if 35 <= C <= 40 and D <= 20 and B >= 65 and E >= 65:
        return 2
    if C >= 95 and B >= 70 and E > 25:
        return 2
    if C >= 75 and (B >= 85 or D <= 10):
        return 2

    # Additional class 4 tie-breaker
    if D <= 30 and E >= 95 and C <= 85:
        return 4

    # High C general lean to 1
    if C >= 65:
        return 1

    # Default
    return 1