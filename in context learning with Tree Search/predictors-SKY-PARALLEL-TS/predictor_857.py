"""
Predictor 857
Generated on: 2025-09-10 00:55:50
Accuracy: 54.65%
"""


# PREDICTOR 857 - Accuracy: 54.65%
# Correct predictions: 5465/10000 (54.65%)

def predict_output(A, B, C, D, E):
    if ((C < 20 and D > 80 and E > 70) or
        (A < 10 and B > 70) or
        (C < 10 and D > 50) or
        (C < 20 and D > 85 and A > 60) or
        (A + B < 50 and C < 15 and D > 55)):
        return 4
    elif (B > 75 and C > 45 and E < 50):
        return 2
    elif ((B >= 75 and D > 80 and E > 80) or
          (A > 80 and B < 20 and C < 20) or
          (A > 40 and B > 70 and C > 40 and D > 80)):
        return 3
    else:
        return 1