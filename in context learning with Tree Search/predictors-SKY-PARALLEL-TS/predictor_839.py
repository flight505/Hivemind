"""
Predictor 839
Generated on: 2025-09-10 00:53:24
Accuracy: 55.32%
"""


# PREDICTOR 839 - Accuracy: 55.32%
# Correct predictions: 5532/10000 (55.32%)

def predict_output(A, B, C, D, E):
    if (B - A > 60 and E < 20) or (D - C > 80):
        return 4
    elif A < 50 and A + B > 120 and E < 20:
        return 2
    elif B > 70 and D > 70:
        return 3
    else:
        return 1