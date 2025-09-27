"""
Predictor 1321
Generated on: 2025-09-10 02:07:02
Accuracy: 55.22%
"""


# PREDICTOR 1321 - Accuracy: 55.22%
# Correct predictions: 5522/10000 (55.22%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 80 and D < 20) or (A > 80 and B < 10 and E > 70) or (A > 70 and E > 80 and D < 40):
        return 4
    elif (B > 80 and C > 90) or (B > 95 and A < 20) or (E > 90 and A < 15 and B < 10):
        return 2
    elif (A < 15 and B < 20 and C < 20) or (A > 90 and B < 5 and C < 10 and D < 5) or (D > 90 and E < 30 and A > 80):
        return 3
    else:
        return 1