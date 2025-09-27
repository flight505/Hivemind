"""
Predictor 1451
Generated on: 2025-09-10 02:27:48
Accuracy: 53.58%
"""


# PREDICTOR 1451 - Accuracy: 53.58%
# Correct predictions: 5358/10000 (53.58%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 90 and C < 40) or (E > 80 and D < 15) or (A < 10 and B < 10 and C > 50 and E < 10) or (A < 30 and B > 95 and C < 40):
        return 4
    elif (B > 70 and E < 25 and A > 50) or (E > 55 and D < 25 and A < 30) or (B > 90 and E > 80 and A < 40):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 30) or (A > 70 and B < 20 and D > 60 and C < 30) or (D > 90 and E > 70 and C > 30) or (B > 90 and E < 15):
        return 3
    else:
        return 1