"""
Predictor 1446
Generated on: 2025-09-10 02:27:48
Accuracy: 56.44%
"""


# PREDICTOR 1446 - Accuracy: 56.44%
# Correct predictions: 5644/10000 (56.44%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 80 and C < 20 and E < 30) or (C < 20 and D > 75 and B > 50) or (A < 20 and C > 85 and E < 10) or (B > 70 and C < 25 and D > 70):
        return 4
    elif (B > 75 and E > 70 and C < 50) or (A < 10 and B > 80 and E > 60):
        return 2
    elif (A > 60 and B < 15 and C > 80 and D < 20) or (A > 80 and B < 35 and D > 65):
        return 3
    else:
        return 1