"""
Predictor 1447
Generated on: 2025-09-10 02:27:48
Accuracy: 53.45%
"""


# PREDICTOR 1447 - Accuracy: 53.45%
# Correct predictions: 5345/10000 (53.45%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70 and E < 20) or (C < 15 and D > 80) or (C > 90 and E < 10) or (B > 70 and C < 20 and (D > 40 or E < 50)):
        return 4
    elif (C > 80 and B < 20) or (A > 80 and B < 30 and D > 70):
        return 3
    elif (B > 80 and E > 80) or (B > 40 and E > 70 and D < 20 and C < 40):
        return 2
    else:
        return 1