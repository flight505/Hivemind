"""
Predictor 932
Generated on: 2025-09-10 01:07:55
Accuracy: 59.97%
"""


# PREDICTOR 932 - Accuracy: 59.97%
# Correct predictions: 5997/10000 (59.97%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C < 30 and E > 60):
        return 4
    elif (B > 85 and E > 75) or (B > 95):
        return 2
    elif (A > 40 and B > 50 and C < 35 and D > 75) or (A < 15 and B > 40 and C < 15 and D > 40):
        return 3
    elif (A > 50 and B < 10 and C < 25 and D < 5):
        return 3
    else:
        return 1