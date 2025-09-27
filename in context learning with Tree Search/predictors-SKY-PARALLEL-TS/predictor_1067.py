"""
Predictor 1067
Generated on: 2025-09-10 01:25:44
Accuracy: 53.94%
"""


# PREDICTOR 1067 - Accuracy: 53.94%
# Correct predictions: 5394/10000 (53.94%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (B > 80 and E > 90 and C < 40 and D < 20) or
        (C > 80 and D < 40 and E < 30) or
        (A > 60 and B < 30 and C > 80)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 80 and D > 80 and A > 80) or
          (D < 20 and E > 50 and C > 40 and A < 30 and B > 60)):
        return 2
    elif ((A > 50 and C < 50 and D > 60) or
          (C <= 10 and E < 60 and B < 50) or
          (A > 90 and B < 40) or
          (A < 5 and C < 10)):
        return 3
    else:
        return 1