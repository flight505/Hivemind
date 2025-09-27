"""
Predictor 841
Generated on: 2025-09-10 00:53:24
Accuracy: 54.66%
"""


# PREDICTOR 841 - Accuracy: 54.66%
# Correct predictions: 5466/10000 (54.66%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and max(D, E) > 80 and A > 50) or
        (C > 75 and D < 20 and E > 50) or
        (B < 20 and C > 70 and D < 20 and E > 50) or
        (B > 90 and C < 20 and D > 65) or
        (C > 80 and E < 20 and D > 60 and 30 < B < 40 and A < 60)):
        return 4
    elif ((B > 85 and E > 50) or
          (A < 50 and B > 90 and D > 70)):
        return 2
    elif ((B < 10 and D > 80) or
          (B > 90 and D > 90)):
        return 3
    else:
        return 1