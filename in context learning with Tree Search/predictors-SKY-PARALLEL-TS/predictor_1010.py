"""
Predictor 1010
Generated on: 2025-09-10 01:15:51
Accuracy: 43.54%
"""


# PREDICTOR 1010 - Accuracy: 43.54%
# Correct predictions: 4354/10000 (43.54%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 80 and E > 90) or (C > 80 and B < 50) or (B > 70 and D > 60 and C < 30):
        return 4
    elif (D > 90 and E > 80) or (C < 5 and B > 50) or (B < 20 and C > 30):
        return 3
    elif B > 70 and C > 80:
        return 2
    else:
        return 1