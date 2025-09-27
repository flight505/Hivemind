"""
Predictor 675
Generated on: 2025-09-10 00:34:06
Accuracy: 59.61%
"""


# PREDICTOR 675 - Accuracy: 59.61%
# Correct predictions: 5961/10000 (59.61%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 25 and E > 65) or (A < 20 and C > 55 and D > 50 and E < 25) or (A > 30 and B < 30 and C < 20 and D > 50 and E < 5) or (A > 50 and B < 10 and C < 20 and D < 10 and E > 60) or (A > 80 and C > 50 and D < 25 and E > 75) or (B < 15 and C > 75 and E < 5):
        return 4
    elif (A > 85 and B > 75 and C < 40 and E > 65) or (B > 85 and C > 80):
        return 2
    elif (A > 50 and B > 50 and D > 50 and C < 55) or (A > 45 and D < 5 and C < 30) or (C <= 10 and E < 60):
        return 3
    else:
        return 1