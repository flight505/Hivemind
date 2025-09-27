"""
Predictor 76
Generated on: 2025-09-09 23:27:20
Accuracy: 57.31%
"""


# PREDICTOR 76 - Accuracy: 57.31%
# Correct predictions: 5731/10000 (57.31%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (B < 10 and A > 80) or (C > 70 and D < 25) or (B > 75 and C < 15):
        return 4
    if (B > 85 and C > 80) or (B > 90 and E < 50) or (B > 70 and D < 20 and A < 50 and E > 40) or (A < 15 and B > 95):
        return 2
    if (A > 50 and C < 50 and D > 60 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80 and C < 40) or (D < 15 and 20 < C < 60 and B < 80) or (C <= 10 and E < 60 and B < 75):
        return 3
    else:
        return 1