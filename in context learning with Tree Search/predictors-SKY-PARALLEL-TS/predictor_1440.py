"""
Predictor 1440
Generated on: 2025-09-10 02:27:48
Accuracy: 49.96%
"""


# PREDICTOR 1440 - Accuracy: 49.96%
# Correct predictions: 4996/10000 (49.96%)

def predict_output(A, B, C, D, E):
    if A < 20 and B > 60:
        if C > 65:
            return 2
        else:
            return 4
    elif (C < 20 and D > 80) or (E > 80 and D < 40) or (C > 90 and B < 30) or (A < 20 and B < 20 and C > 40):
        return 4
    elif B > 80 and C > 60:
        return 2
    elif A > 80 and B < 20 and D < 80:
        return 3
    else:
        return 1