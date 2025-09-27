"""
Predictor 1265
Generated on: 2025-09-10 01:54:58
Accuracy: 51.91%
"""


# PREDICTOR 1265 - Accuracy: 51.91%
# Correct predictions: 5191/10000 (51.91%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (D > 80 and E < 10 and B > 70) or (E < 10 and C < 30 and D > 40):
        return 4
    elif (A > 90 and E < 10 and C < 50) or (B > 90 and C > 40 and E > 40) or (B < 10 and E > 70):
        return 2
    elif (A > 80 and B < 40 and D > 70) or (B < 10 and D > 80) or (A > 40 and C < 30 and D > 70) or (C < 15 and D > 50):
        return 3
    else:
        return 1