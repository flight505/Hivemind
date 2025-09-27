"""
Predictor 7
Generated on: 2025-09-09 23:16:45
Accuracy: 53.72%
"""


# PREDICTOR 7 - Accuracy: 53.72%
# Correct predictions: 5372/10000 (53.72%)

def predict_output(A, B, C, D, E):
    if (B - A > 60) or (D - C > 80):
        return 4
    elif (A + B > 150) and (C + D < 50):
        return 2
    elif (B + E > 150) and (A + D < 50):
        return 3
    else:
        return 1