"""
Predictor 16
Generated on: 2025-09-09 12:42:27
Accuracy: 41.61%
"""


# PREDICTOR 16 - Accuracy: 41.61%
# Correct predictions: 4161/10000 (41.61%)

def predict_output(A, B, C, D, E):
    # Tiny C -> 3
    if C <= 12:
        return 3

    # Low C band (13-25)
    if C <= 25:
        if E >= 85:
            return 4
        if D >= 85:
            return 1
        return 1

    # Mid-high C with low D and low E -> 4 (correction)
    if 65 <= C < 78 and E <= 40 and D <= 25:
        return 4

    # High E in mid C -> 4 (correction)
    if 40 <= C <= 55 and E >= 80:
        return 4

    # Low E and very low D in low-mid C -> 3 (correction)
    if C < 50 and D <= 20 and E <= 20:
        return 3

    # Very high C with low E and not tiny D -> 4 (correction)
    if C >= 90 and E <= 50 and D >= 30:
        return 4

    # Mid C with very low D and very high E -> 2 (correction)
    if 50 <= C <= 60 and D <= 10 and E >= 80:
        return 2

    # Very high C -> 2
    if C >= 78:
        return 2

    # High E with low D and not-too-high C -> 4
    if D <= 30 and E >= 95 and C <= 85:
        return 4

    # High-mid C -> 1
    if 65 <= C < 78:
        return 1

    # Mid C -> 1
    if 50 <= C <= 64:
        return 1

    # Default
    return 1