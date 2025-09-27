"""
Predictor 1019
Generated on: 2025-09-10 01:15:51
Accuracy: 51.58%
"""


# PREDICTOR 1019 - Accuracy: 51.58%
# Correct predictions: 5158/10000 (51.58%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 20 and D > 80 and A > 60 and E < 40) or (C < 10 and E > 70) or (B < 20 and C > 40 and D < 30 and E > 40):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif (B < 10 and D > 80) or (B > 70 and C > 40 and D > 70) or (B < 20 and C < 15 and E > 40) or (D > 80 and C > 45 and A > 70) or (B > 70 and C > 90):
        return 3
    else:
        return 1