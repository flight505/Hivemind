"""
Predictor 1140
Generated on: 2025-09-10 01:35:54
Accuracy: 44.11%
"""


# PREDICTOR 1140 - Accuracy: 44.11%
# Correct predictions: 4411/10000 (44.11%)

def predict_output(A, B, C, D, E):
    if (C > 95 or
        (A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (B > 90) or
        (C > 60 and E > 80) or
        (E < 10 and B < 50 and A < 60 and C < 30)):
        return 4
    elif ((B > 70 and E > 70) or
          (D < 15 and E > 50)):
        return 2
    elif (B > 70 and C < 10):
        return 3
    else:
        return 1