"""
Predictor 55
Generated on: 2025-09-09 04:12:51
Accuracy: 56.04%
"""


# PREDICTOR 55 - Accuracy: 56.04%
# Correct predictions: 5604/10000 (56.04%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and logical tests.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (≤12) – mainly class 3, unless B is very high and E is high
    if C <= 12:
        if B <= 70:          # low‑to‑moderate B → class 3
            return 3
        # B is high
        if E >= 70:
            return 4         # high E pushes to class 4
        return 1             # otherwise class 1

    # 2. Low C with very high E (class 4)
    if C < 30 and E >= 90:
        return 4

    # 3. Very high C (≥75) – class 2 only when both B and E are high
    if C >= 75:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 4. High C (70‑74) – low E and modest D give class 4, otherwise class 1
    if 70 <= C < 75:
        if E < 40 and D < 50:
            return 4
        return 1

    # 5. Mid C (30‑60) – strong B and high E give class 2,
    #    but very high D overrides to class 1
    if 30 <= C <= 60:
        if D > 90 and B >= 60 and E >= 60:
            return 1                     # high D cancels the “2” rule
        if B >= 60 and E >= 60:
            return 2
        # when C is moderate‑high and both E and D are low → class 4
        if C >= 50 and E < 40 and D < 50:
            return 4
        return 1

    # 6. Moderately high C (60‑70) – low E with low D → class 4
    if 60 <= C < 75:
        if E < 40 and D < 50:
            return 4
        return 1

    # default fallback
    return 1