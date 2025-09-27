"""
Predictor 1127
Generated on: 2025-09-10 01:35:54
Accuracy: 53.78%
"""


# PREDICTOR 1127 - Accuracy: 53.78%
# Correct predictions: 5378/10000 (53.78%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90):
        return 4
    elif E > 60 and D < 15 and C > 40:
        return 2
    elif D > 70 and E < 40 and (C < 55 or A < 40):
        return 3
    elif E < 15 and D < 20 and C < 20 and A < 50:
        return 3
    elif A > 50 and B < 30 and C < 25 and E < 40:
        return 3
    elif A > 60 and B < 20 and C < 15 and D < 50 and E > 30:
        return 4
    else:
        return 1