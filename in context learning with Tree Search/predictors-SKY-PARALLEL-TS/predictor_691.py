"""
Predictor 691
Generated on: 2025-09-10 00:34:06
Accuracy: 56.82%
"""


# PREDICTOR 691 - Accuracy: 56.82%
# Correct predictions: 5682/10000 (56.82%)

def predict_output(A, B, C, D, E):
    if (B - A > 70 and E < 20) or (D - C > 80) or \
       (E < 10 and C > 35 and A < 70) or \
       (B > 70 and C > 70 and E < 15) or \
       (E > 80 and C < 30 and A > 65):
        return 4
    elif (A < 10 and B > 85 and C < 15 and E > 70) or \
         (A < 10 and E > 90 and B < 20) or \
         (B > 75 and E > 80 and C > 60) or \
         (C > 85 and D < 10 and A > 50):
        return 2
    elif A > 90 and B < 10:
        return 3
    else:
        return 1