"""
Predictor 29
Generated on: 2025-09-09 13:10:26
Accuracy: 56.83%
"""


# PREDICTOR 29 - Accuracy: 56.83%
# Correct predictions: 5683/10000 (56.83%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # Low C (just above tiny)
    if C <= 25:
        # Very high E with low D -> 4
        if D <= 30 and E >= 85:
            return 4
        # High D and very low E -> 1
        if D >= 90 and E <= 20:
            return 1
        # Moderate/high D with not-high E -> 1
        if D >= 50 and E <= 50:
            return 1
        # Default in this band
        return 3

    # Very high C (C >= 95)
    if C >= 95:
        # Overrides
        if D <= 10:
            return 1
        if D >= 90:
            return 1
        if E <= 25:
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (88 <= C < 95)
    if C >= 88:
        if E <= 25:
            if D <= 10:
                return 1
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C band (70 <= C < 88)
    if C >= 70:
        if D <= 5:
            return 2
        if D <= 10 and E >= 60:
            return 2
        if B >= 90 and D >= 80:
            return 2
        # Allow 2 with strong B/E and moderate D
        if B >= 80 and E >= 55 and D >= 35:
            return 2
        if D <= 10 and E <= 10:
            return 3
        return 1

    # Mid C band (40 <= C <= 65)
    if 40 <= C <= 65:
        # Strong high-D override to 1 (avoids false 3)
        if C >= 60 and D >= 85:
            return 1
        # Low D with high E -> 4
        if D <= 30 and E >= 70:
            return 4
        # Low D with low E -> 3
        if D <= 20 and E <= 20:
            return 3
        # High D with very high E -> 3
        if D >= 70 and E >= 70:
            return 3
        # Very low E with moderate+ D -> 4
        if E <= 10 and D >= 40:
            return 4
        # Very low D with strong E -> 2
        if D <= 10 and E >= 50:
            return 2
        # Strong B with high D -> 2
        if B >= 80 and D >= 50:
            return 2
        return 1

    # Low-mid C (30 <= C < 40)
    if 30 <= C < 40:
        # Very low D and very low E -> 3
        if D <= 10 and E <= 20:
            return 3
        # E strongly exceeds D -> 4
        if ed >= 35:
            return 4
        # Very low D with strong E -> 2
        if D <= 10 and E >= 60:
            return 2
        # Very high B with high D -> 2
        if B >= 90 and D >= 60:
            return 2
        # Moderate D with low-mid E -> 3
        if 20 <= D <= 40 and E <= 50:
            return 3
        return 1

    return 1