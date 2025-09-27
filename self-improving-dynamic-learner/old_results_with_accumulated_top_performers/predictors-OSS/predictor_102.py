"""
Predictor 102
Generated on: 2025-09-09 06:27:44
Accuracy: 55.72%
"""


# PREDICTOR 102 - Accuracy: 55.72%
# Correct predictions: 5572/10000 (55.72%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and logical tests.
    The conditions are ordered from the most specific to the most general.
    """

    # -------------------------------------------------
    # 1. Very low C (≤ 12)
    # -------------------------------------------------
    if C <= 12:
        # low‑B region → class 3
        if B <= 20:
            return 3
        # high E with low C → class 4
        if E >= 70:
            return 4
        # default for very low C
        return 1

    # -------------------------------------------------
    # 2. Low C (13 – 30)
    # -------------------------------------------------
    if C <= 30:
        # very low B together with high E → class 2
        if B <= 10 and E >= 70:
            return 2
        # high D together with moderate‑high B and moderate E → class 3
        if D >= 70 and B > 50 and E >= 50:
            return 3
        # extremely high E forces class 4
        if E >= 90:
            return 4
        if E >= 70:
            return 4
        # fallback for low‑C region
        return 1

    # -------------------------------------------------
    # 3. Mid C (31 – 45)
    # -------------------------------------------------
    if C <= 45:
        # strong B (very high) → class 2
        if B >= 80:
            return 2
        # very high E: 4 unless D is also very high → class 3
        if E >= 90:
            if D >= 80:
                return 3
            return 4
        # default for this band
        return 1

    # -------------------------------------------------
    # 4. High C (46 – 70)
    # -------------------------------------------------
    if C <= 70:
        # very high E always class 4
        if E >= 90:
            return 4

        # very high C (≥75) with strong B/E → class 2
        if C >= 75:
            if B >= 80:                     # very strong B
                return 2
            if B >= 60 and E >= 60:        # strong B & high E
                return 2
            return 1

        # for 46‑74: high B together with high E → class 2
        if B >= 80 and E >= 70:
            return 2

        # otherwise fall back to class 1
        return 1

    # -------------------------------------------------
    # 5. Very high C (≥ 90)
    # -------------------------------------------------
    if C >= 90:
        # high E with extreme C → class 2
        if E >= 70:
            return 2
        return 1

    # -------------------------------------------------
    # 6. Default fallback
    # -------------------------------------------------
    return 1