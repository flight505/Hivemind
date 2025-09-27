"""
Predictor 1201
Generated on: 2025-09-10 01:43:05
Accuracy: 49.04%
"""


# PREDICTOR 1201 - Accuracy: 49.04%
# Correct predictions: 4904/10000 (49.04%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if A < 10:
            return 2
        else:
            return 4
    if A > 70 and C < 10 and E < 45:
        return 3
    if A > 70 and C < 10:
        return 4
    if (B - A > 70) or (D - C > 80) or (C - B > 70) or (D > 65 and C < 15) or (C > 60 and E < 10 and B < 50) or (E > 60 and D < 50 and C < 40 and A > 30) or (A > 50 and B > 60 and E > 65) or (C > 60 and D < 30 and E < 15):
        return 4
    if (A < 20 and D < 5 and E > 70) or (A < 5 and D < 60 and C < 30 and E > 50) or (A < 5 and B > 90 and E > 50) or (A > 50 and B > 60 and E > 70) or (A > 90 and E < 10 and B < 60):
        return 2
    if (D > 80 and E < 20) or (D > 90 and C > 85) or (B < 10 and D > 80):
        return 3
    else:
        return 1