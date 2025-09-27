"""
Predictor 677
Generated on: 2025-09-10 00:34:06
Accuracy: 52.06%
"""


# PREDICTOR 677 - Accuracy: 52.06%
# Correct predictions: 5206/10000 (52.06%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and (D - C) >= 85) or \
       (A > 80 and B < 10 and C > 60) or \
       (C > 90 and D < 20) or \
       (B < 15 and D < 25 and A > 50) or \
       (D < 5 and E > 80) or \
       (C < 15 and D > 80 and B > 50):
        return 4
    elif (B > 85 and C > 80) or \
         (A < 20 and B > 90):
        return 2
    elif (B > 60 and C > 70 and D > 60) or \
         (A > 90 and B < 10 and D > 90 and C < 15) or \
         (C < 25 and D < 20 and B > 50):
        return 3
    else:
        return 1