"""
Predictor 1287
Generated on: 2025-09-10 01:58:17
Accuracy: 55.94%
"""


# PREDICTOR 1287 - Accuracy: 55.94%
# Correct predictions: 5594/10000 (55.94%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A < 30 and B < 20 and C > 35 and D > 40 and E < 15) or
        (40 < A < 50 and B > 60 and C < 35 and D > 50 and E > 70) or
        (A < 40 and B > 55 and C > 80 and D < 20) or
        (A < 35 and B > 90 and C < 20 and D > 95) or
        (A > 80 and B < 10 and D > 70) or
        (A > 70 and B > 90 and C < 10 and D > 70) or
        (B > 70 and D < 20 and E > 90 and A > 60) or
        (C > 90 and E < 10 and D > 50) or
        (A > 50 and B < 20 and C < 20 and E > 60)):
        return 4
    elif ((A > 90 and E < 10) or
          (40 < A < 50 and B > 40 and C > 40 and D < 25 and E > 50) or
          (A > 80 and B > 80 and C < 35 and D > 65 and E > 70) or
          (B > 85 and C > 80 and A < 80 and E > 50)):
        return 2
    elif ((B < 10 and D > 80) or
          (A > 50 and C < 50 and D > 70 and B > 40)):
        return 3
    else:
        return 1