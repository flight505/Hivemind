"""
Predictor 29
Generated on: 2025-09-09 03:56:41
Accuracy: 19.47%
"""


# PREDICTOR 29 - Accuracy: 19.47%
# Correct predictions: 1947/10000 (19.47%)

def predict_output(A, B, C, D, E):
    # ----- very high C (>=80) -----
    if C >= 80:
        # very high C + very high B + very high E → class 2
        if B >= 80 and E >= 70:
            return 2
        # very high C + very high B + high D + low‑moderate E → class 3
        if B >= 80 and D > 70 and E < 50:
            return 3
        # very high C + very low B → class 4
        if B <= 20:
            return 4
        # otherwise class 1
        return 1

    # ----- high C (70‑79) -----
    if 70 <= C < 80:
        if B >= 80 and E >= 70:
            return 2
        return 1

    # ----- low C (<=12) -----
    if C12:
        if E >= 60:                     # high E with low C
            return 4
        if E >= 40 and B > 10:          # moderate‑high E with low C
            return 4
        if E < 20:                      # very low E with low C
            return 1
        return 3                        # remaining low‑C cases

    # ----- low‑mid C (13‑19) -----
    if 13 <= C < 20:
        if E < 20:                      # very low E dominates
            return 1
        if D > 70:                      # high D pushes to class 4
            return 4
        if B >= 50 and 30 <= E <= 60:   # moderate E with strong B
            return 3
        return 1

    # ----- mid C (20‑30) -----
    if 20 <= C <= 30:
        if B >= 60 and E >= 50:         # strong B and high E
            return 2
        if B >= 60 and E < 30:          # strong B but low E
            return 4
        return 1

    # ----- C 30‑45 -----
    if 30 <= C <= 45:
        if B >= 60 and E >= 50:         # high B & high E
            return 2
        if B >= 30 and B <= 50 and E < 40:
            return 3
        if B >= 60 and E < 30:          # strong B, low E
            return 4
        return 1

    # ----- C 45‑55 -----
    if 45 <= C <= 55:
        if B < 40 and E < 40:           # both modest
            return 3
        return 1

    # ----- C 56‑70 (mid‑high) -----
    if 56 <= C <= 70:
        if B >= 80 and E >= 30:         # very high B with at least moderate E
            return 2
        return 1

    # default fallback
    return 1