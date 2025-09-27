"""
Predictor 26
Generated on: 2025-09-09 03:52:01
Accuracy: 56.31%
"""


# PREDICTOR 26 - Accuracy: 56.31%
# Correct predictions: 5631/10000 (56.31%)

def predict_output(A, B, C, D, E):
    # 1. High E together with low C (and not a very low‑B case) → class 4
    if E >= 70 and C < 30 and B > 20:
        return 4

    # 2. Very low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B with very low C → class 3
            return 3
        if E >= 70:                     # otherwise high E pushes to class 4
            return 4
        return 1                        # remaining low‑C cases → class 1

    # 3. Extremely high C with very low D and high E → class 4
    if C >= 90 and D < 20 and E >= 70:
        return 4

    # 4. High C (≥75) – when B and E are both reasonably high → class 2
    if C >= 75:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 5. Mid‑high C (65‑74) – similar rule as above
    if 65 <= C < 75:
        if B >= 60 and E >= 70:
            return 2

    # 6. Very high D together with moderate C and low E → class 3
    if D > 70 and 30 <= C <= 45 and E < 30:
        return 3

    # 7. Low C (≤20) with very low D → class 3
    if C <= 20 and D < 20:
        return 3

    # 8. Moderate C (50‑69) with high B and low D → class 4
    if 50 <= C < 70 and B >= 60 and D < 30:
        return 4

    # 9. Mid C (30‑45) with very high E → class 4
    if 30 <= C <= 45 and E >= 80:
        return 4

    # default fallback
    return 1