"""
Predictor 93
Generated on: 2025-09-09 05:28:32
Accuracy: 41.25%
"""


# PREDICTOR 93 - Accuracy: 41.25%
# Correct predictions: 4125/10000 (41.25%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor.
    The rules are ordered from the most specific to the most general
    and are built from the patterns observed in the training data
    together with the newly reported error cases.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # low C with very high D and a decent B → class 4
        if D >= 90 and B > 30:
            return 4
        # low C with very high D (any B) → class 3
        if D >= 90:
            return 3
        return 1

 # 2. Very low D together with low C (<30) → class 4
    # (captures the case where D is extremely small)
    if C < 30 and D < 10:
        return 4

    # 3. High C (≥75)
    if C >= 75:
        # strong B and strong E → class 2
        if B >= 60 and E >= 60:
            return 2
        # otherwise → class 4
        return 4

    # 4. High D and very low E, but only when B is also high
    if D >= 80 and E < 30 and B >= 70:
        return 3

    # 5. Very high E with low C (<30) → class 4
    if C < 30 and E >= 90:
        return 4

    # 6. C in the 20‑30 range – moderate B and moderate‑high E → class 2
    if 20 <= C <= 30:
        if B >= 40 and E >= 60:
            return 2

    # 7. C in the 30‑45 range – decent B and high E → class 2
    if 30 <= C <= 45:
        if B >= 30 and E >= 70:
            return 2
        # very high E even without strong B → class 4
        if E >= 80:
            return 4

    # 8. C in the 45‑60 range – very high B together with very high E → class 4
    if 45 <= C <= 60:
        if B >= 70 and E >= 80:
            return 4

    # 9. Default fallback
    return 1