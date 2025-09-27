"""
Predictor 8
Generated on: 2025-09-09 03:39:06
Accuracy: 42.46%
"""


# PREDICTOR 8 - Accuracy: 42.46%
# Correct predictions: 4246/10000 (42.46%)

def predict_output(A, B, C, D, E):
    # ---- 1. Very high C values (≥80) ----
    if C >= 80:
        if B < 20:          # low B with very high C → class 4
            return 4
        if B >= 30:         # moderate/high B with very high C → class 4
            return 4
        # B between 20‑29 → class 1
        return 1

    # ---- 2. Low B (≤15) ----
    if B <= 15:
        if C < 5:           # extremely low C together with low B → class 3
            return 3
        if D > 70:          # low B but large D → class 1
            return 1
        return 3           # other low‑B cases → class 3

    # ---- 3. Very high E (≥90) ----
    if E >= 90:
        if C < 30 and D < 10:   # high E with low C and tiny D → class 2
            return 2
        return 4                # otherwise high E → class 4

    # ---- 4. Moderate‑high C (≥65) with high B (≥60) and smaller A (<70) → class 2
    if C >= 65 and B > 60 and A < 70:
        return 2

    # ---- 5. Very low E (≤4) with very high B → class 3
    if E <= 4 and B > 80:
        return 3

    # ---- 6. Default ----
    return 1