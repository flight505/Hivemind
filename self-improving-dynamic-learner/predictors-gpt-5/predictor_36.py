"""
Predictor 36
Generated on: 2025-09-09 13:29:10
Accuracy: 57.28%
"""


# PREDICTOR 36 - Accuracy: 57.28%
# Correct predictions: 5728/10000 (57.28%)

def predict_output(A, B, C, D, E):
    ed = E - D
    sumAB = A + B
    abs_diff_DE = E - D if E >= D else D - E

    # Tiny C band (C <= 12)
    if C <= 12:
        # High E with moderate D and decent B -> 2 (fix specific tiny-C case)
        if E >= 55 and 15 <= D <= 30 and B >= 45:
            return 2
        if E >= 55:
            return 4
        if D >= 80 and E <= 30:
            return 1
        if sumAB >= 165:
            return 1
        return 3

    # Very low C specifics and small-C structure
    if C <= 22 and D >= 90 and E <= 20:
        return 1
    if C <= 20 and E >= 70 and D <= 55:
        return 4
    if C <= 20 and E <= 25 and D >= 30:
        return 3
    if C <= 35 and D <= 20 and E <= 30:
        return 3

    # Specific pocket: C ~25 with very high B and mid-high D/E -> 4
    if 24 <= C <= 28 and B >= 95 and 60 <= D <= 80 and 35 <= E <= 60:
        return 4

    # Low-mid C with tiny D and high E -> 2
    if 30 <= C <= 45 and D <= 12 and E >= 70:
        return 2

    # Mid C, balanced D/E and low B -> 3
    if 45 <= C <= 55 and 35 <= D <= 60 and 35 <= E <= 60 and abs_diff_DE <= 10 and B <= 60:
        return 3

    # Guard: mid C with high B/D but very low E favors 1, not 2
    if 45 <= C <= 60 and B >= 80 and D >= 50 and E <= 25:
        return 1

    # High C with strong B -> 2
    if C >= 95 and B >= 70:
        return 2
    if C >= 90 and B >= 90:
        return 2

    # Prevent false 2 or 4 at high C extremes
    if C >= 90 and D >= 90 and E <= 10:
        return 1
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # Very high C general
    if C >= 88:
        if E <= 25:
            return 4
        return 1

    # Class 2 strong patterns
    if C >= 75 and D <= 10 and E >= 60:
        return 2
    if C >= 80 and B >= 90 and D >= 80 and E >= 60:
        return 2
    if 65 <= C <= 75 and D >= 50 and B >= 75:
        return 2
    if 45 <= C <= 60 and B >= 80 and D >= 50:
        return 2
    if 45 <= C <= 60 and D <= 20 and E >= 90:
        return 2

    # Strong class 4 patterns
    if 60 <= C <= 70 and D <= 20 and E >= 50 and sumAB <= 160:
        return 4
    if 50 <= C <= 60 and D <= 35 and E >= 35:
        return 4
    if 35 <= C <= 45 and ed >= 35 and D <= 35:
        return 4
    if 40 <= C <= 50 and D <= 40 and E >= 35 and E >= D:
        return 4

    # Low D and low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    return 1