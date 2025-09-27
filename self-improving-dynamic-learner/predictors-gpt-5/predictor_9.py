"""
Predictor 9
Generated on: 2025-09-09 12:26:20
Accuracy: 57.63%
"""


# PREDICTOR 9 - Accuracy: 57.63%
# Correct predictions: 5763/10000 (57.63%)

def predict_output(A, B, C, D, E):
    # Tiny C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # Very high C with extreme D
    if C >= 90 and D >= 90:
        return 1
    if C >= 90 and D <= 25:
        return 4

    # Very high C -> 2 with support
    if C >= 95 and (B >= 65 or E >= 75):
        return 2

    # Low D with high C -> 3
    if D <= 10 and C >= 80:
        return 3

    # Specific class 2 and 4 corrections
    if B >= 90 and 30 <= C <= 40 and D >= 60 and E <= 30:
        return 2
    if D <= 10 and E >= 70 and C <= 30:
        return 2
    if A <= 12 and 35 <= C <= 40 and E <= 20:
        return 4

    # Mid-low C patterns
    if C <= 35 and D <= 25 and E >= 50:
        return 4
    if 30 <= C <= 45 and D >= 55 and E <= 40:
        return 3

    # Low D with low-to-mid C -> 3 unless strong 1
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    # Low C general handling
    if C <= 30:
        if C <= 20 and E >= 60:
            return 4
        if E >= 90:
            return 4
        if B >= 90 and E >= 50:
            return 4
        if E >= 80:
            return 4
        if 25 <= D <= 65 and E <= 40 and (A <= 60 or B <= 60):
            return 3
        if A >= 80 and E <= 30 and D < 70:
            return 1

    # High E with low D and not-too-high C -> 4 (avoid C near 70)
    if D <= 30 and E >= 70 and C < 65:
        return 4

    # High D with mid C -> 3
    if D >= 90 and 50 <= C <= 70:
        return 3

    # Class 2 general patterns
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2
    if B >= 70 and 65 <= C <= 75 and (D >= 45 or E >= 85):
        return 2

    # Specific 3 pattern
    if 45 <= C <= 55 and D >= 40 and E >= 75 and B <= 20:
        return 3

    return 1