"""
Predictor 1467
Generated on: 2025-09-10 02:31:46
Accuracy: 44.88%
"""


# PREDICTOR 1467 - Accuracy: 44.88%
# Correct predictions: 4488/10000 (44.88%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80):
        return 4
    elif B > 80:
        return 2
    elif (E > 70 and B < 40 and A < 20) or (D > 90 and E > 80):
        return 4
    elif (A > 90 and B < 20) or (D < 15 and C > 40) or (A > 80 and C < 20 and D > 70):
        return 3
    elif E > 70 and A < 50 and B < 40:
        return 2
    else:
        return 1