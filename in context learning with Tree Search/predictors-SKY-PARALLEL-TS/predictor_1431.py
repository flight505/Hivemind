"""
Predictor 1431
Generated on: 2025-09-10 02:26:25
Accuracy: 55.62%
"""


# PREDICTOR 1431 - Accuracy: 55.62%
# Correct predictions: 5562/10000 (55.62%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 80 and E > 50) or (B < 20 and C > 60 and D < 25) or (C > 80 and E < 15) or (B < 15 and C < 15 and E > 70):
        return 4
    elif (A < 15 and B > 60 and E > 65) or (B > 80 and C > 70 and D < 30 and A < 50):
        return 2
    elif (A < 40 and B < 20 and C > 80 and D < 10) or (A > 50 and C < 20 and D > 70 and B > 40) or (C < 15 and B > 60 and E < 15):
        return 3
    else:
        return 1