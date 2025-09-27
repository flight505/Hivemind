"""
Predictor 1069
Generated on: 2025-09-10 01:25:44
Accuracy: 55.06%
"""


# PREDICTOR 1069 - Accuracy: 55.06%
# Correct predictions: 5506/10000 (55.06%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (40 < A < 50 and C < 40 and D > 70 and E < 10) or
        (A > 50 and B < 10 and C > 40 and D > 60 and E < 10) or
        (A > 70 and B > 80 and C < 70 and D < 30 and E > 70) or
        (60 < A < 70 and B > 50 and C < 10 and D > 90 and E > 80)):
        return 4
    elif ((A > 90 and E < 10) or
          (A > 90 and B > 70 and C < 40 and D > 70 and E < 40) or
          (B > 85 and C > 80 and A < 50)):
        return 2
    elif ((B < 10 and D > 80) or
          (A < 40 and B > 80 and C > 50 and D > 90 and E > 70) or
          (A < 40 and B > 60 and C > 55 and D > 70 and E > 80)):
        return 3
    else:
        return 1