"""
Predictor 75
Generated on: 2025-09-09 04:26:42
Accuracy: 52.13%
"""


# PREDICTOR 75 - Accuracy: 52.13%
# Correct predictions: 5213/10000 (52.13%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
 """

    # 1. Very low C (≤ 12) → class 3
    if C <= 12:
        return 3

    # 2. Low C (13‑30)
    if C <= 30:
        # very high E forces class 4
        if E >= 70:
            return 4
        # moderate‑high E also forces class 4 (covers many 4‑cases)
        if E >= 50:
            return 4
        # when the sum of B and E is small, class 3 seems appropriate
        if (B + E) < 70:
            return 3
        # default for this range
        return 1

    # 3. Mid C (31‑45)
    if C <= 45:
        # very high D together with very high E → class 3
        if D > 90 and E > 80:
            return 3
        # strong B and moderate/high E → class 2
        if B >= 60 and E >= 50:
            return 2
        # very low B → class 
        if B <= 15:
            return 4
        # default
        return 1

    # 4. Upper‑mid C (46‑70)
    if C <= 70:
        # strong B and high E (both ≥ 70) → class 2
        if B >= 60 and E >= 70:
            return 2
        # very low B in this C‑range defaults to class 1
        if B <= 15:
            return 1
        # default
        return 1    # 5. High C (71‑79) – low B with high E gives class 4
    if C < 80:
        if B < 30 and E >= 70:
            return 4
        # otherwise, strong B and high E gives class 2
        if B >= 60 and E >= 70:
            return 2
        # low B and very low E gives class 3
        if B <= 20 and E <= 20:
            return 3
        return 1

    # 6. Very high C (≥ 80)
    # default pattern: high B & high E → class 2, otherwise class 1
    if B >= 60 and E >= 70:
        return 2
    return 1