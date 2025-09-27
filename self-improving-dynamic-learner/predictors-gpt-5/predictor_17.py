"""
Predictor 17
Generated on: 2025-09-09 12:43:21
Accuracy: 54.76%
"""


# PREDICTOR 17 - Accuracy: 54.76%
# Correct predictions: 5476/10000 (54.76%)

def predict_output(A, B, C, D, E):
    # Very low C -> class 3
    if C <= 12:
        return 3

    # Low C band (13-25)
    if C <= 25:
        if E >= 90 and D <= 30:
            return 4
        return 1

    # High C with strong B or very low D -> class 2
    if C >= 75:
        if D <= 10 or B >= 80:
            return 2
        return 1

    # Upper-mid C -> class 1
    if C >= 65:
        return 1

    # Mid C -> class 1
    if 50 <= C <= 64:
        return 1

    # Remaining low-mid C: high E with low D -> class 4
    if C < 50 and E >= 90 and D <= 30:
        return 4

    # Default
    return 1