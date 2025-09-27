"""
Predictor 810
Generated on: 2025-09-10 00:50:43
Accuracy: 47.86%
"""


# PREDICTOR 810 - Accuracy: 47.86%
# Correct predictions: 4786/10000 (47.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 80 and E < 20):
        return 4
    elif (A > 90 and E < 10) or (B > 65 and C < 50):
        return 2
    elif (B > 80 and C < 20) or (A > 50 and C < 20) or (B < 10 and D > 80):
        return 3
    else:
        return 1