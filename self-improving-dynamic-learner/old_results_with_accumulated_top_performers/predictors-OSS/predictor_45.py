"""
Predictor 45
Generated on: 2025-09-09 04:06:23
Accuracy: 48.98%
"""


# PREDICTOR 45 - Accuracy: 48.98%
# Correct predictions: 4898/10000 (48.98%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    Rules are evaluated from the most specific to the most general.
    """

    # ------------------------------------------------------------------
    # 1. Very low C (≤ 12)
    # ------------------------------------------------------------------
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # low‑moderate E with low C also → class 3
        if E < 30:
            return 3
        # very high E with low C → class 4
        if E >= 80:
            return 4
        # default low‑C case
        return 1

    # ------------------------------------------------------------------
    # 2. Low C (13 – 20)
    # ------------------------------------------------------------------
    if C <= 20:
        # high B + very high E → class 2
        if B >= 70 and E >= 90:
            return 2
        # very high E (but not the high‑B case) → class 4
        if E >= 90:
            return 4
        # low E, high D and moderate B → class 4
        if E < 30 and D > 50 and B > 40:
            return 4
        return 1

    # ------------------------------------------------------------------
    # 3. Mid‑low C (21 – 30)
    # ------------------------------------------------------------------
    if C <= 30:
        if B >= 70 and E >= 90:
            return 2                 # high B & high E → class 2
        if B >= 70 and E < 30:
            return 4                 # high B but low E → class 4
        return 1

    # ------------------------------------------------------------------
    # 4. Mid C (31 – 45)
    # ------------------------------------------------------------------
    if C <= 45:
        if B >= 60 and E >= 70:
            return 2                 # strong B & high E → class 2
        if B >= 80 and E < 30:
            return 4                 # very high B with low E → class 4
        return 1

    # ------------------------------------------------------------------
    # 5. Upper‑mid C (46 – 70)
    # ------------------------------------------------------------------
    if C <= 70:
        # very low B with high C → class 4
        if B <= 10:
            return 4
        # very high B with very low E → class 4
        if B >= 80 and E < 30:
            return 4
        # strong B with moderate‑high C → class 2
        if B >= 60 and C >= 45:
            return 2
        return 1

    # ------------------------------------------------------------------
    # 6. High C (≥ 75)
    # ------------------------------------------------------------------
    if C >= 75:
        # very high B (or strong B & high E) → class 2
        if B >= 80:
            return 2
        if B >= 60 and E >= 70:
            return 2
        return 1

    # ------------------------------------------------------------------
    # Default fallback
    # ------------------------------------------------------------------
    return 1