"""
Predictor 58
Generated on: 2025-09-09 23:24:50
Accuracy: 58.31%
"""


# PREDICTOR 58 - Accuracy: 58.31%
# Correct predictions: 5831/10000 (58.31%)

def predict_output(A, B, C, D, E):
    if (A <= 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70):
        return 4
    elif (D < 10 and E > 85) or (B > 85 and C > 80) or (A > 90 and E < 10 and D < 60):
        return 2
    elif (E < 25 and (D > 90 or (C > 55 and D < 15) or (A < 20 and B > 60))) or (A > 50 and C < 50 and D > 70 and B > 40) or (D < 15 and C > 40 and B < 80):
        return 3
    else:
        return 1