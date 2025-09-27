"""
Predictor 10
Generated on: 2025-09-09 17:11:14
Accuracy: 57.49%
"""


# PREDICTOR 10 - Accuracy: 57.49%
# Correct predictions: 5749/10000 (57.49%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if B < 25 and C < 25:
        if E < 50:
            return 3
        else:
            return 1
    if B > 60 and C > 75 and A < 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    return 1