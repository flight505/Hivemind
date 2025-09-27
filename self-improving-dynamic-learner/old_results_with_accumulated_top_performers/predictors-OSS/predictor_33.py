"""
Predictor 33
Generated on: 2025-09-09 03:59:24
Accuracy: 53.25%
"""


# PREDICTOR 33 - Accuracy: 53.25%
# Correct predictions: 5325/10000 (53.25%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logical tests.
    Rules are ordered from most specific to most general.
    """

    # ---- Specific fixes for the reported error cases ----
    # 1. Moderate C (40‑55) with low B and low E → class 4
    if 40 <= C <= 55 and B <= 20 and E < 30:
        return 4

    # 2. Low C (≤30) with moderate/high B and high E → class 4
    if C <= 30 and B >= 60 and E >= 70:
        return 4

    # 3. Very low C (≤20) with very high B and high E → class 4
    if C <= 20 and B >= 80 and E >= 70:
        return 4

    # 4. Mid‑high C (45‑60) with low E → class 4
    if 45 <= C <= 60 and E < 20:
        return 4

    # 5. Very high C (≥80) with low B → class 4
    if C >= 80 and B <= 10:
        return 4

    # 6. High C (40‑55) with very high B, very high D and modest E → class 3
    if 40 <= C <= 55 and B >= 80 and D > 80 and E < 40:
        return 3

    # 7. Low C (≤12) with very high D → class 4
    if C <= 12 and D > 90:
        return 4

    # 8. Low B (≤15) with moderate C (50‑65) and small D → class 3
    if B <= 15 and 50 <= C <= 65 and D < 20:
        return 3

    # 9. Low B (≤15) with C around 40 and very high E → class 2
    if B <= 15 and 35 <= C <= 45 and E >= 70:
        return 2

    # ---- General patterns derived from top performers ----
    # Very low C region
    if C <= 12:
        if B <= 15:
            return 3                     # low B + very low C
        if E >= 60:
            return 4                     # high E pushes to 4
        return 1

    # High C region (≥75)
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2                     # strong B & E give class 2
        return 1

    # Very high C (≥80) with moderate B/E
    if C >= 80:
        if B <= 10:
            return 4
        if B >= 80:
            if E >= 70:
                return 2
            return 1
        return 1

    # Low B overall
    if B <= 15:
        return 3

    # High B with low C and high E → class 4
    if B >= 90 and E >= 70 and C < 30:
        return 4

    # Default fallback
    return 1