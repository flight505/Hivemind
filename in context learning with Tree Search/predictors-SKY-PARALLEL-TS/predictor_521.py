"""
Predictor 521
Generated on: 2025-09-10 00:14:11
Accuracy: 48.68%
"""


# PREDICTOR 521 - Accuracy: 48.68%
# Correct predictions: 4868/10000 (48.68%)

def predict_output(A, B, C, D, E):
    if (C > 55 and D < 10 and E > 85) or (B > 90 and C > 90):
        return 2
    elif (A <= 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (C > 80):
        return 4
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60) or (D > 90 and E < 30) or (C < 20 and B > 60 and E < 30) or (D > 90 and B > 70):
        return 3
    else:
        return 1