"""
Predictor 862
Generated on: 2025-09-09 21:33:22
Accuracy: 47.49%
"""


# PREDICTOR 862 - Accuracy: 47.49%
# Correct predictions: 4749/10000 (47.49%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 80:
        return 4
    if C > 80 and 30 <= B < 50 and E < 50:
        return 4
    if B < 20 and C < 25 and E > 80:
        return 2
    if B < 20 and C < 25:
        return 3
    if 20 <= B < 40 and C > 80 and E < 30:
        return 1
    if B < 20 and C > 70 and E < 30 and D < 20:
        return 3
    if B < 20 and C > 70 and E < 30:
        return 4
    if B > 60 and C > 75 and E >= 70:
        return 2
    if B > 60 and C > 60 and E < 70:
        return 2
    if B > 60 and C < 60 and E < 40:
        return 3
    if 40 <= B <= 60 and C > 70 and E < 30:
        return 3
    return 1