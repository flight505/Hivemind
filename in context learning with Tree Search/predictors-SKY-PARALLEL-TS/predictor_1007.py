"""
Predictor 1007
Generated on: 2025-09-10 01:15:51
Accuracy: 44.56%
"""


# PREDICTOR 1007 - Accuracy: 44.56%
# Correct predictions: 4456/10000 (44.56%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 50) or (A > 80 and B < 10):
        return 4
    elif B > 90 or (B > 70 and E < 25):
        return 2
    elif C > 90 or (D < 25 and C > 40 and A > 10) or (E < 10 and C < 20 and D > 40) or (C < 15 and D < 15):
        return 3
    else:
        return 1