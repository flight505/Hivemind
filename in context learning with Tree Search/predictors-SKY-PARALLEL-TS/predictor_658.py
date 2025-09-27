"""
Predictor 658
Generated on: 2025-09-10 00:31:36
Accuracy: 49.48%
"""


# PREDICTOR 658 - Accuracy: 49.48%
# Correct predictions: 4948/10000 (49.48%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 80 and D < 20 and E < 40) or (A > 90 and B < 10 and C > 60) or (B > 90 and D > 80):
        return 4
    elif (B > 70 and C < 50 and A > 30) or (A < 5 and E > 60) or (A > 90 and E < 10):
        return 2
    elif (A > 90 and B < 30 and D > 60) or (B < 10 and D > 80):
        return 3
    else:
        return 1