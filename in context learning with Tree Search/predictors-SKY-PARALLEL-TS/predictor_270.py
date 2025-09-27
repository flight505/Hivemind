"""
Predictor 270
Generated on: 2025-09-09 23:43:38
Accuracy: 57.07%
"""


# PREDICTOR 270 - Accuracy: 57.07%
# Correct predictions: 5707/10000 (57.07%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 90 and D < 25) or (C < 30 and E > 90):
        return 4
    elif (B > 75 and C > 79 and A < 50) or (B > 90 and E < 25):
        return 2
    elif (B > 70 and D > 70 and C < 50) or (C > 80 and D < 15):
        return 3
    else:
        return 1