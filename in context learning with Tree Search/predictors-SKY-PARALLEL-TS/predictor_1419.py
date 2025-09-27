"""
Predictor 1419
Generated on: 2025-09-10 02:26:25
Accuracy: 55.17%
"""


# PREDICTOR 1419 - Accuracy: 55.17%
# Correct predictions: 5517/10000 (55.17%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 15 and (D > 90 or (B > 80 and D > 50))) or
        (B > 70 and E > 70 and D < 30 and C > 50) or
        (A > 80 and E > 70 and D < 35) or
        (A < 10 and E < 10 and D > 40)):
        return 4
    elif ((B > 80 and C > 80) or
          (A > 60 and E < 20 and D > 50 and B > 60)):
        return 2
    elif ((A > 50 and C < 50 and D > 70) or
          (B > 90 and E < 30)):
        return 3
    else:
        return 1