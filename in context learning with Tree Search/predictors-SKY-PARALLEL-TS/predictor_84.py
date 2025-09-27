"""
Predictor 84
Generated on: 2025-09-09 23:27:20
Accuracy: 60.81%
"""


# PREDICTOR 84 - Accuracy: 60.81%
# Correct predictions: 6081/10000 (60.81%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 60) or (C < 15 and D > 30) or (C < 25 and E > 70):
        return 4
    if (B > 85 and C > 75 and D < 60 and A < 70) or (B > 70 and D < 20 and A < 50 and E > 40) or (E > 90 and D < 20 and B < 25):
        return 2
    if (A > 50 and C <= 50 and D > 60 and B > 30) or (A < 50 and D < 30 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 15 and E < 60):
        return 3
    else:
        return 1