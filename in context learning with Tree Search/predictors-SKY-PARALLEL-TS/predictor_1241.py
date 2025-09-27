"""
Predictor 1241
Generated on: 2025-09-10 01:52:29
Accuracy: 35.57%
"""


# PREDICTOR 1241 - Accuracy: 35.57%
# Correct predictions: 3557/10000 (35.57%)

def predict_output(A, B, C, D, E):
    if B > 70 or (C < 20 and D > 80 and E > 50) or E > 80 or C > 90 or (A > 60 and B < 20 and C < 20 and E > 50):
        return 4
    elif (A > 70 and D > 70) or (A > 70 and B < 20) or (D > 80 and E < 10):
        return 3
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    else:
        return 1