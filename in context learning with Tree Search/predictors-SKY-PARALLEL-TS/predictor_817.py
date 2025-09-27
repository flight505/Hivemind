"""
Predictor 817
Generated on: 2025-09-10 00:50:43
Accuracy: 42.52%
"""


# PREDICTOR 817 - Accuracy: 42.52%
# Correct predictions: 4252/10000 (42.52%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70) or \
       (C < 15 and D > 90) or \
       (B < 5 and D > 60) or \
       (C > 70 and D > 60) or \
       (A > 40 and E > 80 and C < 40) or \
       (A > 60 and E > 80):
        return 4
    elif C > 95 or (B < 10 and D > 80) or (C > 80 and D < 10):
        return 3
    elif (B > 80 and E > 80 and C > 45) or \
         (B > 60 and C > 58 and D > 60) or \
         (A > 90 and E < 10):
        return 2
    else:
        return 1