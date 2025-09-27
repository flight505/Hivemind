"""
Predictor 65
Generated on: 2025-09-09 04:21:45
Accuracy: 56.13%
"""


# PREDICTOR 65 - Accuracy: 56.13%
# Correct predictions: 5613/10000 (56.13%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic,
    comparisons and logical tests.  The rules are ordered
    from the most specific to the most general.
    """

    # 1. Very high C (≥ 90) → class 1
    if C >= 90:
        return 1

    # 2. High C with very high D overrides everything → class 1
    if C >= 70 and D > 90:
        return 1

    # 3. High C + very low E → class 4
    if C >= 70 and E < 20:
        return 4

    # 4. High C + extremely low B (≤ 8) → class 4
    if C >= 70 and B <= 8:
        return 4

    # 5. High C + high B & high E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # 6. High B (≥ 80) with medium C (30‑50) and moderate E (< 70) → class 4
    if 30 <= C <= 50 and B >= 80 and E < 70:
        return 4

    # -------------------------------------------------
    # Low C region (≤ 12)
    # -------------------------------------------------
    if C <= 12:
        if B <= 15:                 # low B with very low C → class 3
            return 3
        if E >= 80:                 # very high E pushes to class 4
            return 4
        if E >= 60:                 # high E also pushes to class 4
            return 4
        return 1                    # other low‑C cases

    # -------------------------------------------------
    # Low‑mid C region (13‑29)
    # -------------------------------------------------
    if C < 30:
        if E >= 70 and B > 20:      # high E with modest B → class 4
            return 4
        if B <= 15:                 # very low B → class 3
            return 3
        if B >= 70 and E >= 60:     # high B together with reasonably high E → class 4
            return 4
        return 1

    # -------------------------------------------------
    # Mid C region (30‑45)
    # -------------------------------------------------
    if 30 <= C <= 45:
        if B >= 70 and E >= 80:     # strong B & very high E → class 2
            return 2
        if E >= 80:                 # very high E otherwise → class 4
            return 4
        if D > 70 and E < 30:       # high D with low E → class 3
            return 3
        return 1

    # -------------------------------------------------
    # Upper‑mid C region (46‑60)
    # -------------------------------------------------
    if 46 <= C <= 60:
        if B >= 70 and E >= 80:     # strong B & very high E → class 2
            return 2
        if D > 90:                  # very high D forces class 1
            return 1
        if B >= 70 and E >= 80 and D < 80:
            return 4               # high B/E but not extreme D → class 4
        return 1

    # -------------------------------------------------
    # Default fallback
    # -------------------------------------------------
    return 1