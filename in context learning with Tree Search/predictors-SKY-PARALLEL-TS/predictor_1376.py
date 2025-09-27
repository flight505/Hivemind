"""
Predictor 1376
Generated on: 2025-09-10 02:16:28
Accuracy: 53.81%
"""


# PREDICTOR 1376 - Accuracy: 53.81%
# Correct predictions: 5381/10000 (53.81%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80 and E > 80) or (C > 60 and D < 30 and E > 80):
        return 4
    elif (C < 5 and D > 80 and E > 70) or (C > 90 and B > 80) or (C < 15 and D > 70 and E > 50):
        return 2
    elif A > 60 and B < 20 and D < 10:
        return 3
    elif B > 60 and E < 5:
        return 4
    else:
        return 1