"""
Predictor 868
Generated on: 2025-09-10 00:58:03
Accuracy: 42.70%
"""


# PREDICTOR 868 - Accuracy: 42.70%
# Correct predictions: 4270/10000 (42.70%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (E < 10 and D > 90) or (C > 80) or (D < 5 and E > 70) or (D < 25 and E > 90):
        return 4
    elif (B > 80 and C > 60) or (E > 60 and D < 10) or (B > 90):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (C > 70 and B < 10) or (A > 70 and E > 90):
        return 3
    else:
        return 1