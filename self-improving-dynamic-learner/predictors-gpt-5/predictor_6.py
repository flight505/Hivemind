"""
Predictor 6
Generated on: 2025-09-09 12:17:05
Accuracy: 58.31%
"""


# PREDICTOR 6 - Accuracy: 58.31%
# Correct predictions: 5831/10000 (58.31%)

def predict_output(A, B, C, D, E):
    # Very small C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # High C with very low E -> 4
    if C >= 88 and E <= 25:
        return 4

    # Low D and low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    # Very small A with strong signal -> 1
    if A <= 10 and (E >= 80 or C >= 70):
        return 1

    # High C but low D with very high E -> 1 (override)
    if C > 90 and D <= 30 and E >= 95:
        return 1

    # Class 2 strong: high B, high D, low C, very high E
    if B >= 90 and D >= 80 and C <= 40 and E >= 90:
        return 2

    # Very high C with decent B -> 2
    if C >= 90 and B >= 65 and E > 25:
        return 2

    # Specific 4 patterns around mid-low C
    if A <= 20 and B >= 80 and 30 <= C <= 45:
        return 4
    if B >= 90 and 30 <= C <= 40 and 40 <= D <= 60:
        return 4

    # Class 2 patterns
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2
    if B >= 80 and 65 <= C <= 75 and D >= 50:
        return 2
    if A <= 35 and D <= 10 and 50 <= C <= 60:
        return 2

    # Small A, small E, mid C -> 4
    if A <= 15 and E <= 15 and 50 <= C <= 65:
        return 4

    # High D with mid C -> 3
    if D >= 90 and 50 <= C <= 70:
        return 3

    # Mid-low C with low E and high D -> 3
    if 30 <= C <= 40 and E <= 20 and D >= 60:
        return 3

    # Low C, low D, low E -> 3
    if C <= 35 and D <= 20 and E <= 30:
        return 3

    # Low C detailed handling
    if C <= 30:
        if D <= 20 and E >= 60:
            return 4
        if C <= 20 and E >= 70 and D <= 55:
            return 4
        if D >= 90 and B < 95:
            return 3
        if D >= 70 and E <= 30:
            return 3
        if A >= 80 and E <= 30 and D < 70:
            return 1
        if E >= 85 and D <= 60:
            return 4

    # High E with low D and not-too-high C -> 4
    if D <= 30 and E >= 95 and C <= 85:
        return 4
    if D <= 30 and E >= 70 and C < 70 and (A >= 40 or B >= 30):
        return 4

    # Mid C with high D and high E -> 3
    if 50 <= C <= 60 and D >= 70 and E >= 70:
        return 3

    return 1