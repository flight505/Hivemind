"""
Predictor 678
Generated on: 2025-09-10 00:34:06
Accuracy: 51.19%
"""


# PREDICTOR 678 - Accuracy: 51.19%
# Correct predictions: 5119/10000 (51.19%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (D - C >= 85 and B > 10) or \
       (A > 80 and B < 10 and E < 20) or \
       (C > 90 and D < 20) or \
       (A > 50 and B < 15 and D < 25) or \
       (D < 5 and E > 80):
        return 4
    elif (B > 85 and C > 80) or \
         (A > 90 and E < 10):
        return 2
    elif (B > 50 and C < 25 and D < 20) or \
         (B > 60 and C > 70 and D > 60) or \
         (A > 90 and B < 10 and C < 15 and D > 90):
        return 3
    else:
        return 1