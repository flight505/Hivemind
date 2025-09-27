"""
Predictor 1203
Generated on: 2025-09-10 01:43:05
Accuracy: 57.64%
"""


# PREDICTOR 1203 - Accuracy: 57.64%
# Correct predictions: 5764/10000 (57.64%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (C < 30 and E > 65) or (A > 80 and B < 15 and D > 70) or (B < 15 and C > 75 and E < 10) or (A < 30 and C > 60 and D < 25 and E > 70) or (A > 70 and B < 20 and C < 15 and D > 50) or (A > 90 and C < 10 and D > 80) or (A > 50 and B > 90 and C < 30 and E > 70):
        return 4
    elif (B > 85 and C > 80) or (B > 70 and D < 20 and E > 40) or (D < 10 and C > 50 and E > 50) or (A < 40 and D < 25 and E > 50) or (B > 75 and C > 55 and E > 60) or (A < 10 and E > 90 and D < 20) or (B > 90 and E > 80) or (A < 50 and B > 80 and C > 75):
        return 2
    elif (A > 45 and C < 50 and D > 60 and B > 35) or (D < 15 and C > 40 and E < 50) or (C < 10 and B < 50 and E < 60) or (A > 75 and B < 25 and D > 40) or (B > 80 and D > 90) or (A < 40 and B > 90 and D > 85) or (A > 60 and B < 15 and D > 70) or (B > 80 and C > 85 and D > 80):
        return 3
    else:
        return 1