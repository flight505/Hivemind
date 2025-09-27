"""
Predictor 7
Generated on: 2025-09-09 12:20:33
Accuracy: 56.85%
"""


# PREDICTOR 7 - Accuracy: 56.85%
# Correct predictions: 5685/10000 (56.85%)

def predict_output(A, B, C, D, E):
    # Tiny C
    if C <= 12:
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        if E >= 60:
            return 4
        return 3

    # Very high C
    if C >= 90:
        if D <= 25:
            return 4
        if B >= 65 and E >= 25:
            return 2
        return 1

    # Very low D with high E -> 2 (guarded to avoid overfitting)
    if D <= 10 and E >= 70 and (C >= 60 or A <= 35 or B <= 80):
        return 2

    # Low D with low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    # High D with mid-low C -> 3
    if D >= 85 and 35 <= C <= 55:
        return 3

    # Specific 4 patterns
    if A <= 15 and E <= 15 and 50 <= C <= 65:
        return 4
    if A <= 20 and B >= 80 and 30 <= C <= 45:
        return 4
    if B >= 90 and 30 <= C <= 40 and 40 <= D <= 60:
        return 4

    # Strong class 2 patterns
    if B >= 70 and C >= 85:
        return 2
    if B >= 70 and 65 <= C <= 75 and E >= 30 and (D >= 45 or E >= 85):
        return 2
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2

    # Low C (13..30) nuanced handling
    if C <= 30:
        if D >= 90 and E >= 95:
            return 3
        if D <= 20 and E >= 60:
            return 4
        if E >= 85 and D <= 60:
            return 4
        if A >= 80 and E <= 30 and D < 70:
            return 1

    # High E with low D and not-too-high C -> 4
    if D <= 30 and E >= 70 and C < 70:
        return 4

    # High D with mid C -> 3
    if D >= 90 and 50 <= C <= 70:
        return 3

    return 1