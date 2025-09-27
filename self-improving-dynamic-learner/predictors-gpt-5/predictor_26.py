"""
Predictor 26
Generated on: 2025-09-09 13:00:10
Accuracy: 52.84%
"""


# PREDICTOR 26 - Accuracy: 52.84%
# Correct predictions: 5284/10000 (52.84%)

def predict_output(A, B, C, D, E):
    # Very low C: specialized handling
    if C <= 6:
        # Strong 4 when D is very high with supportive B/E
        if D >= 90 and B >= 60 and E >= 20:
            return 4
        # 1 when tiny C but strong A/B and moderate D
        if D >= 35 and (A >= 85 or B >= 80):
            return 1
        # 1 when moderate D and very high A
        if 20 <= D <= 40 and A >= 85:
            return 1
        # Low D -> 3
        if D <= 20:
            return 3
        # Otherwise 3
        return 3

    # Low C region
    if C <= 25:
        # High D and high E -> 4
        if D >= 90 and E >= 60:
            return 4
        # High D and very low E -> 1
        if D >= 90 and E <= 20:
            return 1
        # Low D and very high E -> 4
        if D <= 30 and E >= 85:
            return 4
        # High D with strong B and moderate E -> 1
        if D >= 85 and E >= 40 and B >= 90:
            return 1
        # Mid-high D and very low E -> 3
        if D >= 45 and E <= 20:
            return 3
        # Default in this band -> 3
        return 3

    # Very high C
    if C >= 88:
        # Low D with low E -> 1
        if D <= 20 and E <= 20:
            return 1
        # High D with low E -> 1
        if D >= 70 and E <= 25:
            return 1
        # Strong 2 signature with very high B and D and decent E
        if B >= 90 and D >= 80 and E >= 60:
            return 2
        return 1

    # High C band
    if 70 <= C < 88:
        # Very low D -> 2
        if D <= 5:
            return 2
        # High B with high D -> 2
        if B >= 90 and D >= 80:
            return 2
        # Otherwise -> 1
        return 1

    # Mid C band
    if 40 <= C <= 60:
        # High D and high E -> 3
        if D >= 70 and E >= 70:
            return 3
        # Very low D with decent E -> 2
        if D <= 10 and E >= 50:
            return 2
        return 1

    # Fallback
    return 1