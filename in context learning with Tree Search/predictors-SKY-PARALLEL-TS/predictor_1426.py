"""
Predictor 1426
Generated on: 2025-09-10 02:26:25
Accuracy: 50.42%
"""


# PREDICTOR 1426 - Accuracy: 50.42%
# Correct predictions: 5042/10000 (50.42%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (C < 25 and E > 80) or
        (B > 70 and D > 90) or
        (C < 20 and D > 70 and E > 90) or
        (E < 20 and C > 35 and D > 35) or
        (E > 90 and C > 30)):
        return 4
    elif ((B < 20 and C > 70 and E > 70) or
          (B > 80 and C > 70 and E < 30)):
        return 2
    elif ((B > 70 and C > 70 and D > 80) or
          (A < 10 and B < 20 and C < 30) or
          (A > 30 and B > 70 and C > 70 and E < 25)):
        return 3
    else:
        return 1