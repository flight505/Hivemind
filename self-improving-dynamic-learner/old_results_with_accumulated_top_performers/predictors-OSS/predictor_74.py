"""
Predictor 74
Generated on: 2025-09-09 04:26:09
Accuracy: 56.84%
"""


# PREDICTOR 74 - Accuracy: 56.84%
# Correct predictions: 5684/10000 (56.84%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # ---- 1. Very low C (≤ 12) ----
    if C <= 12:
        # high E forces class 4 even when B is low
        if E >= 60:
            return 4
        # low B with very low C → class 3
        if B <= 15:
            return 3
        return 1

    # ---- 2. Low C (13‑29) ----
    if C < 30:
        # any relatively high E pushes to class 4
        if E >= 70:
            return 4
        return 1

    # ---- 3. Mid C (30‑45) ----
    if C <= 45:
        # strong B together with high E → class 2
        if B >= 80 and E >= 70:
            return 2
        # very high E (but not enough B for class 2) → class 4
        if E >= 80:
            return 4
        return 1

    # ---- 4. Upper‑mid C (46‑60) ----
    if C <= 60:
        if E >= 70:
            # when D is large treat as class 3, otherwise class 4
            return 3 if D > 50 else 4
        return 1

    # ---- 5. High C (61‑70) ----
    if C <= 70:
        # very strong B and high E → class 2
        if B >= 80 and E >= 70:
            return 2
        # high E with very low D pushes to class 4
        if E >= 70 and D < 20:
            return 4
        return 1

    # ---- 6. Very high C (≥ 71) ----
    if B >= 60 and E >= 60:
        return 2               # typical high‑C, high‑B/E pattern
    return 1                   # default for extreme C