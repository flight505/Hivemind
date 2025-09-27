"""
Predictor 1492
Generated on: 2025-09-10 02:35:36
Accuracy: 50.43%
"""


# PREDICTOR 1492 - Accuracy: 50.43%
# Correct predictions: 5043/10000 (50.43%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or \
       (C < 30 and E < 20 and B < 40 and A < 60) or \
       (C > 60 and E < 35 and A > 50) or \
       (A > 70 and B < 5 and C > 50) or \
       (E < 5 and A > 30 and D > 40 and C > 35):
        return 4
    elif B > 90 and E > 85:
        return 2
    elif (A > 85 and B < 25 and D > 85 and E > 85) or \
         (A > 85 and E < 15 and B > 50):
        return 3
    else:
        return 1