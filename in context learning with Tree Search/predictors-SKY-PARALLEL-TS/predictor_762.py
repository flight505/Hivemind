"""
Predictor 762
Generated on: 2025-09-10 00:44:16
Accuracy: 54.89%
"""


# PREDICTOR 762 - Accuracy: 54.89%
# Correct predictions: 5489/10000 (54.89%)

def predict_output(A, B, C, D, E):
    if (B - A > 70) or (D - C > 80) or (A > 70 and B < 5 and C > 50) or (B > 80 and C > 75 and E > 90) or (B < 15 and C > 70 and E < 25) or (A > 80 and B < 30 and C > 90 and E > 80) or (C < 15 and D > 80) or (A > 70 and B < 20 and C > 70):
        return 4
    elif (B > 60 and C < 20 and E > 50) or (B > 85 and C > 80) or (A > 80 and B > 80 and D > 50 and E > 70) or (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    elif (A > 40 and B < 10 and C < 20 and D > 45) or (B > 80 and C > 70 and D > 95 and E < 25) or (A < 10 and B < 5 and C > 75) or (A > 50 and C < 50 and D > 70 and B > 40) or (C < 10 and E < 60):
        return 3
    else:
        return 1