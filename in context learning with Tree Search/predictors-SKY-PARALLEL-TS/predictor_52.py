"""
Predictor 52
Generated on: 2025-09-09 23:21:45
Accuracy: 51.45%
"""


# PREDICTOR 52 - Accuracy: 51.45%
# Correct predictions: 5145/10000 (51.45%)

def predict_output(A, B, C, D, E):
    if D > 75 and E < 25:
        return 3
    elif A > 90 and E < 10:
        return 2
    elif B > 90 and C < 10:
        return 2
    elif A < 10 and B > 70 and E < 20:
        return 4
    elif C < 20 and D > 60:
        return 4
    elif B > 70 and D > 80:
        return 4
    elif C > 80 and E < 15:
        return 4
    elif 40 < A < 50 and 40 < B < 50 and 40 < C < 50 and D < 40 and E < 30:
        return 4
    elif A < 20 and B < 30 and C > 30 and D < 40 and E > 40:
        return 4
    elif B < 10 and D > 80:
        return 3
    else:
        return 1