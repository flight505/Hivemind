"""
Predictor 1495
Generated on: 2025-09-10 02:35:36
Accuracy: 51.75%
"""


# PREDICTOR 1495 - Accuracy: 51.75%
# Correct predictions: 5175/10000 (51.75%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90 and E > 80) or
        (C < 30 and E < 20 and A < 80) or
        (C > 65 and E < 40 and A < 60) or
        (A > 70 and B < 10 and E < 40) or
        (E < 5 and B > 50 and A < 50)):
        return 4
    elif (B > 90 and E > 80):
        return 2
    elif ((A > 80 and B < 25 and D > 80) or
          (A > 80 and B > 50 and E < 15)):
        return 3
    else:
        return 1