"""
Predictor 1097
Generated on: 2025-09-10 01:28:10
Accuracy: 57.47%
"""


# PREDICTOR 1097 - Accuracy: 57.47%
# Correct predictions: 5747/10000 (57.47%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E > 10) or (C < 10 and D > 90 and E > 10) or (C < 25 and E > 65 and B > 50) or (B < 20 and C > 90 and E < 20) or (A < 15 and B > 50 and C > 90 and D < 40 and E > 40) or (A > 50 and B < 20 and C > 90 and E < 20):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif (A > 70 and B < 30 and 40 < C < 50 and D > 95 and E > 50) or (A > 70 and B < 15 and C < 20 and D < 35 and E < 20) or (A > 90 and 45 < B < 55 and C < 45 and D > 70 and E > 90) or (A < 30 and B < 10 and 30 < C < 40 and D < 15 and E > 40) or (A < 30 and B > 80 and C < 40 and D > 85 and E < 5):
        return 3
    else:
        return 1