"""
Predictor 1263
Generated on: 2025-09-10 01:54:58
Accuracy: 44.84%
"""


# PREDICTOR 1263 - Accuracy: 44.84%
# Correct predictions: 4484/10000 (44.84%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 50) or (A > 60 and E < 10 and C < 30 and B < 25) or (B < 5 and C > 60 and D < 25):
        return 4
    elif (A > 90 and E < 10) or (B > 90 and C > 90) or (A < 10 and B > 90 and E < 5):
        return 2
    elif (B < 10 and D > 80) or (A > 50 and C > 40 and D > 50):
        return 3
    else:
        return 1