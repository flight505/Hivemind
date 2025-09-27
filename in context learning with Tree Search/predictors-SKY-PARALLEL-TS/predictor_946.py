"""
Predictor 946
Generated on: 2025-09-10 01:07:55
Accuracy: 56.25%
"""


# PREDICTOR 946 - Accuracy: 56.25%
# Correct predictions: 5625/10000 (56.25%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or \
       (C < 15 and D > 80 and B > 30 and A > 5) or \
       (C < 20 and D > 60 and E < 15 and B > 50) or \
       (C > 70 and D > 70 and E < 10 and B > 30):
        return 4
    if (B > 90 and C > 40 and D > 70) or \
       (A < 5 and B > 50 and E > 80):
        return 2
    if (A > 60 and B < 25 and C > 30 and D < 25) or \
       (B > 70 and C < 25 and D > 90) or \
       (A < 10 and B > 85 and C > 70 and D < 10) or \
       (C < 10 and D > 80 and B < 20):
        return 3
    else:
        return 1