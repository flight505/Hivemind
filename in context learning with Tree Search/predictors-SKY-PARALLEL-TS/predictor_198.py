"""
Predictor 198
Generated on: 2025-09-09 23:36:59
Accuracy: 52.16%
"""


# PREDICTOR 198 - Accuracy: 52.16%
# Correct predictions: 5216/10000 (52.16%)

def predict_output(A, B, C, D, E):
    if (B - A > 60) or (D - C > 80) or (E - D > 30 and B < 25):
        return 4
    elif (A > 80 and E < 10 and C > 30) or (C > 60 and E < 10):
        return 2
    elif (B > 80 and D > 80) or (B < 40 and C < 20 and D > 50):
        return 3
    else:
        return 1