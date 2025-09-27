"""
Predictor 3
Generated on: 2025-09-09 12:06:39
Accuracy: 56.01%
"""


# PREDICTOR 3 - Accuracy: 56.01%
# Correct predictions: 5601/10000 (56.01%)

def predict_output(A, B, C, D, E):
    # Very small C handling
    if C <= 12:
        if A + B >= 170:
            return 1
        if E >= 55:
            return 4
        return 3

    # Strong pattern for class 2
    if C >= 75 and B >= 65 and A >= 20:
        return 2
    if A <= 35 and A >= 20 and B >= 90 and C >= 65:
        return 2

    # Low D with moderate C -> class 3
    if D <= 12 and C <= 45:
        return 3

    # High E with low D and not-too-high C -> class 4
    if D <= 30 and E >= 70 and C < 70:
        return 4

    # High A with low C and low E -> class 3
    if C < 30 and A >= 80 and E <= 30:
        return 3

    return 1