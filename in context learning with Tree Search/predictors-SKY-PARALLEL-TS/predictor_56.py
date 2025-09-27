"""
Predictor 56
Generated on: 2025-09-09 23:24:50
Accuracy: 59.47%
"""


# PREDICTOR 56 - Accuracy: 59.47%
# Correct predictions: 5947/10000 (59.47%)

def predict_output(A, B, C, D, E):
    if (A <= 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70):
        return 4
    elif C > 55 and D < 10 and E > 85:
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (D > 90 and E < 30) or (C < 20 and B > 60 and E < 30):
        return 3
    else:
        return 1