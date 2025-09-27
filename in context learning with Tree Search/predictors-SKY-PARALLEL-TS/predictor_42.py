"""
Predictor 42
Generated on: 2025-09-09 23:21:45
Accuracy: 52.66%
"""


# PREDICTOR 42 - Accuracy: 52.66%
# Correct predictions: 5266/10000 (52.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (E < 10 and C > 70 and B < 50):
        return 4
    elif C < 15 and D > 55 and B < 65:
        return 3
    elif A > 70 and B < 30 and E > 20:
        return 3
    elif B > 90 and D > 90:
        return 3
    elif B > 80 and E < 10 and A < 40:
        return 2
    else:
        return 1