"""
Predictor 60
Generated on: 2025-09-09 04:19:12
Accuracy: 50.07%
"""


# PREDICTOR 60 - Accuracy: 50.07%
# Correct predictions: 5007/10000 (50.07%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high C with strong B and E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # 2. Low C (<30)
    if C < 30:
        if E >= 70:                     # high E forces class 4 for moderate/high B
            return 4 if B >= 30 else 3   # very low B still class 3
        # when E is not high
        if B <= 10:                     # very low B with low C → class 1
            return 1
        if B <= 15:                     # low B with low C → class 3
            return 3
        return 1                        # default for low C

    # 3. Mid‑low C (30‑45)
    if 30 <= C <= 45:
        if B >= 70 and E >= 70:         # high B & high E → class 4
            return 4
        if B <= 15 and E >= 70:         # low B but high E → class 3
            return 3
        return 1                        # otherwise class 1

    # 4. Mid C (46‑70)
    if 46 <= C <= 70:
        if B >= 70:                     # strong B in this range → class 4
            return 4
        if B <= 20:                     # low B with mid C also tends to class 4
            return 4
        if B <= 15 and E < 30:          # low B with low E → class 3
            return 3
        return 1                        # default

    # 5. High C (71‑74) – treat similarly to very high C but without the strong B/E requirement
    if 71 <= C < 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # 6. Default fallback → class 1
    return 1