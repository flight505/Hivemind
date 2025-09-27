"""
Predictor 1163
Generated on: 2025-09-10 01:37:38
Accuracy: 55.83%
"""


# PREDICTOR 1163 - Accuracy: 55.83%
# Correct predictions: 5583/10000 (55.83%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 70 and C > 30 and E > 60 and A < 60) or (A > 80 and B < 40 and D < 30 and E > 80) or (A < 30 and C > 60 and E < 15):
        return 4
    elif (C < 15 and D > 60 and E < 30) or (A > 90 and B < 40 and D > 70) or (A < 25 and B > 45 and C < 30 and D < 45):
        return 3
    elif (B > 65 and C > 80 and A < 50) or (B > 60 and E > 60 and C > 45 and C < 55 and D < 60 and A < 50):
        return 2
    else:
        return 1