"""
Predictor 6
Generated on: 2025-09-09 03:37:39
Accuracy: 41.57%
"""


# PREDICTOR 6 - Accuracy: 41.57%
# Correct predictions: 4157/10000 (41.57%)

def predict_output(A, B, C, D, E):
    # 1. Low B values → class 3
    if B <= 15:
        return 3

    # 2. Very low B with low C and low D → class 3
    if B <= 30 and C < 30 and D < 30:
        return 3

    # 3. High B with high D and low‑mid C → class 4
    if B > 80 and D > 50 and C < 50:
        return 4

    # 4. High D together with low C and moderate B → class 4
    if 60 < B < 90 and D >= 70 and C < 30:
        return 4

    # 5. Very high E → class 4 (unless overridden by later rules)
    if E >= 90:
        return 4

    # 6. High C dominates → usually class 2, with a few exceptions
    if C > 70:
        # exception: when E is also very high, class 1
        if E >= 90:
            return 1
        # exception: when D is high and B is not extreme, class 1
        if D > 70 and B < 80:
            return 1
        # default for high C
        return 2

    # 7. Fallback
    return 1