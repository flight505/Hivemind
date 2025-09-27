"""
Predictor 838
Generated on: 2025-09-10 00:53:24
Accuracy: 54.16%
"""


# PREDICTOR 838 - Accuracy: 54.16%
# Correct predictions: 5416/10000 (54.16%)

def predict_output(A, B, C, D, E):
    if (B - A > 60 and E < 20) or (D - C > 80):
        return 4
    elif A + B > 120 and E < 20 and B > 80:
        return 2
    elif B > 70 and D > 70:
        return 3
    else:
        return 1