"""
Predictor 590
Generated on: 2025-09-10 00:22:13
Accuracy: 57.58%
"""


# PREDICTOR 590 - Accuracy: 57.58%
# Correct predictions: 5758/10000 (57.58%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 35) or
        (C < 10 and D > 90) or
        (C > 70 and B < 15 and D < 30) or
        (E > 90 and C < 30) or
        (A < 10 and E > 80 and B < 15 and C < 5)):
        return 4
    elif B > 85 and C > 80:
        return 2
    elif ((A > 80 and B < 35 and C < 45 and D > 90) or
          (A > 85 and D > 90 and C < 30) or
          (A > 50 and B < 40 and C < 10 and E < 10) or
          (B > 60 and D > 70 and C < 35 and E < 5)):
        return 3
    else:
        return 1