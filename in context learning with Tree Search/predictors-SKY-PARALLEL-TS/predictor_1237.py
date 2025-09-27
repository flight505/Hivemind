"""
Predictor 1237
Generated on: 2025-09-10 01:48:40
Accuracy: 54.41%
"""


# PREDICTOR 1237 - Accuracy: 54.41%
# Correct predictions: 5441/10000 (54.41%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70) or (C < 15 and D > 80) or (B >= 70 and C < 20 and D > 60 and A > 50) or (A > 80 and C < 15 and D > 60) or (C > 55 and E < 5 and D < 40):
        return 4
    elif (B > 80 and C > 40 and E > 10):
        return 2
    elif (A < 40 and B < 60 and C < 15 and D > 60) or (A < 10 and C > 60 and D < 10):
        return 3
    else:
        return 1