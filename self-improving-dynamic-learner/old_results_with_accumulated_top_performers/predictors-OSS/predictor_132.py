"""
Predictor 132
Generated on: 2025-09-09 10:50:10
Accuracy: 47.27%
"""


# PREDICTOR 132 - Accuracy: 47.27%
# Correct predictions: 4727/10000 (47.27%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                     # low B with very low C → class 3
            return 3
        if E >= 70:                    # high E overrides low‑C rule
            return 4
        if E >= 50:                    # moderate‑high E also forces class 4
            return 4
        return 1                       # other low‑C cases → class 1

    # 2. Moderate low C (≤ 20) with high E and B not very low
    if C <= 20 and E >= 70 and B > 15:
        return 4

    # 3. Very high C (≥ 75) together with high E → class 2
    if C >= 75 and E >= 70:
        return 2

    # 4. High C (≥ 85) with not‑high E → class 4
    if C >= 85 and E < 70:
        return 4

    # 5. Very high C (≥ 80) together with very strong B (≥ 80) → class 2
    if B >= 80 and 40 <= C <= 49:
        return 2

    # 6. Strong B with mid‑low C → class 4
    if B >= 70 and 20 <= C <= 30 and D < 80:
        return 4

    # 7. Mid C (35‑45) with moderate B (20‑40) → class 4
    if 35 <= C <= 45 and 20 <= B <= 40:
        return 4

    # 8. C around 40‑45 with very high E and high D → class 3
    if 40 <= C <= 45 and E >= 90 and D >= 70:
        return 3

    # 9. Very low B (≤ 15) with C in 45‑55 → class 3
    if B <= 15 and 45 <= C <= 55:
        return 3

    # 10. Default fallback
    return 1