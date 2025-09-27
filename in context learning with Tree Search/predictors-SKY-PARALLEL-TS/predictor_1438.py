"""
Predictor 1438
Generated on: 2025-09-10 02:27:48
Accuracy: 53.07%
"""


# PREDICTOR 1438 - Accuracy: 53.07%
# Correct predictions: 5307/10000 (53.07%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (B > 80 and E > 80) or
        (A > 70 and B < 20 and C > 50) or
        (B > 80 and C < 25)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 80 and E < 35 and A > 60) or
          (A < 10 and B > 65 and E > 70)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (D > 90 and E < 20) or
          (A > 60 and B < 15 and C < 15 and D > 70)):
        return 3
    else:
        return 1