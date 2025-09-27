"""
Predictor 35
Generated on: 2025-09-09 12:27:19
Accuracy: 53.20%
"""


# PREDICTOR 35 - Accuracy: 53.20%
# Correct predictions: 5320/10000 (53.20%)

def predict_output(A, B, C, D, E):
    if C < 35 and E > 70:
        if D > 50:
            return 3
        else:
            return 4
    if B < 50 and C > 50 and D < 50 and E > 20:
        return 4
    if B < 20 and C < 30:
        return 3
    if B > 60 and C > 60:
        if A < 60 and E > 30:
            return 2
        else:
            return 1
    if B > 90 and C > 30:
        return 2
    if 50 < B < 70 and 40 < C < 50 and E < 45:
        return 3
    if A + B > 160 and C < 40 and E < 45:
        return 2
    return 1