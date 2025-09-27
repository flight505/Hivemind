"""
Predictor 27
Generated on: 2025-09-09 13:04:24
Accuracy: 53.41%
"""


# PREDICTOR 27 - Accuracy: 53.41%
# Correct predictions: 5341/10000 (53.41%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Tiny C (very low)
    if C <= 6:
        # Strong 4 when D high and E high (or modest window) or very strong B
        if D >= 80 and (E >= 60 or (20 <= E <= 30) or B >= 80):
            return 4
        # 1 when moderate/high D with strong A or B
        if D >= 35 and (A >= 85 or B >= 80):
            return 1
        # Low D -> 3
        if D <= 20:
            return 3
        return 3

    # Low C region (but not tiny)
    if C <= 25:
        # Low D with very high E -> 4
        if D <= 30 and E >= 85:
            return 4
        # Very high D with very low E -> 1
        if D >= 90 and E <= 20:
            return 1
        # High D with moderate E -> 1
        if D >= 80 and 40 <= E <= 70:
            return 1
        # High D with E in mid-low window -> 4
        if D >= 80 and 30 <= E <= 40:
            return 4
        return 3

    # Very high C
    if C >= 88:
        # Strong 2 when C very high with very strong B and high D (regardless of E)
        if B >= 95 and D >= 70:
            return 2
        # Low E: prefer 1 when D is tiny or (B weak and D very high), else 4
        if E <= 25:
            if D <= 10:
                return 1
            if B < 80 and D >= 70:
                return 1
            return 4
        return 1

    # High C band
    if 70 <= C < 88:
        # Very low D -> 2
        if D <= 5:
            return 2
        # Very strong B with high D -> 2
        if B >= 90 and D >= 80:
            return 2
        # Tiny D with tiny E -> 3
        if D <= 10 and E <= 10:
            return 3
        return 1

    # Mid C band (40 to 60)
    if 40 <= C <= 60:
        # Fixes: 4 when E extremely low with moderate+ D
        if 45 <= C <= 65 and E <= 5 and D >= 40:
            return 4
        # 3 when D high in lower-mid C
        if 40 <= C <= 50 and D >= 70:
            return 3
        # 3 when D moderately high and E very high
        if D >= 65 and E >= 85:
            return 3
        # 2 when D very low and E strong
        if D <= 10 and E >= 50:
            return 2
        # 2 when B strong and D high-ish
        if 45 <= C <= 60 and B >= 80 and D >= 50:
            return 2
        # 2 when mid-low C with decent B/D/E
        if 35 <= C <= 50 and B >= 70 and D >= 45 and E >= 50:
            return 2
        return 1

    # Low-mid C (30 to <40)
    if 30 <= C < 40:
        # 4 when E dominates D strongly
        if ed >= 35:
            return 4
        # 2 when very high B with high D
        if B >= 90 and D >= 60:
            return 2
        # 3 when D is moderate and E not high
        if 20 <= D <= 40 and E <= 50:
            return 3
        return 1

    return 1