"""
Predictor 1015
Generated on: 2025-09-10 01:15:51
Accuracy: 39.89%
"""


# PREDICTOR 1015 - Accuracy: 39.89%
# Correct predictions: 3989/10000 (39.89%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 10 and E < 40) or (E > 90) or (C > 60 and B < 20 and A > 10) or (C > 70 and A > 20):
        return 4
    elif B > 80 and C > 70:
        return 2
    elif B < 5 and A > 50:
        return 3
    else:
        return 1