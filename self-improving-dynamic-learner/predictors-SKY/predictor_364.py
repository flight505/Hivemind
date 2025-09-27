"""
Predictor 364
Generated on: 2025-09-09 15:52:07
Accuracy: 55.18%
"""


# PREDICTOR 364 - Accuracy: 55.18%
# Correct predictions: 5518/10000 (55.18%)

def predict_output(A, B, C, D, E):
    if B < 20:
        if C < 13:
            return 3
        elif C > 30 and D > 25 and E < 50:
            return 4
        elif C > 50 and D < 20:
            return 3
        else:
            return 1
    if C > 80 and E > 80 and B < 30 and D < 20:
        return 4
    if B > 60 and C > 75 and E > 70:
        return 2
    if C < 25 and E > 80 and B > 20:
        return 4
    if B > 60 and C > 80 and E < 30:
        return 4
    if B > 62 and C < 20 and A < 60:
        return 4
    return 1