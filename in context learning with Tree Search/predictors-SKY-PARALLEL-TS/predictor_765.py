"""
Predictor 765
Generated on: 2025-09-10 00:44:16
Accuracy: 54.27%
"""


# PREDICTOR 765 - Accuracy: 54.27%
# Correct predictions: 5427/10000 (54.27%)

def predict_output(A, B, C, D, E):
    if (A < 20 and B > 70) or (C < 15 and D > 90 and E > 80) or (C > 50 and E < 10 and B < 10) or (B > 70 and C < 30 and D > 60) or (A > 90 and B > 70 and C < 20 and D > 60) or (C > 80 and B < 15 and D < 30):
        return 4
    elif (C > 90 and E < 10 and D > 70) or (A > 90 and B > 80):
        return 2
    elif (B > 90 and C > 80 and D > 90 and E < 15) or (A > 70 and B < 20 and C < 10 and D > 60) or (D > 90 and E > 80):
        return 3
    else:
        return 1