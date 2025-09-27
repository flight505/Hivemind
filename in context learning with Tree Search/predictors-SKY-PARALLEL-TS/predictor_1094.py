"""
Predictor 1094
Generated on: 2025-09-10 01:28:10
Accuracy: 51.85%
"""


# PREDICTOR 1094 - Accuracy: 51.85%
# Correct predictions: 5185/10000 (51.85%)

def predict_output(A, B, C, D, E):
    if A > 95 and B < 10 and C > 90:
        return 1
    if A < 5 and B > 90 and C < 10:
        return 1
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B < 25 and C > 35 and A > 30 and D > 30 and E < 30) or (A > 60 and B < 40 and C > 85 and E < 20) or (A < 35 and B < 15 and C > 75 and D < 20 and E > 55) or (A < 40 and B < 15 and C > 75 and D < 20 and E > 50):
        return 4
    elif (A > 90 and E < 10) or (B > 80 and C > 70) or (A < 25 and B > 75 and C > 90) or (A < 50 and B > 85 and C > 70) or (A > 80 and B > 85 and C < 50):
        return 2
    elif (B < 10 and D > 80) or (A > 60 and B < 25 and C > 65 and D < 10 and E < 5) or (A < 50 and B > 60 and C > 90 and D > 90 and E > 80):
        return 3
    else:
        return 1