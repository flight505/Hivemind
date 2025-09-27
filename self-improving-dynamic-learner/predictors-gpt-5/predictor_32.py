"""
Predictor 32
Generated on: 2025-09-09 13:20:48
Accuracy: 54.86%
"""


# PREDICTOR 32 - Accuracy: 54.86%
# Correct predictions: 5486/10000 (54.86%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C (very low)
    if C <= 6:
        # Special: tiny C with strong B and moderate E -> 1
        if B >= 60 and E >= 45:
            return 1
        # Standard tiny C rule
        if E >= 55:
            return 4
        # High A with moderate D also nudges 1
        if A >= 90 and D >= 25:
            return 1
        return 3

    if C <= 12:
        if E >= 55:
            return 4
        return 3

    # Low C (13..25)
    if C <= 25:
        # Very high E with low/moderate D -> 4
        if C <= 22 and E >= 80 and D <= 55:
            return 4
        # Very high B with high D at very low C -> 4
        if C <= 20 and B >= 90 and D >= 80:
            return 4
        # High D and low E -> 1
        if D >= 90 and E <= 20:
            return 1
        # High D and moderate E -> 1
        if D >= 70 and E >= 50 and C <= 20:
            return 1
        # High D and E in mid-low window -> 1
        if C <= 25 and D >= 85 and E >= 45:
            return 1
        # Tiny D and low E -> 1
        if D <= 10 and E <= 35:
            return 1
        # Low D and high E -> 4
        if D <= 20 and E >= 70:
            return 4
        # Default for low C
        return 3

    # Low-mid C (26..35)
    if 26 <= C <= 35:
        # Very low D with high E -> 2
        if D <= 12 and E >= 70:
            return 2
        # Moderate D and high E -> 1
        if 26 <= C <= 35 and 25 <= D <= 60 and E >= 70:
            return 1
        # Moderate D and mid E -> 1
        if 26 <= C <= 35 and 25 <= D <= 60 and 25 <= E <= 60:
            return 1
        # E dominance -> 4
        if ed >= 35:
            return 4
        # Very low D and very low E -> 3
        if D <= 10 and E <= 20:
            return 3
        # Strong B with very high D and E -> 2
        if 30 <= C <= 35 and B >= 90 and D >= 90 and E >= 80:
            return 2
        return 3

    # Very high C (>=95)
    if C >= 95:
        if B >= 95:
            return 2
        if D <= 10 or D >= 90:
            return 1
        if E <= 25:
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (88..94)
    if 88 <= C < 95:
        if B >= 95:
            return 2
        if E <= 25:
            if D <= 10:
                return 1
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (70..87)
    if 70 <= C < 88:
        # Exception: very high A with tiny D -> 1 (avoid false 2)
        if A >= 95 and D <= 6:
            return 1
        # If C quite high and D already high -> 1
        if C >= 85 and D >= 50:
            return 1
        # Very low D -> 2
        if D <= 5:
            return 2
        # Very low D with strong E -> 2
        if D <= 10 and E >= 60:
            return 2
        # Strong B/E with moderate+ D -> 2
        if B >= 95 and D >= 50:
            return 2
        if B >= 80 and E >= 55 and D >= 20:
            return 2
        # Tiny D and tiny E -> 3
        if D <= 10 and E <= 10:
            return 3
        # Very low E at high C with moderate D -> 4
        if E <= 5 and D >= 30:
            return 4
        return 1

    # Mid C (40..65)
    if 40 <= C <= 65:
        # Very high D regardless of E (avoid false 3)
        if 50 <= C <= 60 and D >= 90:
            return 1
        # Low D with high E -> 4
        if D <= 30 and E >= 70:
            return 4
        # Slightly higher D with high E -> 4
        if D <= 40 and E >= 70:
            return 4
        # Very low E with moderate+ D -> 4
        if E <= 10 and D >= 40:
            return 4
        # High D in lower-mid C -> 3
        if 40 <= C <= 50 and D >= 70:
            return 3
        # High D and high E at lower-mid C -> 3
        if 40 <= C <= 50 and D >= 65 and E >= 80:
            return 3
        # Generic high D & high E when C not too high -> 3
        if D >= 70 and E >= 70 and C <= 55:
            return 3
        # Very high D dominance at low end -> 3
        if D >= 80 and C <= 45:
            return 3
        # Very low D: decide by E (>=70 -> 2 else -> 1)
        if D <= 10:
            return 2 if E >= 70 else 1
        # Strong B with high D -> 2
        if B >= 80 and D >= 50:
            return 2
        return 1

    # Low-mid C (36..39)
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