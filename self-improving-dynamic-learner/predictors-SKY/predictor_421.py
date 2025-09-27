"""
Predictor 421
Generated on: 2025-09-09 16:27:23
Accuracy: 50.18%
"""


# PREDICTOR 421 - Accuracy: 50.18%
# Correct predictions: 5018/10000 (50.18%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 40 and C < 5:
        return 3
    if B < 15 and E < 10:
        return 3
    if B < 25 and C < 45 and E > 50:
        return 4
    if A > 80 and B < 10 and C < 30:
        return 4
    if E > 90 and C < 25 and B < 50:
        return 4
    if B > 90 and C > 60:
        return 1
    if A < 5 and B > 60 and C > 75:
        return 1
    if B > 90 and C < 50 and A > 80:
        return 2
    if B > 60 and C > 75:
        return 2
    if A < 10 and B > 30 and C > 40:
        return 2
    return 1