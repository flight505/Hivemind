"""
Predictor 70
Generated on: 2025-09-09 23:24:50
Accuracy: 56.79%
"""


# PREDICTOR 70 - Accuracy: 56.79%
# Correct predictions: 5679/10000 (56.79%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 85 and C < 10:
        return 2
    if (A < 10 and B > 70) or (C < 15 and D > 55 and B > 20) or (C < 25 and E > 70) or (B > 75 and D > 80) or (E > 80 and B < 30 and D < 40):
        return 4
    if (A > 90 and E < 10 and C < 20) or (B > 85 and C > 80):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (B > 70 and D < 20 and C > 30) or (A < 15 and C < 20 and D > 65):
        return 3
    else:
        return 1