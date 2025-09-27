"""
Predictor 1031
Generated on: 2025-09-10 01:20:29
Accuracy: 51.95%
"""


# PREDICTOR 1031 - Accuracy: 51.95%
# Correct predictions: 5195/10000 (51.95%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and D > 80) or \
       (A > 80 and B > 70 and E > 70) or \
       (E < 5 and D > 50 and C < 40):
        return 4
    elif (B > 90) or \
         (A < 10 and E > 70) or \
         (A > 40 and B > 90):
        return 2
    elif (B < 10 and D > 80) or \
         (A > 60 and B < 30 and C < 15 and D > 70) or \
         (A < 40 and B > 70 and C > 70 and D > 80 and E < 25) or \
         (E > 90 and C < 50 and D > 50) or \
         (A < 10 and C > 80 and D < 15) or \
         (A < 10 and C < 10 and D > 80 and E < 20) or \
         (A > 50 and D > 50 and E > 90 and C < 50):
        return 3
    else:
        return 1