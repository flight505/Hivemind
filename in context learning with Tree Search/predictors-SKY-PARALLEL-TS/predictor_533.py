"""
Predictor 533
Generated on: 2025-09-10 00:14:11
Accuracy: 55.04%
"""


# PREDICTOR 533 - Accuracy: 55.04%
# Correct predictions: 5504/10000 (55.04%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 15) or \
       (C < 15 and D > 80 and E > 80) or \
       (B > 80 and C < 30 and D > 70 and E > 80) or \
       (C > 60 and D < 25 and E > 80 and A > 70) or \
       (D < 10 and E > 50 and A > 20) or \
       (B < 15 and E < 25) or \
       (A + B > 160 and C < 30 and D > 70):
        return 4
    elif (A < 20 and D < 30 and E > 40 and C < 40) or \
         (C > 60 and D < 25 and E > 80 and A < 70) or \
         (B > 80 and C < 30 and D > 70 and E < 60) or \
         (A > 90 and B > 80 and E < 50):
        return 2
    elif (B < 20 and C < 10) or \
         (B > 60 and D > 90 and E > 80) or \
         (B > 15 and D < 15 and E < 10 and C > 50) or \
         (D > 90 and E < 30) or \
         (B > 80 and C > 60 and D > 90 and E < 20) or \
         (A < 20 and B > 60 and C < 20 and E < 25) or \
         (A > 90 and B < 20 and C > 60):
        return 3
    else:
        return 1