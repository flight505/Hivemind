"""
Predictor 1389
Generated on: 2025-09-10 02:19:06
Accuracy: 55.32%
"""


# PREDICTOR 1389 - Accuracy: 55.32%
# Correct predictions: 5532/10000 (55.32%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 80 and B < 30 and E < 5) or (A < 10 and B > 80 and C > 45) or (A > 95 and B < 30 and C < 10 and D > 50) or (A > 50 and B > 50 and C > 80 and D < 20 and E < 5):
        return 4
    elif (A > 50 and B > 60 and E < 5) or (B > 90 and D > 80 and E < 35) or (A > 70 and B > 60 and E > 90) or (B > 80 and C > 40 and E < 10):
        return 2
    elif (A > 50 and B < 20 and D < 25) or (A > 30 and B > 50 and C < 15 and D > 60) or (A > 45 and C < 50 and D > 60 and B > 40) or (A > 50 and C < 30 and D < 15):
        return 3
    else:
        return 1