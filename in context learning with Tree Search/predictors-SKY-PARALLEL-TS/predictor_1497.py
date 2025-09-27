"""
Predictor 1497
Generated on: 2025-09-10 02:35:36
Accuracy: 58.43%
"""


# PREDICTOR 1497 - Accuracy: 58.43%
# Correct predictions: 5843/10000 (58.43%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C < 10 and E > 50) or (E < 10 and A < 40 and (D > 70 or C < 20)):
        return 4
    elif (B > 70 and A < 30 and E < 20) or (B > 40 and A < 30 and E > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A > 70 and B < 10 and D > 70 and E < 20):
        return 3
    else:
        return 1