"""
Predictor 1386
Generated on: 2025-09-10 02:19:06
Accuracy: 52.86%
"""


# PREDICTOR 1386 - Accuracy: 52.86%
# Correct predictions: 5286/10000 (52.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 80 and E > 80 and C < 60):
        return 4
    elif ((B > 75 and C > 60 and E < 60) or (B > 75 and E > 80 and C < 70) or (B > 75 and D > 60 and C < 50) or (A > 90 and E < 10)):
        return 2
    elif (A > 80 and B < 20 and D > 70) or (B < 10 and D > 80):
        return 3
    else:
        return 1