"""
Predictor 1240
Generated on: 2025-09-10 01:52:29
Accuracy: 40.86%
"""


# PREDICTOR 1240 - Accuracy: 40.86%
# Correct predictions: 4086/10000 (40.86%)

def predict_output(A, B, C, D, E):
    if (D > 80 and E < 10) or (A > 90 and D > 70) or (A > 70 and C < 10) or (B > 90 and E < 15) or (B < 10 and D > 80):
        return 3
    elif (A < 10 and B > 70) or (C < 15) or (E > 80) or (B > 80) or (C > 90 and A < 10) or (A > 60 and B < 20 and C < 20) or (B > 70 and A < 50):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    else:
        return 1