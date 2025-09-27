"""
Predictor 1423
Generated on: 2025-09-10 02:26:25
Accuracy: 54.35%
"""


# PREDICTOR 1423 - Accuracy: 54.35%
# Correct predictions: 5435/10000 (54.35%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 70 and E < 5) or (A > 80 and E > 90) or (A > 90 and C < 10) or (A > 50 and E < 15 and C < 55) or (A > 95 and C < 5 and E > 80) or (B > 80 and C < 30 and E > 90) or (C > 90 and D < 25):
        return 4
    elif (B > 75 and C > 90) or (B > 90 and C > 75) or (B > 90 and E < 25) or (A > 90 and E < 10) or (B > 50 and C > 65 and D < 10 and E > 90):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 15 and C > 80 and D < 15) or (A < 40 and B > 70 and C < 50 and D > 75) or (C <= 10 and E < 60 and B < 60) or (A > 80 and B < 20 and C > 40 and E > 70) or (A < 25 and B > 80 and C > 65 and D > 90) or (A > 60 and B > 50 and C < 40 and D > 60) or (A > 80 and B < 20 and C < 50) or (B > 80 and D > 90):
        return 3
    else:
        return 1