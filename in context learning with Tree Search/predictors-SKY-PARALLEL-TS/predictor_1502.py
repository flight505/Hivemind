"""
Predictor 1502
Generated on: 2025-09-10 02:35:36
Accuracy: 54.49%
"""


# PREDICTOR 1502 - Accuracy: 54.49%
# Correct predictions: 5449/10000 (54.49%)

def predict_output(A, B, C, D, E):
    if (D > 90 and C < 40) or (A < 10 and B > 70) or (B > 90 and E > 70) or (B > 65 and E > 70) or (B > 65 and C < 40 and D > 50) or (A > 65 and E > 90) or (C < 15 and E > 80):
        return 4
    elif C > 90 and D < 40:
        return 2
    elif (B > 80 and C > 80 and D > 90 and E < 5) or (A < 10 and B > 90 and D < 25 and E < 20) or (A > 45 and B < 20 and D < 10):
        return 3
    else:
        return 1