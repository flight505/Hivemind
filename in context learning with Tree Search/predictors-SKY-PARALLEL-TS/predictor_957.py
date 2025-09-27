"""
Predictor 957
Generated on: 2025-09-10 01:09:35
Accuracy: 57.66%
"""


# PREDICTOR 957 - Accuracy: 57.66%
# Correct predictions: 5766/10000 (57.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 50) or \
       (C < 15 and D > 70) or \
       (B > 90 and E > 90) or \
       (C > 50 and D < 30 and E > 40 and B < 60 and A > 20) or \
       (C > 80 and D < 40 and E < 35 and B < 35) or \
       (C < 30 and D < 10 and E > 50 and B < 35):
        return 4
    elif (B > 85 and C > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1