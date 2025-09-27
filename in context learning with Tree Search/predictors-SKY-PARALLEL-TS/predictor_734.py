"""
Predictor 734
Generated on: 2025-09-10 00:41:18
Accuracy: 57.80%
"""


# PREDICTOR 734 - Accuracy: 57.80%
# Correct predictions: 5780/10000 (57.80%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 15 and D > 80) or
        (C < 25 and E > 65 and B > 50) or
        (A > 60 and B < 30 and D > 65 and E < 15) or
        (A > 80 and B < 20 and C > 40 and E < 25) or
        (A > 35 and B > 70 and C < 30 and D > 55 and E < 50) or
        (B > 70 and C < 30 and D > 70)):
        return 4
    elif ((B > 85 and C > 80) or
          (A > 90 and E < 10) or
          (D < 5 and C > 50 and E > 50) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (A < 15 and B > 50 and C < 20 and E > 70)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (B > 80 and D > 90) or
          (A < 40 and B > 90 and D > 90) or
          (C <= 10 and E < 60) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (A < 40 and B > 60 and C < 5 and D > 75) or
          (A > 90 and C > 35 and D > 55 and E > 50) or
          (A > 80 and B < 50 and C < 30 and D > 70 and E > 90)):
        return 3
    else:
        return 1