"""
Predictor 592
Generated on: 2025-09-10 00:22:13
Accuracy: 53.16%
"""


# PREDICTOR 592 - Accuracy: 53.16%
# Correct predictions: 5316/10000 (53.16%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B < 15 and D < 15 and E > 95) or (A > 40 and B > 40 and C < 50 and D > 70 and E < 5):
        return 4
    elif B > 90 and E < 10:
        return 2
    elif (B < 10 and D > 40) or (A < 5 and B > 40 and C > 80 and D < 10):
        return 3
    else:
        return 1