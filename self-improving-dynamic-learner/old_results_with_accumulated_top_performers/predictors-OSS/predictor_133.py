"""
Predictor 133
Generated on: 2025-09-09 10:50:33
Accuracy: 56.93%
"""


# PREDICTOR 133 - Accuracy: 56.93%
# Correct predictions: 5693/10000 (56.93%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic
    and comparisons. The rules are ordered from most specific
    to most general to capture the error cases while keeping
    the overall logic easy to follow.
    """

    # 1. Very low C (≤ 12)
    if C <= 12:
        # high E forces class 4
        if E >= 60:
            return 4
        # low B forces class 3
        if B <= 15:
            return 3
        # high B together with at least moderate E forces class 4
        if B >= 70 and E >= 30:
            return 4
        # low E (but not very low) also class 3
        if E < 30:
            return 3
        # default for low‑C region
        return 1

    # 2. Low C (13 – 15) – the mid‑low band
    if C <= 15:
        # when B is very high we treat as class 4
        if B >= 70:
            return 4
        return 1

    # 3. Low C (16 – 30) – no special pattern, default to class 1
    if C <= 30:
        return 1

    # 4. Mid C (31 – 45) – handles moderate C values
    if C <= 45:
        # B modest (≤ 60) with high E → class 3
        if B <= 60 and E >= 80:
            return 3
        # B strong (≥ 60) with high E → class 2
        if B >= 60 and E >= 80:
            return 2
        # low E in this range forces class 1
        if E < 30:
            return 1
        return 1

    # 5. High C (≥ 75) – dominant high‑C pattern
    if C >= 75:
        # very low E pushes to class 4
        if E < 30:
            return 4
        # both B and E very high give class 2
        if B >= 80 and E >= 80:
            return 2
        return 1

    # 6. All other cases – default class 1
    return 1