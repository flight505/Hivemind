"""
Predictor 355
Generated on: 2025-09-09 23:51:59
Accuracy: 56.14%
"""


# PREDICTOR 355 - Accuracy: 56.14%
# Correct predictions: 5614/10000 (56.14%)

def predict_output(A, B, C, D, E):
    if ((B - A > 60 and E < 20) or
        (D - C > 80 and E > 80) or
        (C - B > 50 and E < 5) or
        (A - B > 70 and C < 15) or
        (B - D > 50 and C > 60 and E > 70) or
        (A < 10 and B > 70) or
        (C < 15 and D > 80)):
        return 4
    if ((E - A > 80 and B < 60 and C < 20) or
        (B > 90 and E > 85 and C < 60) or
        (B > 85 and C > 80)):
        return 2
    if ((C - A > 20 and D < 25 and (E - B > 30)) or
        (D > 90 and B > 80 and C < 40 and E < 40) or
        (A > 50 and C < 50 and D > 70)):
        return 3
    else:
        return 1