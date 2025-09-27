"""
Predictor 689
Generated on: 2025-09-10 00:34:06
Accuracy: 56.37%
"""


# PREDICTOR 689 - Accuracy: 56.37%
# Correct predictions: 5637/10000 (56.37%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (E > 80 and C < 30 and A > 60) or (B > 70 and C > 70 and E < 15) or (E < 5 and C > 35 and B > 25):
        return 4
    elif (A < 10 and B > 80 and E > 70) or (E > 90 and D < 20) or (B > 75 and E > 80 and C > 60) or (C > 80 and D < 10):
        return 2
    elif A > 90 and B < 10 and D > 50:
        return 3
    else:
        return 1