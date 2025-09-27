"""
Predictor 1026
Generated on: 2025-09-10 01:20:29
Accuracy: 56.05%
"""


# PREDICTOR 1026 - Accuracy: 56.05%
# Correct predictions: 5605/10000 (56.05%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 40) or
        (C < 15 and D > 90 and E > 80) or
        (A < 30 and B > 65 and C < 35 and D > 50 and E < 20) or
        (A > 70 and B < 20 and C < 10 and D > 50) or
        (B > 90 and C < 25 and D > 80) or
        (B > 80 and C > 70 and D < 20 and E > 80)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 75 and C > 50 and D > 55 and E < 40) or
          (B > 90 and C < 40 and D > 60)):
        return 2
    elif ((A > 70 and B > 40 and C < 50 and D > 55) or
          (D < 15 and C > 40 and E < 30)):
        return 3
    else:
        return 1