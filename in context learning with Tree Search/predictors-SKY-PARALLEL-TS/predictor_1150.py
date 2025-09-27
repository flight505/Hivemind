"""
Predictor 1150
Generated on: 2025-09-10 01:37:38
Accuracy: 54.28%
"""


# PREDICTOR 1150 - Accuracy: 54.28%
# Correct predictions: 5428/10000 (54.28%)

def predict_output(A, B, C, D, E):
    if (C < 20 and E > 70) or (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 70 and C < 20 and E > 70):
        return 4
    elif (B > 80 and C > 80) or (B > 70 and D < 20 and A < 50) or (B > 75 and C < 40 and D > 70):
        return 2
    elif (A > 60 and B < 10) or (C > 90 and E < 5 and D > 80) or (A > 60 and D > 70 and B > 40) or (B > 80 and C > 90 and D > 80 and E < 10) or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1