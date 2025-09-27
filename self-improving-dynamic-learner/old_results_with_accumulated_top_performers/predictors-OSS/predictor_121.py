"""
Predictor 121
Generated on: 2025-09-09 09:18:21
Accuracy: 55.70%
"""


# PREDICTOR 121 - Accuracy: 55.70%
# Correct predictions: 5570/10000 (55.70%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor.
    Uses only basic arithmetic, comparisons and logical operators.
    """

    # ------------------------------------------------------------------
    # 1. Very low C (≤ 12) – distinguishes the three low‑C classes.
    if C <= 12:
        if B <= 15:                     # low B with very low C → class 3
            return 3
        if E >= 70:                     # high E pushes to class 4
            return 4
        # other low‑C cases (moderate B, low E) → class 1
        return 1

    # ------------------------------------------------------------------
    # 2. Low C (13 – 29) – high E still forces class 4,
    #    very low B keeps class 3, otherwise class 1.
    if C < 30:
        if E >= 70:
            return 4
        if B <= 15:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 3. Mid C (30 – 59) – strong B & high E give class 2,
    #    otherwise default to class 1.
    if C < 60:
        if B >= 70 and E >= 70:         # clear high‑B / high‑E pattern
            return 2
        return 1

    # ------------------------------------------------------------------
    # 4. High C (60 – 74) – when both B and E are high we use class 2,
    #    very low E together with high C tends to class 4,
    #    otherwise class .
    if C < 75:
        if B >= 60 and E >= 60:
            return 2
        if E < 30:                     # high C but low E → class 4
            return 4
        return 1

    # ------------------------------------------------------------------
    # 5. Very high C (≥ 75) – the dominant pattern in the data.
    #    High B & high E → class 2, otherwise class1.
    if B >= 60 and E >= 60:
        return 2
    return 1