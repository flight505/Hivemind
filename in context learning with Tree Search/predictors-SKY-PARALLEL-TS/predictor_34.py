"""
Predictor 34
Generated on: 2025-09-09 23:19:12
Accuracy: 51.81%
"""


# PREDICTOR 34 - Accuracy: 51.81%
# Correct predictions: 5181/10000 (51.81%)

def predict_output(A, B, C, D, E):
    if (B - A > 60) or (C < 30 and (D - C > 40)) or (A + E < 20) or (B < 20 and C > 50):
        return 4
    elif (C - D > 80) or (A - E > 80):
        return 2
    elif (A + D > 130 and B + C < 100 and B > 40) or (A + D + E < 80):
        return 3
    else:
        return 1