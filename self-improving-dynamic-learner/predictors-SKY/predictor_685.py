"""
Predictor 685
Generated on: 2025-09-09 19:35:36
Accuracy: 48.88%
"""


# PREDICTOR 685 - Accuracy: 48.88%
# Correct predictions: 4888/10000 (48.88%)

def predict_output(A, B, C, D, E):
    # Specific rules for 1
    if B > 90 and C < 20:
        return 1
    if B < 10 and C < 25 and E > 75:
        return 1
    if A > 80 and B < 40 and C > 50 and D < 10 and E > 80:
        return 1
    if B > 90 and 60 < C < 80 and D < 20 and E > 70:
        return 1
    # Specific rule for 2
    if A < 10 and C < 25 and E > 75:
        return 2
    # Specific rules for 4
    if E > 90 and D < 10:
        return 4
    if D > 90 and E < 10:
        return 4
    # General rules for 4
    if C < 25 and E > 75 and B > 10:
        return 4
    if B > 65 and C < 30 and A > 50 and E > 70:
        return 4
    if C >= 85 and E < 20 and B < 50:
        return 4
    if C > 80 and D < 20 and B < 40:
        return 4
    # Specific rules for 3
    if D > 90 and B > 65:
        return 3
    if C < 10 and B > 60:
        return 3
    if E < 10 and B > 50:
        return 3
    # General rules for 3
    if B < 20 and C < 20:
        return 3
    if 55 < B < 65 and D > 70:
        return 3
    if A < 10 and D < 10 and B > 40:
        return 3
    # Rules for 2
    if A < 50 and B + C > 120:
        return 2
    if B > 60 and C > 70:
        return 2
    if B > 60 and C > 50 and E >= 70:
        return 2
    # Default
    return 1