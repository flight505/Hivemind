"""
Predictor 79
Generated on: 2025-09-09 23:27:20
Accuracy: 58.03%
"""


# PREDICTOR 79 - Accuracy: 58.03%
# Correct predictions: 5803/10000 (58.03%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (C > 70 and D < 25) or (A > 80 and B < 10 and C < 20) or (B > 75 and C < 15):
        return 4
    if (B > 85 and C > 75) or (B > 70 and D < 20 and A < 50 and E > 40) or (B > 90):
        return 2
    if (A > 45 and C < 55 and D > 60 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and 40 < C < 60 and B < 80) or (C <= 10 and E < 60 and B < 70):
        return 3
    else:
        return 1