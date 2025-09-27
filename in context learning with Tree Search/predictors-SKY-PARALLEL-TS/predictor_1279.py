"""
Predictor 1279
Generated on: 2025-09-10 01:58:17
Accuracy: 53.60%
"""


# PREDICTOR 1279 - Accuracy: 53.60%
# Correct predictions: 5360/10000 (53.60%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 85 and C < 15) or (B > 55 and C < 35 and E < 15):
        return 4
    elif (A > 90 and E < 10) or (B > 75 and C > 45 and D > 65):
        return 2
    elif (B > 80 and D > 90 and E > 90) or (A > 40 and B > 60 and C < 35 and D > 70 and E < 5):
        return 3
    else:
        return 1