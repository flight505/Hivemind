"""
Predictor 1219
Generated on: 2025-09-10 01:46:44
Accuracy: 52.18%
"""


# PREDICTOR 1219 - Accuracy: 52.18%
# Correct predictions: 5218/10000 (52.18%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A > 45 and B < 25 and C > 35 and E > 50) or
        (A > 50 and B > 80 and C < 20 and E > 60) or
        (A < 20 and B < 25 and C < 20 and D > 50 and E > 70) or
        (A > 45 and B < 10 and C < 5 and D > 60 and E > 65) or
        (A > 50 and B < 15 and C < 5 and E > 60) or
        (A < 45 and B > 90 and C < 5 and E > 75) or
        (A > 60 and B < 25 and C > 75 and D < 30)):
        return 4
    elif (A > 90 and E < 10) or (A > 95 and B > 85 and C < 55 and E < 20):
        return 2
    elif (B < 10 and D > 80) or (A > 40 and B < 25 and C < 20 and E < 25):
        return 3
    else:
        return 1