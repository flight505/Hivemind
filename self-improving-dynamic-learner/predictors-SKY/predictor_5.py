"""
Predictor 5
Generated on: 2025-09-09 12:05:36
Accuracy: 57.07%
"""


# PREDICTOR 5 - Accuracy: 57.07%
# Correct predictions: 5707/10000 (57.07%)

def predict_output(A, B, C, D, E):
    if B < 20 and C > 70 and E < 50:
        return 4
    if C < 32 and E > 60:
        return 4
    if B > 80 and E > 80 and C < 50:
        return 4
    if B > 60 and C < 25 and E < 30 and D > 90:
        return 4
    if B > 60 and C < 40 and E < 40:
        if D > 70:
            return 2
        else:
            return 3
    if B < 50 and C < 40 and E < 60:
        if A > 40 or B > 40:
            return 3
        else:
            return 1
    if A > 80 and E > 80 and C < 50:
        return 3
    if B >= 40 and C > 65 and A < 50 and E > 65:
        return 2
    return 1