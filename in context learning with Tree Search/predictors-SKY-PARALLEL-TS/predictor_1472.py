"""
Predictor 1472
Generated on: 2025-09-10 02:31:46
Accuracy: 56.41%
"""


# PREDICTOR 1472 - Accuracy: 56.41%
# Correct predictions: 5641/10000 (56.41%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 20) or
        (C < 10 and D > 90) or
        (A > 70 and A < 90 and C < 30 and D > 50) or
        (C > 90 and E < 10) or
        (A > 65 and C < 20 and D > 60) or
        (C < 25 and E > 65 and A > 50)):
        return 4
    elif ((A > 90 and E < 10) or
          (A < 10 and B > 60 and E > 50) or
          (A > 90 and C < 30 and D > 70)):
        return 2
    elif ((B < 10 and D > 80) or
          (A < 10 and B < 10 and C > 70)):
        return 3
    else:
        return 1