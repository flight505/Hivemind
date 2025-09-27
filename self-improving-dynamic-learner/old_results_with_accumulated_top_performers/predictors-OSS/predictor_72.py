"""
Predictor 72
Generated on: 2025-09-09 04:25:23
Accuracy: 59.41%
"""


# PREDICTOR 72 - Accuracy: 59.41%
# Correct predictions: 5941/10000 (59.41%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high C (dominant class 1)
    if C >= 90:
        return 1

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B
            if E >= 60:                 # high E pushes to class 4
                return 4
            return 3                    # otherwise class 3
        # B > 15
        if E >= 70:
            return 4
        if E >= 60:
            return 4
        return 1

    # 3. Low C (13‑30) – high E forces class 4
    if C < 30:
        if E >= 70:
            return 4
        if E >= 60:
            return 4
        return 1

    # 4. High C (70‑79) with very high E → class 4
    if 70 <= C < 80:
        if E >= 80:
            return 4
        # low B and very low E also → class 4
        if B <= 15 and E < 20:
            return 4
        # otherwise fall through to later rules
        # (moderate cases may be class 2 via rule 8)

    # 5. Mid C (30‑45) – strong B & moderate E → class 2
    if 30 <= C <= 45:
        if B >= 70 and E >= 30:
            return 2
        # very low B with very low E → class 4
        if B <= 15 and E < 20:
            return 4

    # 6. High C (75‑94) – class 2 when B and E are both strong
    if 75 <= C < 95:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 7. Default fallback
    return 1