"""
Predictor 16
Generated on: 2025-09-09 03:45:57
Accuracy: 42.21%
"""


# PREDICTOR 16 - Accuracy: 42.21%
# Correct predictions: 4221/10000 (42.21%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logic.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (<=12) → class 3 (matches the training rows)
    if C <= 12:
        return 3

    # 2. High C (>=70) – several sub‑cases
    if C >= 70:
        # 2a. Very high C with high E → class 2
        if C > 80 and E >= 70:
            return 2

        # 2b. High C with moderately high B and high E – use D to decide
        if B >= 60 and E >= 70:
            return 2 if D > 60 else 1

        # 2c. High C, low‑moderate B and low E – often class 4,
        #     but when B is in the middle range (45‑60) and E is low,
        #     give class 3 (covers several observed cases)
        if E < 40:
            if 45 <= B <= 60:
                return 3
            return 4

        # default for high C
        return 1

    # 3. Mid‑range C (40‑69)
    if 40 <= C < 70:
        # high B with high E → class 3
        if B > 80 and E > 70:
            return 3
        if B > 60 and E > 70:
            return 3

        # high B with low E → class 4
        if B > 60 and E < 30:
            return 4

        # default for mid C
        return 1

    # 4. Low‑mid C (13‑39)
    if C < 40:
        # high B with very high E → class 4
        if B > 60 and E >= 90:
            return 4

        # high B with moderate E → class 3
        if B > 60 and 30 <= E <= 70:
            return 3

        # low B with very low E → class 4
        if B <= 15 and E < 20:
            return 4

        # default for low‑mid C
        return 1

    # 5. Fallback
    return 1