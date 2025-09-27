"""
Predictor 1424
Generated on: 2025-09-10 02:26:25
Accuracy: 48.72%
"""


# PREDICTOR 1424 - Accuracy: 48.72%
# Correct predictions: 4872/10000 (48.72%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (E < 20 and C > 30 and D > 30) or
        (C < 25 and D > 60) or
        (C < 20 and E > 90) or
        (C < 30 and D > 55 and E > 80) or
        (A > 80 and E > 90)):
        return 4
    elif (B < 20 and C > 70):
        return 2
    elif ((C > 70 and D > 80) or
          (A < 10 and B < 20 and C < 30)):
        return 3
    else:
        return 1