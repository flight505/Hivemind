"""
Predictor 1226
Generated on: 2025-09-10 01:48:40
Accuracy: 53.62%
"""


# PREDICTOR 1226 - Accuracy: 53.62%
# Correct predictions: 5362/10000 (53.62%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 85 and E < 20:
        return 3
    if A < 5 and C < 20 and E > 80:
        return 2
    if (A < 10 and B > 70 and E < 20) or \
       (C < 15 and D > 60) or \
       (C > 60 and D < 20) or \
       (E > 75 and D < 25 and (A > 40 or B > 70)) or \
       (C < 50 and E < 20 and A < 40) or \
       (C > 80 and B < 30):
        return 4
    else:
        return 1