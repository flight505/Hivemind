"""
Predictor 659
Generated on: 2025-09-10 00:31:36
Accuracy: 56.96%
"""


# PREDICTOR 659 - Accuracy: 56.96%
# Correct predictions: 5696/10000 (56.96%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70) or (C < 25 and D > 85) or (C > 85 and D < 20 and E < 40) or (A > 90 and B < 10 and C > 70):
        return 4
    elif (A < 5 and E > 60) or (B > 70 and A < 50 and C > 30 and D > 40):
        return 2
    elif A > 90 and B < 30 and D > 60:
        return 3
    else:
        return 1