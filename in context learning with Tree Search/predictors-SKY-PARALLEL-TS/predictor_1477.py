"""
Predictor 1477
Generated on: 2025-09-10 02:33:36
Accuracy: 51.75%
"""


# PREDICTOR 1477 - Accuracy: 51.75%
# Correct predictions: 5175/10000 (51.75%)

def predict_output(A, B, C, D, E):
    if ((A < 20 and B > 70) or
        (C < 15 and D > 90) or
        (B > 80 and C > 60 and E > 70) or
        (A > 55 and B < 20 and C > 45 and D < 20 and E > 65) or
        (A > 95 and C < 10 and D > 50) or
        (A > 40 and B < 15 and C > 40 and D > 45) or
        (C > 95 and D < 40)):
        return 4
    elif ((A < 20 and B > 65 and C < 30 and D < 15 and E > 80) or
          (A < 5 and B < 10 and C < 10 and D > 45 and E > 65) or
          (A > 90 and B > 90 and C < 50 and D > 60)):
        return 2
    elif (A > 90 and B < 15 and C < 40 and D > 85 and E > 80):
        return 3
    else:
        return 1