"""
Predictor 54
Generated on: 2025-09-09 04:12:11
Accuracy: 52.43%
"""


# PREDICTOR 54 - Accuracy: 52.43%
# Correct predictions: 5243/10000 (52.43%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    Rules are evaluated from most specific to most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        if B <= 15:            # low B with very low C → class 3
            return 3
        if E >= 90:           # very high E with very low C → class 4
            return 4
        return 1

    # 2. Low B (≤15) with moderate C
    if B <= 15:
        if C <= 45:           # low B and not‑very‑low C → class 3
            return 3
        return 1

    # 3. High E together with low C (C < 30) → class 4
    if C < 30 and E >= 90:
        return 4

    # 4. C ≤ 45 and high E (E ≥ 70) → class 4
    if C <= 45 and E >= 70:
        return 4

    # 5. Very high C (≥75)
    if C >= 75:
        if B >= 60:
            if E < 20:               # high C, high B, very low E → class 3
                return 3
            if D < 30:              # high C, high B, low D → class 2
                return 2
        return 1

    # 6. High C (65‑74)
    if 65 <= C < 75:
        if B >= 60 and 70 <= E < 90:  # moderate‑high C with high B and mid‑high E → class 2
            return 2
        return 1

    # 7. Mid C (40‑60)
    if 40 <= C <= 60:
        if B <= 30 and E >= 80:       # low‑mid B but very high E → class 3
            return 3
        if B >= 70 and E >= 40:       # high B and decent E → class 2
            return 2
        return 1

    # 8. C ≤ 30 and very low E (E < 10) → class 4
    if C <= 30 and E < 10:
        return 4

    # 9. Default fallback → class 1
    return 1