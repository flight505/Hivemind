"""
Predictor 1439
Generated on: 2025-09-10 02:27:48
Accuracy: 51.75%
"""


# PREDICTOR 1439 - Accuracy: 51.75%
# Correct predictions: 5175/10000 (51.75%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (C < 10 and D > 70) or
        (B > 90 and E > 80) or
        (A > 70 and B < 10 and C > 60 and E < 10) or
        (A > 65 and B < 20 and D > 60 and E < 10) or
        (B > 80 and C < 25) or
        (A > 60 and B < 20 and C < 10 and D > 70)):
        return 4
    elif ((B > 85 and C > 80) or
          (A < 30 and B > 90 and C > 80 and D > 90) or
          (B > 85 and E < 35 and D > 50) or
          (A < 10 and E > 70)):
        return 2
    elif ((A > 50 and B < 20 and D > 60) or
          (B < 10 and D > 80) or
          (A > 60 and C < 15 and D > 70)):
        return 3
    else:
        return 1