"""
Predictor 1329
Generated on: 2025-09-10 02:07:02
Accuracy: 54.75%
"""


# PREDICTOR 1329 - Accuracy: 54.75%
# Correct predictions: 5475/10000 (54.75%)

def predict_output(A, B, C, D, E):
    if (C > 85 and E < 15) or (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (A < 70 and B > 55 and E < 20 and C > 80):
        return 4
    elif (C > 90 and D < 10 and E > 60) or (B > 40 and C > 60 and D < 10 and E > 50):
        return 2
    elif (A > 90 and D > 80 and C < 40) or (A > 70 and B < 20 and D > 65):
        return 3
    else:
        return 1