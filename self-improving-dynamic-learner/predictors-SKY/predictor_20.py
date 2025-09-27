"""
Predictor 20
Generated on: 2025-09-09 12:17:21
Accuracy: 54.42%
"""


# PREDICTOR 20 - Accuracy: 54.42%
# Correct predictions: 5442/10000 (54.42%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70:
        return 4
    if B < 20 and C > 70 and E < 50:
        return 4
    if C < 35 and B > 60 and D > 70 and E < 40:
        return 4
    if B < 20 and C < 20:
        return 3
    if 40 < B < 60 and 35 < C < 55 and 35 < E < 55:
        return 3
    if B > 60 and C > 45 and E > 80 and D > 70:
        return 3
    if B > 60 and C > 90:
        return 3
    if B > 70 and C < 60 and E < 40:
        return 2
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if B > 80 and C > 40 and E > 40:
        if A > 80 or C > 60:
            return 1
        return 2
    return 1