"""
Predictor 83
Generated on: 2025-09-09 04:46:27
Accuracy: 52.97%
"""


# PREDICTOR 83 - Accuracy: 52.97%
# Correct predictions: 5297/10000 (52.97%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very high C (≥75) – class 2 when B and E are both strong
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:                 # low B with very low C → class 3
            return 3
        if E >= 70:                 # high E pushes to class 4
            return 4
        return 1

    # 3. High D together with low E for mid‑range C (30‑50) → class 3
    if 30 <= C <= 50 and D > 90 and E < 30:
        return 3

    # 4. Low‑mid C (13‑30) – high E forces class 4
    if C <= 30:
        if E >= 60:
            return 4
        return 1

    # 5. Mid C (31‑45)
    if C <= 45:
        if B >= 70 and E >= 80:     # strong B & very high E → class 2
            return 2
        if B <= 15 and E < 30:      # very low B with very low E → class 3
            return 3
        return 1

    # 6. Upper‑mid C (46‑70)
    if C <= 70:
        if E < 30:                  # low E in this band → class 4
            return 4
        if B <= 15:                 # low B
            if E >= 40:
                return 3           # moderate E → class 3
            return 4               # very low E → class 4
        if B < 30 and E >= 40:      # modest B with moderate‑high E → class 3
            return 3
        return 1

    # default fallback
    return 1