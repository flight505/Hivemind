"""
Predictor 88
Generated on: 2025-09-09 23:27:20
Accuracy: 50.79%
"""


# PREDICTOR 88 - Accuracy: 50.79%
# Correct predictions: 5079/10000 (50.79%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 25 and E > 70) or (D < 5 and E > 60) or (B > 80 and E > 90) or (C > 90 and D < 30) or (E > 70 and C < 40 and D > 50):
        return 4
    elif (B > 85 and C > 80 and E > 50) or (B > 70 and D < 20 and A < 50 and E > 40) or (C > 80 and B > 70 and E < 15):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 50) or (A < 50 and D < 30 and E < 40 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60 and D < 50) or (C > 80 and D > 70) or (B < 20 and A < 40):
        return 3
    else:
        return 1