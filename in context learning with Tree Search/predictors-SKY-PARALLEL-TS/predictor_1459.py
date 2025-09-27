"""
Predictor 1459
Generated on: 2025-09-10 02:31:46
Accuracy: 54.54%
"""


# PREDICTOR 1459 - Accuracy: 54.54%
# Correct predictions: 5454/10000 (54.54%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 30 and D > 60) or (B > 65 and E < 5) or (A > 60 and C < 20) or (C > 70 and B > 70 and E < 10):
        return 4
    elif (B > 90 and E < 15) or (C > 80 and D < 15 and E > 80) or (A < 5 and B > 95 and E < 20):
        return 2
    elif (A > 50 and B < 20 and C < 15) or (A > 80 and D > 60 and C < 40) or (A > 70 and B > 40 and D > 50 and C < 40):
        return 3
    else:
        return 1