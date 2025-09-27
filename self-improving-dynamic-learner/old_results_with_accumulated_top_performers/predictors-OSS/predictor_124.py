"""
Predictor 124
Generated on: 2025-09-09 09:23:28
Accuracy: 56.89%
"""


# PREDICTOR 124 - Accuracy: 56.89%
# Correct predictions: 5689/10000 (56.89%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons
    and logical operators.  The rules are ordered from the most
    specific to the most general and aim to correct the previously
    mis‑predicted cases while keeping good overall performance.
    """

    # ------------------------------------------------------------------
    # 0. Very low D overrides to class 1 (covers rare low‑D cases)
    if D < 10:
        return 1

    # ------------------------------------------------------------------
    # 1. Very high C (>= 90) – dominant class 1
    if C >= 90:
        return 1

    # ------------------------------------------------------------------
    # 2. Very low C (<= 12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # strong B and high E → class 2
        if B >= 60 and E >= 60:
            return 2
        # very high D together with low C → class 4
        if D > 80:
            return 4
        # high E also forces class 4
        if E >= 70:
            return 4
        # default for low‑C region
        return 1

    # ------------------------------------------------------------------
    # 3. Low C (13‑20)
    if C <= 20:
        if E >= 70:
            return 4
        if B <= 15:          # very low B still class 3
            return 3
        return 1

    # ------------------------------------------------------------------
    # 4. Mid‑low C (21‑30)
    if C <= 30:
        if E >= 70:
            return 4
        if E < 10:           # extremely low E → class 3
            return 3
        return 1

    # ------------------------------------------------------------------
    # 5. C in the 31‑45 range
    if C <= 45:
        # high B with very low E → class 4
        if B >= 80 and E < 30:
            return 4
        # any high E (>=70) pushes to class 4
        if E >= 70:
            return 4
        # high B with moderate E (30‑69) → class 3
        if B >= 80 and 30 <= E < 70:
            return 3
        # both B and E high (>=70) → class 2
        if B >= 70 and E >= 70:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 6. C in the 46‑60 range
    if C <= 60:
        # strong B and strong E → class 2
        if B >= 60 and E >= 60:
            return 2
        # low E (<40) keeps it at class 1
        if E < 40:
            return 1
        return 1

    # ------------------------------------------------------------------
    # 7. C in the 61‑70 range
    if C <= 70:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 8. C in the 71‑89 range
    if C < 90:
        # very strong B together with very strong E → class 2
        if B >= 80 and E >= 80:
            return 2
        return 1

    # ------------------------------------------------------------------
    # Default fallback
    return 1