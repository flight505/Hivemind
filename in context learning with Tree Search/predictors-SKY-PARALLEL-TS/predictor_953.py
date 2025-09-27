"""
Predictor 953
Generated on: 2025-09-10 01:09:35
Accuracy: 47.29%
"""


# PREDICTOR 953 - Accuracy: 47.29%
# Correct predictions: 4729/10000 (47.29%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 50) or
        (C < 15 and D > 90) or
        (B < 20 and C > 60)):
        return 4
    elif ((D < 20 and E > 60) or
          (B > 90) or
          (B > 70 and C > 75)):
        return 2
    elif ((C < 20 and D < 25 and B > 50) or
          (B < 30 and C < 20 and D > 30)):
        return 3
    else:
        return 1