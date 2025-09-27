"""
Predictor 1009
Generated on: 2025-09-10 01:15:51
Accuracy: 39.48%
"""


# PREDICTOR 1009 - Accuracy: 39.48%
# Correct predictions: 3948/10000 (39.48%)

def predict_output(A, B, C, D, E):
    if (C > 80) or (B > 70 and E > 90) or (D > 90 and C < 15) or (C > 80 and E < 10) or (B > 70 and C < 30 and A > 50):
        return 4
    elif (B > 85 and C > 80) or (A < 50 and D < 20 and E > 50):
        return 2
    elif (B > 60 and D > 90 and E > 70) or (B > 50 and C < 10) or (B < 20 and C > 30) or (A > 40 and B > 50 and C < 30):
        return 3
    else:
        return 1