"""
Predictor 24
Generated on: 2025-09-09 23:19:12
Accuracy: 55.18%
"""


# PREDICTOR 24 - Accuracy: 55.18%
# Correct predictions: 5518/10000 (55.18%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 20 and D > 50:
        return 4
    if C > 70 and B < 30 and E < 40:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80 and D < 40:
        return 4
    if C > 90 and D > 90:
        return 3
    if A < 5 and C < 10:
        return 3
    if B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    if B > 90:
        return 2
    if A > 90 and E < 10:
        return 2
    if B < 10 and D > 80:
        return 3
    else:
        return 1