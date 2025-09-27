"""
Predictor 818
Generated on: 2025-09-10 00:50:43
Accuracy: 47.71%
"""


# PREDICTOR 818 - Accuracy: 47.71%
# Correct predictions: 4771/10000 (47.71%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (D > 60 and E < 15 and B < 10) or
        (B > 85 and E > 80 and C < 40) or
        (C > 70 and D > 60 and E < 10) or
        (E > 80 and C < 35 and D < 20) or
        (B > 80 and C < 20 and D > 50)):
        return 4
    elif ((B > 60 and C > 45 and E > 15) or
          (A > 90 and E < 10)):
        return 2
    elif ((C > 95 and D < 10) or
          (B < 10 and D > 80)):
        return 3
    else:
        return 1