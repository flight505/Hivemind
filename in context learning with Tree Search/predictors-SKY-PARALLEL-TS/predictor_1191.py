"""
Predictor 1191
Generated on: 2025-09-10 01:43:05
Accuracy: 52.73%
"""


# PREDICTOR 1191 - Accuracy: 52.73%
# Correct predictions: 5273/10000 (52.73%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (D > 60 and E < 15) or
        (D > 50 and E < 10 and C < 90) or
        (B < 10 and C > 70 and A > 80)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 70 and E > 90) or
          (A < 40 and B > 90)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (B < 10 and D > 80) or
          (C < 10 and D > 80 and E < 5) or
          (A < 20 and B > 50 and C < 20 and D > 40)):
        return 3
    else:
        return 1