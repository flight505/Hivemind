"""
Predictor 1053
Generated on: 2025-09-10 01:23:11
Accuracy: 55.54%
"""


# PREDICTOR 1053 - Accuracy: 55.54%
# Correct predictions: 5554/10000 (55.54%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (40 < A < 50 and C < 30 and D > 65 and E < 10) or (50 < A < 60 and C < 35 and D > 50 and E > 80) or (A < 5 and C > 40 and D < 30 and E < 30) or (A < 35 and B > 60 and C > 70 and D < 20) or (A > 70 and B < 35 and C < 15 and D > 50) or (C < 15 and D > 80):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80) or (B > 90 and E < 20) or (A < 25 and D < 20 and E > 60):
        return 2
    elif (B < 10 and D > 80) or (A > 90 and D > 70 and C < 50 and E < 30) or (A > 50 and C < 50 and D > 70 and B > 40) or (A > 90 and B > 50 and C < 50 and E < 30):
        return 3
    else:
        return 1