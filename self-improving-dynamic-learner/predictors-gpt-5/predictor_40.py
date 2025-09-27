"""
Predictor 40
Generated on: 2025-09-09 13:42:28
Accuracy: 59.62%
"""


# PREDICTOR 40 - Accuracy: 59.62%
# Correct predictions: 5962/10000 (59.62%)

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
        # Specific 1-case
        if C <= 22 and D >= 90 and E <= 20:
            return 1
        # High E with not-high D -> 4 (covers C=13, D=50, E=75)
        if E >= 70 and D <= 60:
            return 4
        # Low D with high E -> 4
        if D <= 20 and E >= 60:
            return 4
        # Very high E -> 4
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

    # Low C with very high E and moderate D -> 4 (extends to C up to 30)
    if C <= 30 and E >= 70 and D <= 60:
        return 4

    # Very low E in low-mid C
    if 30 <= C <= 40 and E <= 5:
        if D >= 70:
            return 3
        if D >= 60:
            return 4

    # Class 2 in low-mid C
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2
    if 30 <= C <= 45 and B >= 80 and D >= 60 and E >= 60:
        return 2

    # Strong class 4 via E dominating D at low C
    if C <= 45 and ed >= 35:
        return 4

    # Mid-low C: low E with low D -> 3
    if 40 <= C <= 50 and D <= 25 and E <= 30:
        return 3

    # Specific class 4 at C ~ 48 with strong B, low D, high E
    if 45 <= C <= 50 and D <= 35 and E >= 70 and B >= 80:
        return 4

    # Mid C with very low E -> 1 (fixes several cases)
    if 50 <= C <= 60 and E <= 10:
        return 1

    # Mid/High C with high D -> 3, except a pocket that is 1
    if 65 <= C <= 72 and D >= 75 and E >= 60:
        return 1
    if 50 <= C <= 70 and D >= 75 and E >= 40:
        return 3

    # Mid C with very low D and high E -> 2
    if 45 <= C <= 60 and D <= 12 and E >= 60:
        return 2

    # High C with small D specializations
    if C >= 90 and E <= 10 and D <= 20:
        return 4
    if 70 <= C < 90 and D <= 10 and E >= 60:
        return 2
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # Very high C with very low E (and not tiny D) -> 1
    if C >= 88 and E <= 25 and D > 10:
        return 1

    # Class 2 via B synergy
    if C >= 80 and B >= 90 and D >= 70 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75 and E >= 60:
        return 2

    # Special pocket: high C mid band with low D and very low E but decent B -> 2
    if 60 <= C <= 70 and D <= 35 and E <= 15 and B >= 50:
        return 2

    return 1