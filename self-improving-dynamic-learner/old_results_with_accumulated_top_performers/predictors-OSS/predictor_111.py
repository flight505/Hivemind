"""
Predictor 111
Generated on: 2025-09-09 07:42:55
Accuracy: 54.73%
"""


# PREDICTOR 111 - Accuracy: 54.73%
# Correct predictions: 5473/10000 (54.73%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic,
    comparisons and logical tests.  The rules are ordered
    from the most specific to the most general.
    """

    # ------------------------------------------------------------------
    # 1. Very high C (≥75) – strong B & E give class 2
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2                     # e.g. rows with C≈78‑84
        # very high C together with low B & low E tends to class 4
        if B < 40 and E < 30:
            return 4
        return 1

    # ------------------------------------------------------------------
    # 2. High C (70‑74)
    if C >= 70:
        if B <= 15 and E < 30:
            return 4                     # low‑B / low‑E corner case
        return 1

    # ------------------------------------------------------------------
    # 3. Mid C (30‑50) – strong B & very high E give class 2
    if 30 <= C <= 50:
        if B >= 60 and E >= 80:
            return 2

    # ------------------------------------------------------------------
    # 4. Very low C (≤12)
    if C <= 12:
        # low B or very high D → class 3
        if B <= 15 or D > 70:
            return 3
        # otherwise a very high E pushes to class 4
        if E >= 70:
            return 4
        return 1

    # ------------------------------------------------------------------
    # 5. Low‑mid C region – high E forces class 4
    if C <= 20 and E >= 60:
        return 4
    if C <= 30 and B <= 15 and E < 20:
        return 4
    if C <= 35 and B <= 15 and E < 20:
        return 4

    # ------------------------------------------------------------------
    # 6. Very high E
    if E >= 90:
        # when D is also very high keep class 1
        if D > 80:
            return 1
        # otherwise high E with not‑extreme C → class 4
        if C < 80:
            return 4
    if E >= 80 and C <= 30:
        return 4

    # ------------------------------------------------------------------
    # 7. High C (≥65) with modest B/E tends to class 4
    if C >= 65 and B < 40 and E < 50:
        return 4

    # ------------------------------------------------------------------
    # 8. Very high D together with low E → class 3
    if D > 80 and E < 30:
        return 3

    # ------------------------------------------------------------------
    # 9. C ≥45 with low B but decent E → class 4
    if C >= 45 and B <= 20 and E >= 60:
        return 4

    # ------------------------------------------------------------------
    # default fallback
    return 1