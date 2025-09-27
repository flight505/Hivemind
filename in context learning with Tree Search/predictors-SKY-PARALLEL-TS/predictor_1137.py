"""
Predictor 1137
Generated on: 2025-09-10 01:35:54
Accuracy: 49.38%
"""


# PREDICTOR 1137 - Accuracy: 49.38%
# Correct predictions: 4938/10000 (49.38%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 90 and D < 15) or (A > 55 and B < 35 and C > 40):
        return 4
    elif (B > 85 and C > 75) or (B > 95 and E > 80):
        return 2
    elif (C > 75 and D > 85 and E > 80) or (A < 5 and C < 15) or (C < 30 and D > 95):
        return 3
    else:
        return 1