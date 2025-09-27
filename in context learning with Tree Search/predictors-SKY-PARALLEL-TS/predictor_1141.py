"""
Predictor 1141
Generated on: 2025-09-10 01:35:54
Accuracy: 36.20%
"""


# PREDICTOR 1141 - Accuracy: 36.20%
# Correct predictions: 3620/10000 (36.20%)

def predict_output(A, B, C, D, E):
    if (C > 90 or
        (A < 20 and B > 70) or
        (C < 20 and D > 80) or
        (B > 90) or
        (C > 60 and E > 75) or
        (E < 15 and B < 55 and A < 70 and C < 35) or
        (A > 40 and B > 90 and C < 40)):
        return 4
    elif ((B > 70 and E > 65) or
          (D < 20 and E > 45) or
          (B > 45 and C > 35 and E > 45)):
        return 2
    elif (B > 70 and C < 15) or (A > 15 and B > 70 and D < 25):
        return 3
    else:
        return 1