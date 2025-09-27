"""
Predictor 1449
Generated on: 2025-09-10 02:27:48
Accuracy: 53.32%
"""


# PREDICTOR 1449 - Accuracy: 53.32%
# Correct predictions: 5332/10000 (53.32%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 90 and C < 40) or (E > 80 and D < 15) or (C > 50 and E < 5) or (B > 90 and A > 70 and C < 30) or (A < 30 and B > 95 and C < 40) or (E > 80 and B < 30):
        return 4
    elif (B > 70 and D > 60 and E < 25 and A < 60) or (B > 90 and D > 70 and E > 80) or (E > 50 and D < 25 and A < 30) or (B > 90 and E > 80):
        return 2
    elif (A > 60 and B < 30 and D > 90 and E < 30):
        return 3
    else:
        return 1