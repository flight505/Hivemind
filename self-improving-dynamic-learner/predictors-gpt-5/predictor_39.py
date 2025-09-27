"""
Predictor 39
Generated on: 2025-09-09 13:39:12
Accuracy: 57.48%
"""


# PREDICTOR 39 - Accuracy: 57.48%
# Correct predictions: 5748/10000 (57.48%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B

    # Tiny C band (C <= 12)
    if C <= 12:
        # High D with high E -> 2
        if D >= 80 and E >= 55:
            return 2
        # High E -> 4
        if E >= 55:
            return 4
        # Strong 1 cues
        if sumAB >= 165 or (B >= 80 and E <= 30) or (A >= 75 and E <= 30):
            return 1
        # High D with low E -> 1
        if D >= 80 and E <= 30:
            return 1
        # Otherwise -> 3
        return 3

    # Very low C band (13..25)
    if C <= 25:
        # Low D with high E -> 4
        if D <= 20 and E >= 60:
            return 4
        # Very high E regardless of D -> 4
        if E >= 85:
            return 4
        # Low E with moderate/high D -> 3
        if E <= 20 and D >= 20:
            return 3
        # Very high D with not-high E -> 1
        if D >= 85 and E <= 60:
            return 1
        # Strong A+B -> 1
        if sumAB >= 165:
            return 1
        return 1

    # Low C with very high E and moderate D -> 4 (covers C around 27)
    if C <= 30 and E >= 70 and D <= 60:
        return 4

    # Specific mid/low pockets
    if 30 <= C <= 40 and E <= 5:
        if D >= 70:
            return 3
        if D >= 60:
            return 4

    # Mid-low C: low E with low D -> 3
    if 40 <= C <= 50 and D <= 25 and E <= 30:
        return 3

    # Mid C with low D and high E -> 4
    if 45 <= C <= 55 and D <= 35 and E >= 50:
        return 4

    # Mid C with very low E -> 4
    if 50 <= C <= 60 and E <= 10:
        return 4

    # Mid/High C with high D -> 3
    if 50 <= C <= 70 and D >= 75 and E >= 40:
        return 3

    # Mid-low C with strong B and high D but low E -> 2
    if 35 <= C <= 45 and B >= 80 and D >= 55 and E <= 30:
        return 2

    # Low-to-mid C with strong E dominating D -> 4
    if C <= 45 and E >= 70 and ed >= 35:
        return 4

    # High-C with tiny D specializations
    if C >= 90 and E <= 10 and D <= 20:
        return 4
    if C >= 90 and D <= 10 and E >= 60:
        return 4
    if 70 <= C < 90 and D <= 10 and E >= 60:
        return 2
    if C >= 75 and D <= 10 and E <= 30:
        return 1
    if 60 <= C <= 70 and D <= 10 and E <= 20:
        return 3

    # High C with low E generally -> 1
    if C >= 88 and E <= 25:
        return 1

    # Class 2 via B synergy
    if C >= 80 and B >= 90 and D >= 70 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75 and E >= 60:
        return 2

    # Mid C with low D and moderate E -> 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4

    return 1