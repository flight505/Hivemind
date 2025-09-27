"""
Predictor 23
Generated on: 2025-09-09 03:50:31
Accuracy: 46.75%
"""


# PREDICTOR 23 - Accuracy: 46.75%
# Correct predictions: 4675/10000 (46.75%)

def predict_output(A, B, C, D, E):
    # 1. Very high C together with very high E → class 4
    if C >= 80 and E >= 90:
        return 4

    # 2. Very high C with high B – decide by E
    if C >= 90 and B >= 80:                 # overrides rule 1 when E < 90
        return 2 if E >= 80 else 1

    # 3. High C (≥75) with very high B – split by E
    if C >= 75 and B >= 80:
        if E >= 70:
            return 2
        if E < 30:
            return 3
        return 1

    # 4. High C (≥70) with low‑mid B and high E → class 4
    if C >= 70 and B < 30 and E >= 70:
        return 4

    # 5. Mid‑high C (≥65) with very high B and very high E → class 2
    if C >= 65 and B >= 80 and E >= 80:
        return 2

    # 6. Very low C (≤5) with strong B or D → class 4
    if C <= 5 and (B > 80 or D > 80):
        return 4

    # 7. Low C (≤12) – separate by E
    if C <= 12:
        return 4 if E >= 50 else 3

    # 8. Low C (<30) with low B and high E → class 4
    if C < 30 and B <= 20 and E >= 60:
        return 4

    # 9. C in 20‑30 range, low‑mid B, very low E → class 4
    if 20 <= C <= 30 and B <= 40 and E < 30:
        return 4

    # 10. C in 30‑45 range, very low B, high E → class 2
    if 30 <= C <= 45 and B <= 15 and E >= 60:
        return 2

    # 11. C in 30‑45 range, very high E but moderate B → class 3
    if 30 <= C <= 45 and E >= 90 and B <= 60:
        return 3

    # 12. C in 40‑50 range with very high D → class 3
    if 40 <= 50 and D > 80:
        return 3

    # 13. Very low B with mid‑high C → class 4
    if B <= 10 and 60 <= C <= 70:
        return 4

    # default
    return 1