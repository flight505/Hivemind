"""
Predictor 20
Generated on: 2025-09-09 03:48:04
Accuracy: 56.52%
"""


# PREDICTOR 20 - Accuracy: 56.52%
# Correct predictions: 5652/10000 (56.52%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high E with low C → class 4
    if E >= 90 and C < 30:
        return 4

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B + low C → class 3
            return 3
        if E >= 80:                     # low C + very high E → class 4
            return 4
        if E < 30 and B <= 60:         # low C, low‑moderate E and modest B → class 3
            return 3
        return 1                        # other low‑C cases

    # 3. High C (≥75) with high B and decent E → class 2
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # 4. C in the narrow band 28‑30
    if 28 <= C <= 30:
        # high B with moderate E (30‑49) → class 3
        if B > 70 and 30 <= E < 50:
            return 3
        # otherwise fall through to later rules

    # 5. Mid C (30‑40)
    if 30 <= C <= 40:
        if B > 60 and E > 50:           # high B & high E → class 2
            return 2
        if B > 70 and E < 50:           # high B but low E → class 3
            return 3
        return 1

    # 6. Low‑mid C (13‑27)
    if 13 <= C <= 27:
        if B > 70 and E >= 70:          # very high B and high E → class 2
            return 2
        return 1

    # default
    return 1