"""
Predictor 25
Generated on: 2025-09-09 03:51:16
Accuracy: 58.62%
"""


# PREDICTOR 25 - Accuracy: 58.62%
# Correct predictions: 5862/10000 (58.62%)

def predict_output(A, B, C, D, E):
    # 1. Very low B (≤10)
    if B <= 10:
        if C <= 12:                 # low C with very low B → class 3
            return 3
        return 1

    # 2. Very high C (≥80)
    if C >= 80:
        if B <= 10:                 # high C together with very low B → class 4
            return 4
        if B >= 80:
            if E >= 90:             # extremely high E pushes to class 4
                return 4
            if E >= 70:             # high E but not extreme → class 2
                return 2
        return 1

    # 3. Low C (≤12)
    if C <= 12:
        if B <= 15:                 # low B with low C → class 3
            return 3
        if E >= 50:                 # modest E with low C → class 4
            return 4
        return 1

    # 4. High B with low C (C < 20)
    if B >= 80 and C < 20:
        if E < 20:                  # low E keeps class 1
            return 1
        if E >= 60:                 # higher E pushes to class 4
            return 4
        return 2

    # 5. Moderate‑high C (70‑79) with low B → class 1
    if 70 <= C < 80 and B < 40:
        return 1

    # 6. High C (≥70) with modest B and high E → class 4
    if C >= 70 and B < 40 and E >= 70:
        return 4

    # 7. Mid C (30‑45) – high E & moderate B → class 4
    if 30 <= C <= 45:
        if E >= 50 and 30 <= B <= 70:
            return 4
        if E < 20 and D > 70:      # low E but large D → class 3
            return 3

    # 8. Low C region (20‑30) with very high B and very low E → class 4
    if 20 <= C <= 30 and B >= 80 and E < 20:
        return 4

    # 9. High B & very high E with mid C → class 4
    if B >= 70 and E >= 90 and 30 <= C <= 45:
        return 4

    # 10. High B with mid‑range C (40‑50) and moderate E → class 1
    if B >= 80 and 40 <= C <= 50 and E < 70:
        return 1

    # 11. Low C (<20) with modest B and low E → class 3
    if C < 20 and E < 30 and B <= 50:
        return 3

    # default
    return 1