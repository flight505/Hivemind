"""
Predictor 31
Generated on: 2025-09-09 13:18:20
Accuracy: 54.67%
"""


# PREDICTOR 31 - Accuracy: 54.67%
# Correct predictions: 5467/10000 (54.67%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C (very low)
    if C <= 12:
        if E >= 55:
            return 4
        return 3

    # Low C (<=25)
    if C <= 25:
        # Very high D with very low E -> 1
        if D >= 90 and E <= 20:
            return 1
        # Very low C with very high E and low/moderate D -> 4
        if C <= 22 and E >= 90 and D <= 40:
            return 4
        # Tiny D and low-mid E -> 1
        if D <= 10 and E <= 35:
            return 1
        # Low C with low D and not-high E -> 1
        if D <= 15 and E <= 40:
            return 1
        # High D and not-high E -> 1
        if D >= 50 and E <= 50:
            return 1
        # Special: very low C, very low E, high D with strong B -> 4
        if C <= 20 and E <= 15 and D >= 50 and B >= 70:
            return 4
        # Special: low C near 25, moderate D and low E -> 1
        if C <= 26 and 30 <= D <= 45 and E <= 25:
            return 1
        # Special: low C with moderately high E and not-too-high D -> 4
        if C <= 22 and E >= 65 and D <= 60:
            return 4
        return 3

    # Low-mid C (26..35)
    if 26 <= C <= 35:
        # Very low D with high E -> 2
        if D <= 12 and E >= 70:
            return 2
        # Moderate D with high E in this band -> 1
        if 30 <= C <= 35 and 35 <= D <= 55 and E >= 70:
            return 1
        # Very low D with very low E -> 3
        if D <= 10 and E <= 20:
            return 3
        # Strong E dominance -> 4
        if ed >= 35:
            return 4
        return 3

    # Very high C (>=95)
    if C >= 95:
        if D <= 10 or D >= 90:
            return 1
        if E <= 25:
            return 4
        if B >= 90 and D >= 80:
            return 2
        return 1

    # High C (88..94)
    if 88 <= C < 95:
        if E <= 25:
            if D <= 10:
                return 1
            return 4
        if B >= 90 and D >= 80:
            return 2
        # If fairly high C and D already high, prefer 1 over 2
        if D >= 50:
            return 1
        return 1

    # High C (70..87)
    if 70 <= C < 88:
        # Override: very high A with tiny D -> 1
        if A >= 95 and D <= 6:
            return 1
        # Override: fairly high C with high D -> 1
        if C >= 85 and D >= 50 and E > 25:
            return 1
        # Very low D -> 2
        if D <= 5:
            return 2
        # Very low D with strong E -> 2
        if D <= 10 and E >= 60:
            return 2
        # Strong B/E with moderate+ D -> 2
        if B >= 80 and E >= 55 and D >= 20:
            return 2
        # Tiny D and tiny E -> 3
        if D <= 10 and E <= 10:
            return 3
        # Very high D with very low E in this band -> 3
        if D >= 90 and E <= 30:
            return 3
        return 1

    # Mid C (40..65)
    if 40 <= C <= 65:
        # Narrow: very high C in band with very high D and high E -> 1
        if 60 <= C <= 65 and D >= 85 and E >= 80:
            return 1
        # Low D with high E -> 4
        if D <= 30 and E >= 70:
            return 4
        # Slightly higher D but still low with high E -> 4
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
        # Very high D dominance at low end of band -> 3
        if D >= 80 and C <= 45:
            return 3
        # Strong B with very high D and E -> 2
        if 40 <= C <= 50 and B >= 85 and D >= 85 and E >= 90:
            return 2
        # Very low D with strong E -> 2
        if D <= 10 and E >= 50:
            return 2
        # Strong B with high D -> 2
        if B >= 80 and D >= 50:
            return 2
        # Specific: C around 40 with very high D -> 3
        if C <= 45 and D >= 75:
            return 3
        # Specific: mid band, high D, low E -> 1
        if 50 <= C <= 60 and D >= 70 and E <= 50:
            return 1
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