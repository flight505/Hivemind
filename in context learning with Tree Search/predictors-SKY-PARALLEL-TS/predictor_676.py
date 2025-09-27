"""
Predictor 676
Generated on: 2025-09-10 00:34:06
Accuracy: 52.32%
"""


# PREDICTOR 676 - Accuracy: 52.32%
# Correct predictions: 5232/10000 (52.32%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 10 and D > 90 and E > 80) or \
       (B > 70 and C < 5 and D > 90) or \
       (A > 80 and B < 10 and C > 60) or \
       (C > 90 and D < 20) or \
       (B < 15 and A > 50 and D < 25) or \
       (D < 5 and E > 80) or \
       (C < 15 and D > 80 and B > 20):
        return 4
    elif (B > 85 and C > 80) or \
         (A < 20 and B > 90) or \
         (D < 5 and E > 70 and C < 30 and A > 10) or \
         (E > 75 and B > 60 and C < 50):
        return 2
    elif (B > 50 and C < 25 and D < 20) or \
         (B > 60 and C > 70 and D > 60) or \
         (A > 90 and B < 10 and C < 15 and D > 90):
        return 3
    else:
        return 1