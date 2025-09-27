"""
Predictor 101
Generated on: 2025-09-09 06:27:03
Accuracy: 57.37%
"""


# PREDICTOR 101 - Accuracy: 57.37%
# Correct predictions: 5737/10000 (57.37%)

def predict_output(A, B, C, D, E):
    # 1. Very low C (≤12)
    if C <= 12:
        if E >= 60:            # high E overrules low B
            return 4
        if B <= 15:
            return 3
        return 1

    # 2. Low C (13‑29)
    if C < 30:
        if E >= 70:
            return 4
        if B <= 15:
            return 3
        return 1

    # 3. Mid‑low C (20‑30) – strong B pushes to class 2
    if 20 <= C <= 30:
        if B >= 80:
            return 2
        if E >= 70:
            return 4
        if B <= 15:
            return 3
        return 1

    # 4. Mid C (31‑45)
    if 31 <= C <= 45:
        if B >= 70 and E >= 70:
            return 2
        if B <= 20 and E < 30:
            return 3
        if E >= 70:
            return 4
        return 1

    # 5. Upper‑mid C (46‑60)
    if 46 <= C <= 60:
        if B >= 70 and E >= 70:
            return 2
        if D > 80 and E < 30:          # high D with low E
            return 3
        return 1

    # 6. High‑mid C (61‑70)
    if 61 <= C <= 70:
        if 65 <= C <= 70 and D < 20:   # low D forces class 4
            return 4
        if E < 10:
            return 3
        if B >= 80 and D >= 70 and E >= 70:  # very strong B,D,E
            return 2
        return 1

    # 7. High C (71‑79)
    if 71 <= C <= 79:
        if B >= 60 and E >= 60:
            return 2
        if B >= 80 and E < 40:        # high B but low E → class 4
            return 4
        return 1

    # 8. Very high C (≥80)
    if C >= 80:
        # 75‑85 region with strong B & E → class 2
        if 75 <= C <= 85 and B >= 60 and E >= 60:
            return 2
        return 1

    # default fallback
    return 1