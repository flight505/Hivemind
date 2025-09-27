"""
Predictor 66
Generated on: 2025-09-09 04:22:04
Accuracy: 33.96%
"""


# PREDICTOR 66 - Accuracy: 33.96%
# Correct predictions: 3396/10000 (33.96%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic,
    comparisons and simple logical tests.
    Rules are evaluated from the most specific to the most general.
    """

    # 1. Very high C (≥ 90) → class 2
    if C >= 90:
        return 2

    # 2. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                 # low B with very low C
            return 3
        return 4                    # otherwise very high C‑but‑low‑C cases

    # 3. High C (75–89)
    if C >= 75:
        if B >= 60 and E >= 60:     # strong B and high E
            return 2
        return 1                    # default for high‑C otherwise

    # 4. Mid range C (30–70)
    if 30 <= C <= 70:
        # very low B → class 3  (with tiny D it is still 3)
        if B <= 15:
            return 3

        # high B with very low E → class 1
        if B >= 70 and E < 20:
            return 1

        # high B with high E → class 2
        if B >= 70 and E >= 70:
            return 2

        # very low E (but not covered above) → class 4
        if E < 20:
            return 4

        # low B with modest E and very small D → class 3
        if D < 10 and B <= 30:
            return 3

        # low B with moderate E and very small D → class 3
        if D < 10 and B <= 20 and E < 50:
            return 3

        # default for mid‑range C
        return 4

    # 5. All remaining cases → class 1
    return 1