"""
Predictor 1418
Generated on: 2025-09-10 02:26:25
Accuracy: 54.77%
"""


# PREDICTOR 1418 - Accuracy: 54.77%
# Correct predictions: 5477/10000 (54.77%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 30) or
        (C < 15 and (D > 90 or (B > 80 and D > 50))) or
        (B > 70 and E > 70 and D < 30) or
        (A < 10 and E < 10 and D > 40) or
        (E > 70 and A > 80 and D < 35)):
        return 4
    elif ((B > 80 and C > 80) or
          (A > 60 and E < 20 and D > 50 and B > 60 and C > 30)):
        return 2
    elif ((A > 50 and C < 50 and D > 70) or
          (B > 90 and E < 30)):
        return 3
    else:
        return 1