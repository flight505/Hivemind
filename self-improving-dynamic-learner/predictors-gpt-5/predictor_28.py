"""
Predictor 28
Generated on: 2025-09-09 13:07:55
Accuracy: 56.38%
"""


# PREDICTOR 28 - Accuracy: 56.38%
# Correct predictions: 5638/10000 (56.38%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C
    if C <= 12:
        if E >= 55:
            return 4
        if (A + B) >= 165:
            return 1
        return 3

    # Low C (just above tiny)
    if C <= 25:
        # Strong joint A/B with high D -> 4
        if A >= 80 and B >= 80 and D >= 80:
            return 4
        # Low D with very high E -> 4
        if D <= 30 and E >= 85:
            return 4
        # Very low C with high E and modest D -> 4
        if C <= 20 and E >= 70 and D <= 55:
            return 4
        # Differentiate high D + high E by A (fixes conflicting cases)
        if D >= 60 and E >= 80:
            return 4 if A >= 80 else 1
        # Specific small-C mid D/E -> 1
        if 12 < C <= 15 and 50 <= E <= 60 and 35 <= D <= 50:
            return 1
        # High D with not-high E -> 1
        if D >= 80 and E <= 60:
            return 1
        return 3

    # Very high C
    if C >= 88:
        if E <= 25:
            if B >= 95 and D >= 70:
                return 2
            if D <= 10:
                return 1
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (70 to <88)
    if C >= 70:
        if D <= 5:
            return 2
        if D <= 10 and E >= 60:
            return 2
        if B >= 90 and D >= 80:
            return 2
        if D <= 10 and E <= 10:
            return 3
        return 1

    # Mid C (40 to 65)
    if 40 <= C <= 65:
        # Low D with high E -> 4
        if D <= 30 and E >= 70:
            return 4
        # High D in lower-mid C -> 3
        if 40 <= C <= 50 and D >= 70:
            return 3
        # High D with very high E -> 3
        if 40 <= C <= 50 and D >= 65 and E >= 85:
            return 3
        if D >= 70 and E >= 70:
            return 3
        # Very low D with decent E -> 2
        if D <= 10 and E >= 50:
            return 2
        # Extremely low E with moderate+ D -> 4
        if 45 <= C <= 65 and E <= 5 and D >= 40:
            return 4
        # Strong B with high D -> 2
        if 45 <= C <= 60 and B >= 80 and D >= 50:
            return 2
        # Upper-mid C with high D and moderate E -> 3
        if 60 <= C <= 65 and D >= 75 and E >= 45:
            return 3
        return 1

    # Low-mid C (30 to <40)
    if 30 <= C < 40:
        if ed >= 35:
            return 4
        if B >= 90 and D >= 60:
            return 2
        if D <= 10 and E >= 50:
            return 2
        if 20 <= D <= 40 and E <= 50:
            return 3
        if B >= 90 and D <= 35 and E <= 55:
            return 1
        return 1

    return 1