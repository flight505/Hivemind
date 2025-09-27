"""
Predictor 85
Generated on: 2025-09-09 04:47:42
Accuracy: 47.95%
"""


# PREDICTOR 85 - Accuracy: 47.95%
# Correct predictions: 4795/10000 (47.95%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general
    and aim to correct the most recent error patterns while keeping
    overall behaviour reasonable.
    """

    # -----------------------------------------------------------------
    # 1. Very high C (≥ 90)
    # -----------------------------------------------------------------
    if C >= 90:
        # very high C with large D and fairly high E → class 3
        if D >= 80 and E > 70:
            return 3
        # very high C with very high B and moderate/low E → class 2
        if B >= 90 and E < 70:
            return 2
        # very high C with very high E → class 4
        if E >= 80:
            return 4
        # default for extreme C
        return 1

    # -----------------------------------------------------------------
    # 2. High C (75 – 89)
    # -----------------------------------------------------------------
    if C >= 75:
        # high E forces class 4
        if E >= 80:
            return 4
        # strong B (≥ 60) gives class 2 even if E is moderate
        if B >= 60:
            return 2
        return 1

    # -----------------------------------------------------------------
    # 3. Mid C (40 – 70)
    # -----------------------------------------------------------------
    if 40 <= C <= 70:
        # very low E with C ≥ 60 → class 4
        if C >= 60 and E < 30:
            return 4
        # low E with lower C (40‑59) → class 2 if B is decent, else 4
        if E < 30:
            if B >= 50:
                return 2
            return 4
        # very high E (≥ 80) → class 4
        if E >= 80:
            return 4
        # very low B (≤ 10) → class 4
        if B <= 10:
            return 4
        return 1

    # -----------------------------------------------------------------
    # 4. Low C (≤ 30)
    # -----------------------------------------------------------------
    if C <= 30:
        # high E (≥ 60) → usually class 4, but very low B gives class 2
        if E >= 60:
            if B <= 5:
                return 2
            return 4
        # very low C (≤ 12) → class 3
        if C <= 12:
            return 3
        return 1

    # -----------------------------------------------------------------
    # default fallback
    # -----------------------------------------------------------------
    return 1