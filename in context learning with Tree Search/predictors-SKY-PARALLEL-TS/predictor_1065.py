"""
Predictor 1065
Generated on: 2025-09-10 01:25:44
Accuracy: 48.82%
"""


# PREDICTOR 1065 - Accuracy: 48.82%
# Correct predictions: 4882/10000 (48.82%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (A > 60 and C > 80) or (B < 10 and C > 45 and D > 40):
        return 4
    elif (B > 85 and C > 80) or (A < 50 and B > 70 and E > 80):
        return 2
    elif (A > 45 and C < 50 and D > 60) or (C < 10 and B > 60 and D < 10) or (A > 90 and B < 40 and E < 50):
        return 3
    else:
        return 1