"""
Predictor 962
Generated on: 2025-09-10 01:09:35
Accuracy: 44.58%
"""


# PREDICTOR 962 - Accuracy: 44.58%
# Correct predictions: 4458/10000 (44.58%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and D > 90) or \
       (A < 5 and B > 55) or \
       (B > 90) or \
       (E > 70 and D < 20 and B > 40) or \
       (A > 60 and B < 35 and C > 40 and D > 40 and E < 35):
        return 4
    elif (B > 80) or (B > 55 and A > 60 and E > 30 and C <= 40):
        return 2
    elif A > 75 and D > 50:
        return 3
    else:
        return 1