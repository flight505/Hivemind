"""
Predictor 1041
Generated on: 2025-09-10 01:20:29
Accuracy: 52.36%
"""


# PREDICTOR 1041 - Accuracy: 52.36%
# Correct predictions: 5236/10000 (52.36%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 85 and B > 75 and E > 70) or (A > 55 and B > 70 and E > 70 and D < 35):
        return 4
    elif (B > 80 and C > 60 and E < 30) or (A > 30 and B < 40 and 50 < C < 70 and E > 60) or (A < 25 and B > 65 and D < 15 and E > 80):
        return 2
    elif A > 90 and E < 10:
        return 2
    elif B < 10 and D > 80:
        return 3
    elif A > 50 and C < 50 and D > 70:
        return 3
    else:
        return 1