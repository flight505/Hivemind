"""
Predictor 10
Generated on: 2025-09-09 12:29:45
Accuracy: 54.23%
"""


# PREDICTOR 10 - Accuracy: 54.23%
# Correct predictions: 5423/10000 (54.23%)

def predict_output(A, B, C, D, E):
    # Tiny C
    if C <= 12:
        if D >= 60 and E <= 35:
            return 4
        if A >= 90 and E <= 35:
            return 1
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # Very high C
    if C >= 90:
        if D <= 25:
            return 3 if E <= 20 else 4
        return 1

    # Specific corrections and strong patterns
    if C <= 30 and E >= 90 and D >= 80:
        return 1  # e.g., high D and very high E with very low C -> 1
    if B >= 80 and 35 <= C <= 45 and E >= 90:
        return 2  # high B, mid-low C, very high E
    if C <= 20 and E >= 55 and D >= 30:
        return 4  # very low C with mid/high D and mid-high E
    if A <= 15 and E <= 15 and 50 <= C <= 70:
        return 4  # very small A, very low E, mid C
    if D <= 10 and C <= 30 and E >= 70:
        return 2  # very low D, very low C, high E
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3
    if D >= 90 and 50 <= C <= 80:
        return 3  # high D with mid C

    # Class 2 patterns
    if B >= 90 and 30 <= C <= 40 and D >= 50:
        return 2
    if B >= 90 and 45 <= C <= 55 and D >= 80:
        return 2
    if B >= 90 and 70 <= C <= 85 and D >= 50:
        return 2
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2

    # Class 4 patterns (low C emphasis)
    if C <= 30 and E >= 85 and D <= 60:
        return 4
    if C <= 20 and E >= 60 and 30 <= D <= 80:
        return 4
    if C <= 35 and D <= 25 and E >= 50:
        return 4
    if C <= 30 and B >= 90 and E >= 50 and D <= 80:
        return 4
    if 30 <= C <= 40 and E <= 20 and 40 <= D <= 60:
        return 4
    if 35 <= C <= 40 and 30 <= D <= 40 and 20 <= E <= 30 and B <= 20:
        return 4

    # Class 3 patterns
    if 30 <= C <= 45 and D >= 80:
        return 3
    if C <= 30 and 25 <= D <= 65 and E <= 40:
        return 3
    if 50 <= C <= 60 and D >= 70 and E >= 70:
        return 3

    return 1