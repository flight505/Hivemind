"""
Predictor 86
Generated on: 2025-09-09 23:27:20
Accuracy: 54.49%
"""


# PREDICTOR 86 - Accuracy: 54.49%
# Correct predictions: 5449/10000 (54.49%)

def predict_output(A, B, C, D, E):
    if (A < 20 and B > 65 and C < 50) or (C < 30 and D > 30 and E > 50):
        return 4
    elif (B > 85 and C > 70 and A < 50) or (E > 90 and D < 25):
        return 2
    elif (A > 70 and D > 60) or (E < 10 and D < 40 and A > 40 and B > 35):
        return 3
    else:
        return 1