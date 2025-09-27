"""
Predictor 1409
Generated on: 2025-09-10 02:24:45
Accuracy: 56.53%
"""


# PREDICTOR 1409 - Accuracy: 56.53%
# Correct predictions: 5653/10000 (56.53%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (A < 50 and B < 40 and C > 65 and D > 55 and E < 5) or
        (50 < A < 60 and B > 60 and C < 35 and E > 85) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 20 and D > 70 and E < 10) or
        (A > 50 and B < 30 and C > 80 and E < 5)):
        return 4
    elif ((B > 85 and C > 80) or
          (A > 90 and E < 10) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (A < 40 and D < 20 and E > 50 and C > 40 and B < 70) or
          (B > 75 and C > 50 and E > 60 and A < 50) or
          (B > 80 and E < 10)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (C < 10 and E < 60) or
          (A > 75 and B < 25 and C < 45 and D > 40) or
          (B > 80 and D > 90 and E < 30) or
          (A < 40 and B > 90 and D > 90) or
          (A > 80 and B < 10 and C < 30 and D > 40) or
          (A > 70 and B < 20 and C < 5 and D > 50 and E < 10) or
          (A > 80 and B < 5 and C < 5 and D > 80) or
          (A < 35 and B > 75 and C > 60 and D > 85 and E < 5) or
          (A > 80 and B < 20 and C > 70 and D < 10) or
          (A < 50 and B < 60 and C > 55 and D > 75 and E > 95) or
          (A < 15 and B < 40 and C > 85 and D < 5 and E < 10) or
          (A < 15 and B > 50 and C > 50 and E < 30 and D < 60)):
        return 3
    else:
        return 1