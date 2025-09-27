"""
Predictor 1369
Generated on: 2025-09-10 02:16:28
Accuracy: 53.54%
"""


# PREDICTOR 1369 - Accuracy: 53.54%
# Correct predictions: 5354/10000 (53.54%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 15 and D > 90) or (A > 90 and C < 20) or (A < 10 and C > 60) or (B > 80 and C > 60 and E > 95):
        return 4
    elif (B > 90 and C > 80) or (B > 70 and C > 90 and E < 5):
        return 2
    elif (B > 70 and C < 20) or (C < 15 and D > 45) or (B > 90 and D > 90):
        return 3
    else:
        return 1