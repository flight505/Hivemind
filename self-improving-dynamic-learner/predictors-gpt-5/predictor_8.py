"""
Predictor 8
Generated on: 2025-09-09 12:23:20
Accuracy: 56.31%
"""


# PREDICTOR 8 - Accuracy: 56.31%
# Correct predictions: 5631/10000 (56.31%)

def predict_output(A, B, C, D, E):
    # Tiny C
    if C <= 12:
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        if E >= 55:
            return 4
        return 3

    # Very high C: prioritize 1 with very high D, 4 with very low D
    if C >= 90 and D >= 90:
        return 1
    if C >= 90 and D <= 25:
        return 4

    # High C but not extreme: 2 when B high and D low
    if 85 <= C <= 92 and B >= 70 and D <= 30 and E >= 30:
        return 2

    # Very low D with very high E and mid C -> 4
    if D <= 12 and E >= 90 and 50 <= C <= 70:
        return 4

    # Low D and low E with not-high C -> 3
    if D <= 20 and C <= 60 and E <= 20:
        return 3

    # Override: low D, high E, C near 70 but both A and B high -> 1
    if D <= 25 and E >= 70 and 65 <= C <= 70 and A >= 70 and B >= 70:
        return 1

    # Strong class 2 when B very high, C high, D high, E very low
    if B >= 95 and 70 <= C <= 80 and D >= 80 and E <= 10:
        return 2

    # Mid-low C with high D -> 3
    if 30 <= C <= 45 and D >= 80:
        return 3
    if 30 <= C <= 45 and D >= 55 and E <= 40:
        return 3

    # Specific 4 patterns
    if A <= 20 and B >= 80 and 30 <= C <= 45:
        return 4
    if B >= 90 and 30 <= C <= 40 and 40 <= D <= 60:
        return 4

    # Class 2 patterns (general)
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2
    if B >= 70 and 65 <= C <= 75 and (D >= 45 or E >= 85):
        return 2

    # Very low C with high E and moderate D -> 4
    if C <= 20 and E >= 70 and D <= 55:
        return 4

    # Low C with moderate D and low E -> 3
    if C <= 30 and 25 <= D <= 65 and E <= 40:
        return 3
    if C <= 30 and A < 20 and 20 <= D <= 60 and E <= 30:
        return 3

    # High E with low D and not-too-high C -> 4 (broad)
    if D <= 30 and E >= 95 and C <= 85:
        return 4
    if D <= 30 and E >= 70 and C < 70 and (A >= 40 or B >= 30):
        return 4

    # High D with mid C -> 3
    if D >= 90 and 50 <= C <= 70:
        return 3

    # Mid C with high D and high E -> 3
    if 50 <= C <= 60 and D >= 70 and E >= 70:
        return 3

    # Specific corrections
    if 45 <= C <= 55 and D >= 40 and E >= 75 and B <= 20:
        return 3
    if 35 <= C <= 40 and 30 <= D <= 40 and 20 <= E <= 30 and 30 <= A <= 45 and B <= 20:
        return 4

    return 1