"""
Predictor 7
Generated on: 2025-09-09 03:38:05
Accuracy: 39.11%
"""


# PREDICTOR 7 - Accuracy: 39.11%
# Correct predictions: 3911/10000 (39.11%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and logical tests.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high E together with low C  → class 4
    if E >= 80 and C < 30:
        return 4

    # 2. High B (≥ 80)
    if B >= 80:
        # high B + low C is class 1 unless the high‑E condition above applied
        if C < 30:
            return 1
        # high B + mid C (40 – 60) → class 2
        if 40 <= C <= 60:
            return 2
        # otherwise → class 1
        return 1

    # 3. Very low C with modest B (C < 15, B ≤ 30) → class 3
    if C < 15 and B <= 30:
        return 3

    # 4. Low C (C < 20) and not‑high E (E < 50) → class 3
    if C < 20 and E < 50:
        return 3

    # 5. High C (≥ 70)
    #    – if E is also moderately high (≥ 50) → class 4
    #    – otherwise, when B is modest (>30) → class 2, else → class 1
    if C >= 70:
        if E >= 50:
            return 4
        if B > 30:
            return 2
        return 1

    # 6. Very low B (≤ 15) → class 3
    if B <= 15:
        return 3

    # 7. Small D (≤ 10) together with modest C (< 50) → class 3
    if D <= 10 and C < 50:
        return 3

    # 8. Moderate C (55 – 65) together with low D (≤ 40) → class 4
    if 55 <= C <= 65 and D <= 40:
        return 4

    # 9. Mid‑range B and C (40 – 60) with moderate D (50 – 70) → class 3
    if 40 <= B <= 60 and 40 <= C <= 60 and 50 <= D <= 70:
        return 3

    # 10. Default fallback → class 1
    return 1