"""
Predictor 423
Generated on: 2025-09-10 00:02:23
Accuracy: 45.91%
"""


# PREDICTOR 423 - Accuracy: 45.91%
# Correct predictions: 4591/10000 (45.91%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or \
       (C < 15 and D > 70 and E > 85) or \
       (B < 20 and 40 < C < 70) or \
       (D < 20 and E > 50):
        return 4
    elif (C < 15 and D > 70 and E < 85) or \
         (B > 80 and C > 70) or \
         (A > 90 and E < 10):
        return 2
    elif (B < 20 and C > 70) or \
         (A > 80 and D > 75) or \
         (D > 90 and E > 90):
        return 3
    else:
        return 1