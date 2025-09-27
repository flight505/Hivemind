"""
Predictor 425
Generated on: 2025-09-10 00:02:23
Accuracy: 59.71%
"""


# PREDICTOR 425 - Accuracy: 59.71%
# Correct predictions: 5971/10000 (59.71%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (A > 70 and B < 40 and C < 30 and D > 70):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80) or (C > 70 and D < 5 and E > 60):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A > 90 and B < 30 and D > 70):
        return 3
    else:
        return 1