"""
Predictor 1373
Generated on: 2025-09-10 02:16:28
Accuracy: 55.24%
"""


# PREDICTOR 1373 - Accuracy: 55.24%
# Correct predictions: 5524/10000 (55.24%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 50) or (C < 15 and D > 80 and E > 70) or (C > 80 and E < 5) or (B < 25 and E > 50 and C < 35) or (B < 25 and D < 25 and E > 60):
        return 4
    elif (B > 85 and C > 80 and A < 70) or (B > 90 and C < 40 and D > 70) or (B > 70 and E > 80):
        return 2
    elif (B > 80 and C > 80 and D < 5) or (A > 50 and C < 15 and D < 15) or (A > 50 and C < 50 and D > 70) or (D < 15 and C > 40):
        return 3
    else:
        return 1