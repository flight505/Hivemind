"""
Predictor 1444
Generated on: 2025-09-10 02:27:48
Accuracy: 54.47%
"""


# PREDICTOR 1444 - Accuracy: 54.47%
# Correct predictions: 5447/10000 (54.47%)

def predict_output(A, B, C, D, E):
    if (A < 20 and B > 70 and E < 20) or (C < 15 and D > 80) or (B > 70 and C < 20) or (C > 80 and E < 10):
        return 4
    elif B > 40 and E > 70 and C < 40:
        return 2
    elif (C > 80 and D < 20) or (A > 80 and B < 30 and D > 70):
        return 3
    else:
        return 1