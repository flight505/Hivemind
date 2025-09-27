"""
Predictor 36
Generated on: 2025-09-09 04:01:37
Accuracy: 29.20%
"""


# PREDICTOR 36 - Accuracy: 29.20%
# Correct predictions: 2920/10000 (29.20%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logical tests.
    The rules are ordered from most specific to most general.
    """

    # ----- Very high C (≥90) -----
    if C >= 90:
        if B >= 60:
            return 2                      # high C with decent B → class 2
        return 4                          # otherwise → class 4

    # ----- High C (80‑89) -----
    if C >= 80:
        if B >= 60:
            return 2
        return 4

    # ----- High C (70‑79) -----
    if C >= 70:
        if B >= 80:
            return 2
        if B <= 35 and E < 30:
            return 4                      # low B & low E → class 4
        if B <= 35 and E >= 70:
            return 2                      # low B but very high E → class 2
        return 1

    # ----- Mid‑high C (50‑69) -----
    if C >= 50:
        if B >= 80:
            return 2
        if B <= 35 and E < 30:
            return 4
        # specific pattern for C around 45‑55 with strong B and moderate‑high E
        if 45 <= C <= 55 and B >= 70 and E >= 50:
            return 2
        # pattern where moderate B, low E gives class 3
        if 45 <= C <= 60 and E < 30 and 30 <= B <= 60:
            return 3
        return 

    # ----- Mid C (30‑49) -----
    if C >= 30:
        if B >= 60 and E >= 70:
            return 2
        if B >= 60 and E < 30:
            return 4
        return 1

    # ----- Low C (≤20) -----
    if C <= 20:
        if E >= 70:
            return 2                      # high E overrides low C
        if D > 70 and E < 30:
            return 4                      # high D with very low E → class 4
        if B <= 15:
            return 3                      # low B & low C → class 3
        if B >= 60 and E < 30:
            return 3                      # moderate B but low E → class 3
        # new rule to catch moderate B and moderate‑high E for low C
        if B >= 50 and E >= 50:
            return 2
        return 1

    # ----- Default fallback -----
    return 1