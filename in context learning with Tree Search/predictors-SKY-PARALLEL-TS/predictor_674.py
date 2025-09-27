"""
Predictor 674
Generated on: 2025-09-10 00:34:06
Accuracy: 52.25%
"""


# PREDICTOR 674 - Accuracy: 52.25%
# Correct predictions: 5225/10000 (52.25%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 50 and E < 25 and A < 25) or (D > 50 and E < 5 and C < 20) or (B < 10 and D < 10 and E > 60) or (C > 50 and D < 25 and E > 75) or (C < 20 and D > 50 and E > 60 and B < 10):
        return 4
    elif (A > 85 and B > 75 and E > 65) or (A > 90 and B > 70 and C < 40):
        return 2
    elif (A > 55 and B > 55 and C > 45 and D > 55 and E < 50) or (A > 45 and D < 5):
        return 3
    else:
        return 1