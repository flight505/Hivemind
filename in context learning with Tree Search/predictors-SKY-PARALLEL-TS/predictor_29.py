"""
Predictor 29
Generated on: 2025-09-09 23:19:12
Accuracy: 37.60%
"""


# PREDICTOR 29 - Accuracy: 37.60%
# Correct predictions: 3760/10000 (37.60%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (D < 30 and E > 70):
        return 4
    elif (A > 90 and E < 10) or (B > 70 and E < 30 and A > 20) or (B < 20 and E > 40):
        return 2
    elif B < 20 or (B > 50 and C < 30 and A < 60) or D > 90 or A > 90 or (B < 10 and D > 80):
        return 3
    else:
        return 1