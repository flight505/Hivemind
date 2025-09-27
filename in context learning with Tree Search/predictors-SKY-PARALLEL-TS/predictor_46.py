"""
Predictor 46
Generated on: 2025-09-09 23:21:45
Accuracy: 59.58%
"""


# PREDICTOR 46 - Accuracy: 59.58%
# Correct predictions: 5958/10000 (59.58%)

def predict_output(A, B, C, D, E):
    if A < 15 and B > 70 and E < 20:
        return 4
    if C <= 20 and (D > 55 or E > 75):
        return 4
    if B > 85 and C > 80:
        return 2
    if A > 90 and E < 10:
        return 2
    if D < 15 and C > 80:
        return 3
    if A < 15 and D < 15:
        return 3
    if C < 10 and B < 50:
        return 3
    else:
        return 1