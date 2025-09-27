"""
Predictor 1188
Generated on: 2025-09-10 01:43:05
Accuracy: 58.39%
"""


# PREDICTOR 1188 - Accuracy: 58.39%
# Correct predictions: 5839/10000 (58.39%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (C < 15 and D > 80 and E < 20 and (A >= 30 or B <= 40 or E >= 5)) or
        (C < 25 and E > 65) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (A > 60 and B < 30 and C > 35 and D > 65 and E < 15) or
        (A < 20 and B < 10 and C < 30 and D > 50 and E < 10)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (A < 35 and B > 95 and C > 55 and E < 25) or
          (A > 70 and B > 70 and E > 90)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 30 and B > 40 and C < 10 and D > 80 and E < 5) or
          (A < 20 and B > 50 and C < 20 and D > 40 and E < 40) or
          (A > 85 and B < 10 and C < 10 and D > 80) or
          (B < 10 and D > 80)):
        return 3
    else:
        return 1