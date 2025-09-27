"""
Predictor 82
Generated on: 2025-09-09 04:45:52
Accuracy: 54.15%
"""


# PREDICTOR 82 - Accuracy: 54.15%
# Correct predictions: 5415/10000 (54.15%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and comparisons.
    The rules are evaluated from most specific to most general.
    """

    # 1. Very high C (≥ 90) → class 1
    if C >= 90:
        return 1

    # 2. High C (75 ≤ C < 90) → class 2 when B and E are strong
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # 3. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                     # low B → class 3
            return 3
        # B > 15
        if B > 30 and D > 90:           # moderate‑high B together with very high D
            return 4
        if E >= 80:                     # very high E forces class 4
            return 4
        return 1                        # other low‑C cases

    # 4. Low‑mid C (13 ≤ C ≤ 30)
    if C <= 30:
        # strong B with very high D and very high E → class 3
        if 30 <= B <= 60 and D > 80 and E >= 80:
            return 3
        # very high D (but not extremely high E) → class 1
        if D > 80:
            return 1
        # low B → class 1 (overrides high E)
        if B <= 15:
            return 1
        # high E pushes to class 4
        if E >= 70:
            return 4
        # default for this band → class 3
        return 3

    # 5. Mid C (31 ≤ C ≤ 60)
    if C <= 60:
        if B >= 70:                     # strong B in this range → class 2
            return 2
        return 1

    # default fallback
    return 1