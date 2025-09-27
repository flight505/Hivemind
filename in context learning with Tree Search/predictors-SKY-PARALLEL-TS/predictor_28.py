"""
Predictor 28
Generated on: 2025-09-09 23:19:12
Accuracy: 42.28%
"""


# PREDICTOR 28 - Accuracy: 42.28%
# Correct predictions: 4228/10000 (42.28%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 50 and D < 30 and E > 70):
        return 4
    elif (B > 70 and C > 60 and E < 30) or (A < 10 and B < 30 and E > 40) or (A > 90 and E < 10):
        return 2
    elif B < 15 or (C < 40 and D > 60) or (A > 60 and B < 20) or (A > 90):
        return 3
    else:
        return 1