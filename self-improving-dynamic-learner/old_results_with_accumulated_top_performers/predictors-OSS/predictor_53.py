"""
Predictor 53
Generated on: 2025-09-09 04:11:55
Accuracy: 53.73%
"""


# PREDICTOR 53 - Accuracy: 53.73%
# Correct predictions: 5373/10000 (53.73%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and logical tests.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high E together with low C → class 4
    if E >= 90 and C < 30:
        return 4

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:                 # low B with very low C → class 3
            return 3
        if E >= 70:                 # high E pushes to class 4
            return 4
        return 1                    # other low‑C cases

    # 3. Low C region (13‑29)
    if C < 30:
        if B >= 70:                 # high B with low‑C
            if E >= 60:             # high E → class 4
                return 4
            return 3                # otherwise class 3 (e.g. B high, E moderate)
        if B <= 20 and E >= 50:     # low‑mid B with decent E → class 2
            return 2
        return 1                    # default for this range

    # 4. Very high C with very low E → class 4
    if C >= 65 and E < 20:
        return 4

    # 5. High C (≥70)
    if C >= 70:
        if B <= 20:                 # low B + high C → class 1
            return 1
        if B >= 70:
            if D > 80:              # high B, high C, very high D → class 3
                return 3
            if E < 20:              # high B, high C, very low E → class 4
                return 4
            return 1                # otherwise class 1
        return 1                    # medium B with high C → class 1

    # 6. Mid‑range C (30‑69)
    if 30 <= C < 70:
        if B >= 70 and E >= 60:     # high B & decent E → class 4
            return 4
        if 20 <= B <= 40 and 35 <= C <= 45 and E >= 50:
            return 2                # medium B, middle C, moderate‑high E → class 2
        return 1                    # default for this range

    # default fallback
    return 1