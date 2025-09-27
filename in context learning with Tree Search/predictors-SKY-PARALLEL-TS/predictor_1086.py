"""
Predictor 1086
Generated on: 2025-09-10 01:28:10
Accuracy: 57.51%
"""


# PREDICTOR 1086 - Accuracy: 57.51%
# Correct predictions: 5751/10000 (57.51%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and D < 50) or (C < 15 and D > 90) or (B > 67 and C > 60 and E > 50 and D < 30 and (A < 20 or C > 80)):
        return 4
    elif A < 50 and C > 65 and ((B > 80 and E < 60) or (D < 10 and B < 70 and E > 20)):
        return 2
    elif (C > 70 and D < 5 and E < 10) or (B < 10 and C < 20 and A < 30):
        return 3
    else:
        return 1