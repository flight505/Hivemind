"""
Predictor 1428
Generated on: 2025-09-10 02:26:25
Accuracy: 55.55%
"""


# PREDICTOR 1428 - Accuracy: 55.55%
# Correct predictions: 5555/10000 (55.55%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20 and C < 35) or
        (C < 10 and D > 90) or
        (C > 90 and D < 25 and A < 50) or
        (B < 20 and C > 60 and D < 25) or
        (A < 20 and B < 20 and E > 70) or
        (A < 30 and B < 35 and C > 90)):
        return 4
    elif ((B > 75 and C > 90) or
          (B > 90 and C > 75) or
          (B > 90 and E < 25) or
          (A > 90 and E < 10) or
          (A < 10 and B > 70 and C < 15 and D > 80) or
          (A < 10 and B > 60 and C > 60 and E > 70)):
        return 2
    elif ((A > 50 and C < 50 and D > 65 and B > 40 and E > 20) or
          (A < 15 and C > 80 and D < 15) or
          (A < 40 and B > 70 and C < 50 and D > 75) or
          (C <= 10 and E < 60 and B < 80) or
          (B < 25 and C > 80 and D < 10)):
        return 3
    else:
        return 1