"""
Predictor 843
Generated on: 2025-09-10 00:53:24
Accuracy: 51.30%
"""


# PREDICTOR 843 - Accuracy: 51.30%
# Correct predictions: 5130/10000 (51.30%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (C > 70 and D < 20 and E > 20) or
        (C > 70 and E < 20 and D > 50 and A < 70) or
        (B > 90 and C < 20)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 85 and C > 80) or
          (B > 90 and C < 40)):
        return 2
    elif ((B < 10 and D > 80) or
          (B > 90 and D > 90)):
        return 3
    else:
        return 1