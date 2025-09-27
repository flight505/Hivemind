"""
Predictor 1215
Generated on: 2025-09-10 01:46:44
Accuracy: 47.23%
"""


# PREDICTOR 1215 - Accuracy: 47.23%
# Correct predictions: 4723/10000 (47.23%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (C > 60 and B < 20) or
        (A > 80 and B > 70) or
        (A > 30 and B < 25 and C > 35 and D < 40 and E < 25) or
        (A > 60 and B < 20 and C > 60 and D < 30 and E < 5) or
        (A > 80 and B > 70 and C < 40 and D < 45 and E > 70)):
        return 4
    elif ((D < 10 and C > 50 and E > 50) or
          (B > 80 and C < 40) or
          (A > 40 and B < 30 and C > 50 and D < 10 and E > 45) or
          (A > 80 and B > 80 and C < 35 and D > 65 and E > 70)):
        return 2
    elif ((A > 90 and E > 90) or
          (A > 90 and B < 40 and C < 50 and D > 60 and E > 95)):
        return 3
    else:
        return 1