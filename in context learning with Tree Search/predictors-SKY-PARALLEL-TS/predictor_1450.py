"""
Predictor 1450
Generated on: 2025-09-10 02:27:48
Accuracy: 52.99%
"""


# PREDICTOR 1450 - Accuracy: 52.99%
# Correct predictions: 5299/10000 (52.99%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 50 and E < 5) or (B > 90 and C < 40) or (E > 80 and D < 15):
        return 4
    elif (A > 90 and E < 10) or (B > 70 and E < 25 and C < 50) or (A < 30 and D < 25 and E > 50) or (B > 90 and E > 80):
        return 2
    elif B < 10 and D > 80:
        return 3
    else:
        return 1