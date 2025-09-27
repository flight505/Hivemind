"""
Predictor 761
Generated on: 2025-09-09 20:27:51
Accuracy: 55.58%
"""


# PREDICTOR 761 - Accuracy: 55.58%
# Correct predictions: 5558/10000 (55.58%)

def predict_output(A, B, C, D, E):
    if B < 15 and C < 15 and E > 50:
        return 4
    elif C < 25 and E > 90:
        return 4
    elif C > 80 and E > 90:
        return 4
    elif B < 10 and C > 40 and E < 30:
        return 4
    elif B + C > 140 and A < 40:
        return 2
    elif B < 20 and C < 20:
        return 3
    elif B < 10 and C > 50:
        return 3
    elif B < 30 and C < 30 and E < 10:
        return 3
    elif C < 35 and D > 80 and B > 50 and E > 60:
        return 3
    else:
        return 1