"""
Predictor 1167
Generated on: 2025-09-10 01:39:40
Accuracy: 49.16%
"""


# PREDICTOR 1167 - Accuracy: 49.16%
# Correct predictions: 4916/10000 (49.16%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and D < 10:
        return 3
    if (A < 10 and B > 70 and D >= 10) or (C < 10 and D > 90) or (A > 80 and D < 30 and E > 70) or (B < 5 and E > 70) or (A > 70 and B < 15) or (C > 80 and D < 25 and E < 15):
        return 4
    if (A > 90 and E < 10) or (B > 75 and C > 50):
        return 2
    if B < 30 and D > 30 and E < 20:
        return 3
    if A > 40 and B < 30 and C > 20 and D < 30 and E < 30:
        return 3
    if A > 40 and B < 5 and D > 30:
        return 3
    else:
        return 1