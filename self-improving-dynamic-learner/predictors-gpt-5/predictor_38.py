"""
Predictor 38
Generated on: 2025-09-09 13:35:52
Accuracy: 59.19%
"""


# PREDICTOR 38 - Accuracy: 59.19%
# Correct predictions: 5919/10000 (59.19%)

def predict_output(A, B, C, D, E):
    sumAB = A + B

    # Tiny C band (C <= 12)
    if C <= 12:
        # Very high B, D, E -> 2
        if B >= 90 and D >= 90 and E >= 90:
            return 2
        # Strong 1 cues with small C
        if sumAB >= 165 or (B >= 80 and E <= 30) or (A >= 75 and E <= 30):
            return 1
        # High E -> 4
        if E >= 55:
            return 4
        # High D with low E -> 1
        if D >= 80 and E <= 30:
            return 1
        # Otherwise -> 3
        return 3

    # Very low C band (13..25)
    if C <= 25:
        if sumAB >= 165:
            return 1
        if D <= 15 and E >= 50:
            return 4
        if E >= 80 and D <= 55:
            return 4
        if C >= 15 and D >= 85 and E <= 60:
            return 1
        return 1

    # Specific mid/low pockets
    if 30 <= C <= 40 and D >= 60 and E <= 5:
        return 4
    if 50 <= C <= 60 and E <= 10:
        return 4
    if 50 <= C <= 70 and D >= 75 and E >= 40:
        return 3

    # High-C with tiny D specializations
    if C >= 90 and D <= 10 and E >= 60:
        return 4
    if C >= 88 and E <= 25 and D > 10:
        return 1
    if C >= 75 and D <= 10 and E <= 30:
        return 1
    if C >= 70 and D <= 10 and E <= 12:
        return 3
    if 70 <= C < 90 and D <= 10 and E >= 60:
        return 2

    # Class 2 via B synergy
    if C >= 80 and B >= 90 and D >= 70 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75 and E >= 60:
        return 2
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2

    # High C with low E but moderate D -> 4
    if C >= 85 and E <= 35 and D <= 50:
        return 4
    if C >= 80 and E <= 20 and D <= 50:
        return 4

    return 1