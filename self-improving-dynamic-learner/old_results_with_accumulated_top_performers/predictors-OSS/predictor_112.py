"""
Predictor 112
Generated on: 2025-09-09 07:43:34
Accuracy: 51.49%
"""


# PREDICTOR 112 - Accuracy: 51.49%
# Correct predictions: 5149/10000 (51.49%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic,
    comparisons and logical tests.  The rules are ordered from
    the most specific to the most general.
    """

    # ------------------------------------------------------------------
    # 1. Very high C (≥75) – strong B & E give class 2
    if C >= 75:
        if B >= 60 and E >= 60:          # typical high‑C / high‑B / high‑E pattern
            return 2
        if B < 40 and E < 30:           # low B & low E together with very high C
            return 4
        return 1

    # ------------------------------------------------------------------
    # 2. High C (60‑74)
    if C >= 60:
        # high B with very low E → class 2  (e.g. (5,99,62,…,1))
        if B >= 80 and E < 20:
            return 2
        # very high E pushes to class 4
        if E >= 80:
            return 4
        # high B with very high E also → class 2
        if B >= 80 and E >= 80:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 3. Mid‑high C (45‑59)
    if C >= 45:
        if B >= 60 and E >= 60:          # strong B & E → class 2
            return 2
        if B >= 30 and E < 40:           # moderate B but low E → class 4
            return 4
        # high D with modest E → class 3  (e.g. (42,84,47,90,32))
        if D > 80 and E < 50:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 4. Mid C (30‑44)
    if C >= 30:
        if B >= 70 and E >= 70:          # strong B & high E → class 2
            return 2
        if E >= 70 and B < 40:           # high E but low B → class 4
            return 4
        if B <= 15:                      # low B → class 3
            return 3
        # very low E in this band → class 4
        if E < 10:
            return 4
        return 1

    # ------------------------------------------------------------------
    # 5. Low C (≤20)
    if C <= 20:
        # very low C with high D forces class 4
        if D > 70:
            return 4
        # very low C (≤12) handling
        if C <= 12:
            # high E pushes to class 4
            if E >= 70:
                return 4
            # strong B and high E → class 2  (e.g. (3,53,10,63,81))
            if B >= 50 and E >= 70:
                return 2
            # low B → class 3
            if B <= 15:
                return 3
            return 1
        # 13‑20 range – default to class 1
        return 1

    # ------------------------------------------------------------------
    # default fallback
    return 1