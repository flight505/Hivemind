"""
Predictor 1030
Generated on: 2025-09-10 01:20:29
Accuracy: 48.62%
"""


# PREDICTOR 1030 - Accuracy: 48.62%
# Correct predictions: 4862/10000 (48.62%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90 and B > 50) or
        (A > 80 and B > 70) or
        (E < 5 and A < 50 and C < 40 and D > 50) or
        (A > 80 and B < 10 and D > 70 and E < 10)):
        return 4
    elif ((B > 90) or
          (A < 10 and B > 50 and E > 70) or
          (A < 40 and B > 85 and C > 70)):
        return 2
    elif ((B < 30 and C < 15 and D > 70) or
          (B > 80 and C > 70 and D > 80) or
          (C < 10 and D > 80 and B < 50) or
          (E > 90 and D > 50) or
          (C > 80 and D < 15) or
          (A > 50 and B < 50 and C < 50 and D > 50)):
        return 3
    else:
        return 1