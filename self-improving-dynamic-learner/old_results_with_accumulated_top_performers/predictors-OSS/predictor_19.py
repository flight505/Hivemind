"""
Predictor 19
Generated on: 2025-09-09 03:47:33
Accuracy: 42.11%
"""


# PREDICTOR 19 - Accuracy: 42.11%
# Correct predictions: 4211/10000 (42.11%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only arithmetic comparisons.
    The rules are ordered from most specific to most general.
    """

    # Very low C (≤12)
    if C <= 12:
        if B <= 20:               # low B  → class 3
            return 3
        if B > 80:                # very high B  → class 1
            return 1
        return 4                 # otherwise  → class 4

    # Very high C (≥80)
    if C >= 80:
        if B > 80:                # high C + very high B  → class 2
            return 2
        if B <= 30:              # high C + very low B  → class 4
            return 4
        return 1                 # other high‑C cases  → class 1

    # Mid range C (30 ≤ C < 70)
    if 30 <= C < 70:
        # very high E dominates
        if E >= 90:
            return 2

        # high B with low E → class 4
        if B > 80 and E < 50:
            return 4

        # high B with moderate/high E
        if B > 80 and E >= 50:
            # when C is still low (<35) keep class 4, else class 2
            if C < 35:
                return 4
            return 2

        # high B (≥60) with high E (≥60) → class 2
        if B >= 60 and E >= 60:
            return 2

        # middle B / middle E → class 3
        if 30 <= B <= 60 and 30 <= E <= 60:
            return 3

        # low B (≤15) → class 3
        if B <= 15:
            return 3

        # default for this band
        return 1

    # Low‑mid C (13 ≤ C < 30)
    if C < 30:
        if B > 80:
            return 1                     # high B overrules low C
        if B > 50 and E > 60:
            return 2
        if B > 50 and E <= 60:
            return 4
        if B <= 15:
            return 3
        return 1

    # fallback
    return 1