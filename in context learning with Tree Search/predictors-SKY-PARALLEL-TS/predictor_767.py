"""
Predictor 767
Generated on: 2025-09-10 00:44:16
Accuracy: 52.11%
"""


# PREDICTOR 767 - Accuracy: 52.11%
# Correct predictions: 5211/10000 (52.11%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 80 and B < 15) or (A < 30 and B > 70 and D > 65) or (A > 90 and B > 70 and C < 20 and D > 65) or (A < 50 and B < 10 and C > 50 and E < 10):
        return 4
    elif (B > 70 and C > 90) or (A > 90 and B > 80):
        return 2
    elif (A > 80 and B < 15 and D > 80 and E < 10) or (D > 90 and E < 15):
        return 3
    else:
        return 1