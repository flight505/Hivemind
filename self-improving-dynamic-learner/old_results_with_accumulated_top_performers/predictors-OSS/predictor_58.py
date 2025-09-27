"""
Predictor 58
Generated on: 2025-09-09 04:17:54
Accuracy: 55.91%
"""


# PREDICTOR 58 - Accuracy: 55.91%
# Correct predictions: 5591/10000 (55.91%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high C (≥90) – always class 1
    if C >= 90:
        return 1

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:          # low B with very low C → class 3
            return 3
        return 1            # otherwise class 1

    # 3. Low‑to‑moderate C (≤30)
    if C <= 30:
        if E >= 90:          # very high E with low C → class 4
            return 4
        if E >= 70 and B < 70:   # high E and modest B → class 4
            return 4
        return 1            # default for this range

    # 4. High C (≥70)
    if C >= 70:
        if B >= 60 and E >= 60:   # strong B and E with high C → class 2
            return 2
        return 1            # otherwise class 1

    # 5. Mid C (30 < C ≤ 60)
    # At this point C is >30 and ≤60
    if B >= 80 and (D >= 70 or E >= 60):
        return 2            # high B with large D or high E → class 2
    return 1                # default fallback