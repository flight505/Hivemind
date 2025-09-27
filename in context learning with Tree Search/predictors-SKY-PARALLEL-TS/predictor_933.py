"""
Predictor 933
Generated on: 2025-09-10 01:07:55
Accuracy: 59.30%
"""


# PREDICTOR 933 - Accuracy: 59.30%
# Correct predictions: 5930/10000 (59.30%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C < 30 and E > 60 and D < 30) or (B > 50 and C < 30 and E > 55):
        return 4
    elif (B > 85 and E > 75) or (B > 95 and C < 30) or (A < 15 and B > 80 and C > 40):
        return 2
    elif (A > 40 and B > 50 and C < 35 and D > 75) or (A < 15 and B > 40 and C < 15 and D > 40) or (A > 50 and B < 30 and C < 40 and D < 20):
        return 3
    else:
        return 1