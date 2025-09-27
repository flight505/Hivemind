"""
Predictor 1335
Generated on: 2025-09-10 02:07:02
Accuracy: 49.15%
"""


# PREDICTOR 1335 - Accuracy: 49.15%
# Correct predictions: 4915/10000 (49.15%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (E > 55 and (B < 20 or B > 80)) or (C > 70 and D < 10 and E > 50):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    elif (C > 80 and D < 10) or (A > 70 and B < 20) or (B < 10 and D > 80):
        return 3
    else:
        return 1