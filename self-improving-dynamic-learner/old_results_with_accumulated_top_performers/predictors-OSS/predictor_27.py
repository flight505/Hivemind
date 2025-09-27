"""
Predictor 27
Generated on: 2025-09-09 03:52:26
Accuracy: 45.68%
"""


# PREDICTOR 27 - Accuracy: 45.68%
# Correct predictions: 4568/10000 (45.68%)

def predict_output(A, B, C, D, E):
    # 1. Very high C (≥80)
    if C >= 80:
        if E < 20:                     # high C with very low E
            return 4
        if B >= 60 and E >= 60:        # high C with strong B and high E
            return 2
        return 1

    # 2. High C (70‑79)
    if 70 <= C < 80:
        if B >= 60 and E >= 60:
            return 2
        if E < 20:
            return 4
        return 1

    # 3. Mid‑high C (45‑69)
    if 45 <= C < 70:
        if B >= 60:                     # strong B pushes to class 2
            return 2
        if D > 90:                      # very high D tends to class 3
            return 3
        if B <= 15 and E < 20:          # low B and low E → class 3
            return 3
        return 1

    # 4. Low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B with low C → class 3
            return 3
        if E >= 60 and B >= 40:        # moderate‑high B with high E → class 2
            return 2
        return 4                        # other low‑C cases → class 4

    # 5. Very low B (≤10)
    if B <= 10:
        if C >= 30:                     # low B with mid/high C → class 3
            return 3
        return 4                        # very low B & very low C → class 4

    # 6. Low B (≤15) – general fallback
    if B <= 15:
        if C < 20 and E < 40:           # low B, low‑mid C, low E → class 3
            return 3
        return 1

    # 7. High B (≥80) with mid C (30‑45)
    if B >= 80 and 30 <= C <= 45:
        if E < 20:
            return 4
        return 2

    # 8. Very high D (>90) – interact with C
    if D > 90:
        if 40 <= C <= 70:
            return 3
        return 4

    # default
    return 1