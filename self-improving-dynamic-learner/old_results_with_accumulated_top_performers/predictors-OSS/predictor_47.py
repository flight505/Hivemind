"""
Predictor 47
Generated on: 2025-09-09 04:08:08
Accuracy: 44.53%
"""


# PREDICTOR 47 - Accuracy: 44.53%
# Correct predictions: 4453/10000 (44.53%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    Rules are evaluated from most specific to most general.
    """

    # 1. Very high C (≥90) with low B → class 1
    if C >= 90 and B < 30:
        return 1

    # 2. Very high C (≥80) together with very high B, very high E and low D → class 4
    if C >= 80 and B >= 80 and E >= 80 and D < 20:
        return 4

    # 3. Class 2 when C is high (≥75) and B and E are both strong
    if C >= 75 and B >= 60 and E >= 70:
        return 2

    # 4. Class 2 for moderate C (20‑35) with high E and decent B
    if 20 <= C <= 35 and E >= 80 and B >= 30:
        return 2

    # 5. Very low C (≤12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # high D together with relatively high E → class 4
        if D > 70 and E > 60:
            return 4
        # otherwise treat as class 3
        return 3

    # 6. Low‑mid C (13‑30) with low B and high D → class 3
    if C <= 30 and B <= 20 and D > 45:
        return 3

    # 7. Very high E (≥90) with low‑moderate C → class 4
    if E >= 90 and C < 30:
        return 4

    # 8. Very high B (≥80) with low C → class 4
    if B >= 80 and C < 30:
        return 4

    # 9. High C (≥80) but insufficient B/E → class 4
    if C >= 80 and (B < 60 or E < 70):
        return 4

    # 10. Mid C (40‑50) with very high D and very high E → class 3
    if 40 <= C <= 50 and D > 60 and E > 80:
        return 3

    # 11. Default fallback → class 1
    return 1