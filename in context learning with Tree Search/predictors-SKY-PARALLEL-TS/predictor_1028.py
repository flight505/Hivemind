"""
Predictor 1028
Generated on: 2025-09-10 01:20:29
Accuracy: 52.78%
"""


# PREDICTOR 1028 - Accuracy: 52.78%
# Correct predictions: 5278/10000 (52.78%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and D > 80 and E > 50) or \
       (A > 80 and B > 70 and C < 40 and E > 70) or \
       (E < 5 and D > 50 and C > 30 and A < 50):
        return 4
    elif (A > 90 and E < 10) or \
         (B > 90) or \
         (A < 10 and E > 70 and D < 20):
        return 2
    elif (B < 10 and D > 80) or \
         (A > 60 and B < 30 and C < 15 and D > 70) or \
         (A < 40 and B > 70 and C > 70 and D > 80 and E < 25) or \
         (E > 90 and C < 50 and D > 50) or \
         (A < 10 and C > 80 and D < 15) or \
         (A < 10 and C < 10 and D > 80 and E < 20):
        return 3
    else:
        return 1