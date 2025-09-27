"""
Predictor 23
Generated on: 2025-09-09 23:19:12
Accuracy: 48.48%
"""


# PREDICTOR 23 - Accuracy: 48.48%
# Correct predictions: 4848/10000 (48.48%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 80) or (B < 20 and C > 60) or (B < 20 and C < 20 and D > 65) or (A > 70 and E > 90):
        return 4
    elif (B > 80 and E < 20) or (B < 20 and C < 20 and D <= 65) or (D > 90 and C >= 20):
        return 3
    elif A > 90 and E < 10:
        return 2
    else:
        return 1