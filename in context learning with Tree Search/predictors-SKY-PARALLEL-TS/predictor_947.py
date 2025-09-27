"""
Predictor 947
Generated on: 2025-09-10 01:07:55
Accuracy: 49.15%
"""


# PREDICTOR 947 - Accuracy: 49.15%
# Correct predictions: 4915/10000 (49.15%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or \
       (C < 15 and D > 90 and E > 80 and B > 50) or \
       (E < 15 and D > 60 and C < 25) or \
       (C > 70 and D > 70 and E < 10 and B > 50):
        return 4
    elif B > 90 or (A < 5 and E > 80 and D < 70):
        return 2
    elif (B > 80 and C > 70 and D < 10) or \
         (D > 90 and C < 30 and B > 70) or \
         (C < 15 and D > 70 and E < 50) or \
         (A > 60 and B < 25):
        return 3
    else:
        return 1