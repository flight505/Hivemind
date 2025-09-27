"""
Predictor 938
Generated on: 2025-09-10 01:07:55
Accuracy: 49.31%
"""


# PREDICTOR 938 - Accuracy: 49.31%
# Correct predictions: 4931/10000 (49.31%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (C < 25 and E > 65 and B > 50) or
        (A < 15 and B > 90 and 30 < C < 40 and D < 35 and E > 75) or
        (A > 60 and B > 80 and C < 50 and D < 40 and E > 90)):
        return 4
    elif ((A < 50 and B > 60 and C > 45 and E > 65) or
          (B > 85 and C > 80) or
          (B > 70 and D < 20 and A < 50 and E > 40)):
        return 2
    elif ((B < 5 or D < 5) or
          (C < 10 and E < 10) or
          (C < 15 and E < 15) or
          (A < 10 and C < 15) or
          (C > 80 and D > 60) or
          (A > 55 and B < 5 and C < 25 and D < 5 and E < 50) or
          (A < 15 and B > 60 and C < 15 and D > 40 and E < 15) or
          (A < 50 and B > 60 and C > 80 and D > 60) or
          (A > 55 and B < 40 and C < 10 and D < 25 and E < 10) or
          (A < 10 and B < 40 and C < 15 and D > 30 and E < 40)):
        return 3
    else:
        return 1