"""
Predictor 684
Generated on: 2025-09-10 00:34:06
Accuracy: 56.46%
"""


# PREDICTOR 684 - Accuracy: 56.46%
# Correct predictions: 5646/10000 (56.46%)

def predict_output(A, B, C, D, E):
    if (D > 40 and ((C < 40 and (B > 60 or E > 60)) or (C > 90 and E < 20))):
        return 4
    if ((A < 10 and C < 15 and E > 70) or (B > 90 and E > 80) or (C > 50 and D < 20 and E > 60 and A < 55)):
        return 2
    if ((A > 75 and D > 60 and E > 70) or (C < 20 and E < 10 and B < 50)):
        return 3
    else:
        return 1