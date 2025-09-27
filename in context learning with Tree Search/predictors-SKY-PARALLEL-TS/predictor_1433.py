"""
Predictor 1433
Generated on: 2025-09-10 02:27:48
Accuracy: 51.27%
"""


# PREDICTOR 1433 - Accuracy: 51.27%
# Correct predictions: 5127/10000 (51.27%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 50) or
        (B > 80 and C < 20 and E > 60) or
        (C > 80 and E < 10) or
        (A > 60 and B < 20 and E < 10) or
        (C > 70 and E < 10) or
        (A > 60 and B < 20 and C < 15) or
        (A < 40 and C > 80)):
        return 4
    elif ((B > 85 and D > 40) or
          (E > 90 and C < 20) or
          (B > 80 and E > 70)):
        return 2
    elif ((A > 50 and D > 70 and B > 30) or
          (C < 10 and E < 60)):
        return 3
    else:
        return 1