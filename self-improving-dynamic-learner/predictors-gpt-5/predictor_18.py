"""
Predictor 18
Generated on: 2025-09-09 12:44:12
Accuracy: 42.24%
"""


# PREDICTOR 18 - Accuracy: 42.24%
# Correct predictions: 4224/10000 (42.24%)

def predict_output(A, B, C, D, E):
    # Very low C -> class 3
    if C <= 12:
        return 3

    # Low C (13-25): high E with low D -> 4, otherwise -> 1
    if C <= 25:
        if D <= 30 and E >= 90:
            return 4
        return 1

    # High C (>=78) -> class 2
    if C >= 78:
        return 2

    # Upper-mid C (65-77): low D with high E -> 1, otherwise -> 1
    if 65 <= C < 78:
        if D <= 15 and E >= 70:
            return 1
        return 1

    # Mid C (50-64) -> class 1
    if 50 <= C <= 64:
        return 1

    # Default -> class 1
    return 1