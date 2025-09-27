"""
Predictor 395
Generated on: 2025-09-09 23:57:59
Accuracy: 59.17%
"""


# PREDICTOR 395 - Accuracy: 59.17%
# Correct predictions: 5917/10000 (59.17%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 50) or \
       (C < 15 and D > 80) or \
       (C < 30 and E > 60) or \
       (E < 10 and C > 60 and B < 40) or \
       (C < 20 and B > 80) or \
       (A > 80 and B > 80) or \
       (C < 20 and D > 50):
        return 4
    elif (B > 90 and E > 50) or \
         (B > 85 and C > 70 and A > 30):
        return 2
    elif (D < 10 and C > 50 and B < 30) or \
         (D < 10 and C < 30 and B < 40 and A < 60 and E < 20) or \
         (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1