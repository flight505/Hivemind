"""
Predictor 353
Generated on: 2025-09-09 15:44:15
Accuracy: 51.53%
"""


# PREDICTOR 353 - Accuracy: 51.53%
# Correct predictions: 5153/10000 (51.53%)

def predict_output(A, B, C, D, E):
    if B >= 60 and C > 75 and E > 60:
        return 2
    if C > 90 and E < 30:
        return 4
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 60 and C > 10 and C < 50 and E < 50:
        return 4
    if C < 25 and E > 90 and B > 20:
        return 4
    if B < 10 and C > 40 and E < 40:
        return 4
    if C > 30 and E < 5:
        return 4
    if B > 80 and C < 20 and E < 10:
        return 4
    if B < 20 and C < 15 and A > 90:
        return 1
    if B < 20 and C < 15:
        return 3
    if B > 50 and C < 10 and E < 10:
        return 3
    return 1