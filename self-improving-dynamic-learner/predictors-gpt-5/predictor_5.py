"""
Predictor 5
Generated on: 2025-09-09 12:12:41
Accuracy: 58.88%
"""


# PREDICTOR 5 - Accuracy: 58.88%
# Correct predictions: 5888/10000 (58.88%)

def predict_output(A, B, C, D, E):
    # Very small C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # Very high C with strong B -> 2
    if C >= 95 and B >= 70:
        return 2

    # Very high C general
    if C >= 88:
        if E <= 25:
            return 4
        return 1

    # Low D and low-to-mid C -> 3 unless strong 1-signals
    if D <= 12 and C <= 45:
        if A >= 70 or B >= 90 or E >= 80:
            return 1
        return 3

    # High D with low-mid C and low E -> 3
    if D >= 95 and 30 <= C <= 40 and E <= 25:
        return 3

    # Class 2 patterns
    if A <= 35 and C >= 65 and (B >= 70 or D <= 10):
        return 2
    if B >= 90 and 70 <= C <= 85 and D >= 50:
        return 2
    if B >= 90 and D >= 80 and C <= 40 and E >= 90:
        return 2

    # Low C with low D and low E -> 3
    if C <= 35 and D <= 20 and E <= 30:
        return 3

    # Very low C with high E and moderate D -> 4
    if C <= 20 and E >= 70 and D <= 55:
        return 4

    # Low C general handling
    if C <= 30:
        if D <= 20 and E >= 60:
            return 4
        if D >= 90 and E >= 95:
            return 3
        if E >= 85:
            return 4
        if A >= 80 and E <= 30:
            return 3

    # High E with low D and not-too-high C -> 4 (requires some A/B strength)
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

    return 1