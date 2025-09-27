"""
Predictor 22
Generated on: 2025-09-09 03:50:14
Accuracy: 58.66%
"""


# PREDICTOR 22 - Accuracy: 58.66%
# Correct predictions: 5866/10000 (58.66%)

def predict_output(A, B, C, D, E):
    # 1. Very low C with very high B or very high D → class 4
    if C <= 5 and (B > 80 or D > 80):
        return 4

    # 2. Very high C (≥90) with high B → class 2
    if C >= 90 and B >= 80:
        return 2

    # 3. High C (≥75) – need strong B to move to class 2, otherwise 1
    if C >= 75:
        if B >= 80 and E >= 70:
            return 2
        return 1

    # 4. Moderately high C (≥65) with very high B and E → class 2
    if C >= 65 and B >= 80 and E >= 80:
        return 2

    # 5. High B with mid C and low E → class 4
    if B >= 80 and 20 <= C <= 30 and E < 20:
        return 4

    # 6. Very low B with C in 60‑70 range → class 4
    if B <= 10 and 60 <= C <= 70:
        return 4

    # 7. Low C (≤12) – use E to separate 3 vs 4
    if C <= 12:
        if E >= 60:
            return 4
        return 3

    # 8. High E with mid C and sufficiently high B → class 2
    if E >= 90 and 30 <= C <= 45 and B > 60:
        return 2

    # 9. Default
    return 1