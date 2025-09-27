"""
Predictor 30
Generated on: 2025-09-09 13:15:00
Accuracy: 52.42%
"""


# PREDICTOR 30 - Accuracy: 52.42%
# Correct predictions: 5242/10000 (52.42%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 160 or (A >= 75 and B >= 50):
            return 1
        return 3

    # Low C (13 to 35)
    if C <= 35:
        # Very small sub-band (<= 20): finer handling
        if C <= 20:
            if D <= 10 and E >= 70:
                return 4
            if D >= 90 and E >= 60:
                return 4
            if 45 <= D <= 60 and 30 <= E <= 45:
                return 1
            if D <= 15 and E <= 40:
                return 1
            if E >= 70 and D <= 55:
                return 4

        # General rules for 13..35
        if D <= 10:
            if E >= 70:
                # Very low D with high E in this band → 2
                if C >= 21:
                    return 2
                return 4
            if E <= 20:
                return 3
        if C <= 25 and D <= 10 and E <= 35:
            return 1
        if D >= 90:
            if E <= 20:
                return 1
            if E >= 40 and C <= 25:
                return 1
        if 20 <= D <= 35 and 25 <= E <= 55 and A >= 80:
            return 1
        return 3

    # Very high C (>= 95)
    if C >= 95:
        if D <= 10:
            return 1
        if D >= 90:
            return 1
        if E <= 25:
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (88 to 94)
    if C >= 88:
        if E <= 25:
            if D <= 10:
                return 1
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (70 to 87)
    if C >= 70:
        if D <= 5:
            return 2
        if D <= 10 and E >= 60:
            return 2
        if B >= 80 and E >= 55 and D >= 20:
            return 2
        if D <= 10 and E <= 10:
            return 3
        return 1

    # Mid C (40 to 65)
    if 40 <= C <= 65:
        # Narrow band adjustments near 60-65
        if 60 <= C <= 65:
            if D <= 75 and E >= 75:
                return 1
            if D >= 75 and E >= 45:
                return 3

        # Low D with high E -> 4
        if D <= 30 and E >= 70:
            return 4
        # Slightly higher D but still low with high E -> 4
        if D <= 40 and E >= 70:
            return 4
        # Very low E with moderate+ D -> 4
        if E <= 20 and D >= 35:
            return 4
        # High D dominance in lower-mid C -> 3
        if 40 <= C <= 50 and D >= 70:
            return 3
        # High D and high E at lower mid C -> 3
        if 40 <= C <= 50 and D >= 65 and E >= 80:
            return 3
        # Generic high D & high E in lower mid C -> 3
        if D >= 70 and E >= 70 and C <= 55:
            return 3
        # Very high D dominance at C <= 45 -> 3
        if D >= 80 and C <= 45:
            return 3
        # Strong B, very high D, very high E in lower mid C -> 2
        if 40 <= C <= 50 and B >= 90 and D >= 85 and E >= 90:
            return 2
        # Very low D with strong E -> 2
        if D <= 10 and E >= 50:
            return 2
        # Strong B with high D in mid -> 2
        if 45 <= C <= 60 and B >= 80 and D >= 50:
            return 2
        return 1

    # For remaining (C in 36..39)
    if 36 <= C < 40:
        if D <= 10 and E <= 20:
            return 3
        if D <= 10 and E >= 60:
            return 2
        if ed >= 35:
            return 4
        if B >= 90 and D >= 60:
            return 2
        if D >= 75:
            return 3
        return 1

    return 1