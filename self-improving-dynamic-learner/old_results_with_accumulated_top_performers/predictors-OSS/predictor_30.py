"""
Predictor 30
Generated on: 2025-09-09 03:57:13
Accuracy: 51.10%
"""


# PREDICTOR 30 - Accuracy: 51.10%
# Correct predictions: 5110/10000 (51.10%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        # high E together with very low C → class 4
        if E >= 70:
            return 4
        # otherwise low C → class 3
        return 3

    # 2. Low‑mid C (13‑20) with high E → class 4
    if C <= 20 and E >= 70:
        return 4

    # 3. Very high C (≥80)
    if C >= 80:
        # low B with very high C → class 1
        if B <= 15:
            return 1
        # high B (≥60) with very high C → class 2
        if B >= 60:
            return 2
        return 1

    # 4. High C (75‑79)
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # 5. Mid‑high C (50‑74)
    if C >= 50:
        # strong B (≥60) → class 2 (even if E is moderate)
        if B >= 60:
            return 2
        # low B (≤20) together with very low E (<10) → class 4
        if B <= 20 and E < 10:
            return 4
        # low B (≤20) with low‑moderate E (<30) → class 4
        if B <= 20 and E < 30:
            return 4
        return 1

    # 6. Mid C (30‑49)
    if C >= 30:
        # low B (≤20) and very low E → class 4
        if B <= 20 and E < 10:
            return 4
        # low B (≤20) and low‑moderate E → class 4
        if B <= 20 and E < 30:
            return 4
        return 1

    # 7. Very low B (≤10) with moderately high C (≥40) → class 4
    if B <= 10 and C >= 40:
        return 4

    # default fallback
    return 1