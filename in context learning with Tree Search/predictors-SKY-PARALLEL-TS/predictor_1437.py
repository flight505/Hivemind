"""
Predictor 1437
Generated on: 2025-09-10 02:27:48
Accuracy: 52.84%
"""


# PREDICTOR 1437 - Accuracy: 52.84%
# Correct predictions: 5284/10000 (52.84%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 70) or (C < 25 and E > 70) or (B > 80 and C < 35) or (A >= 70 and B < 20 and C > 50):
        return 4
    elif (B > 80 and (C > 80 or D > 55)) or (B > 60 and E > 70 and C < 20):
        return 2
    elif A > 50 and B < 40 and D > 60:
        return 3
    else:
        return 1