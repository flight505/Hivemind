"""
Predictor 1421
Generated on: 2025-09-10 02:26:25
Accuracy: 56.45%
"""


# PREDICTOR 1421 - Accuracy: 56.45%
# Correct predictions: 5645/10000 (56.45%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 70 and E < 5) or (A > 80 and E > 80) or (C > 65 and D < 10 and E > 90) or (A > 50 and C < 20 and E > 60):
        return 4
    elif (B > 75 and C > 90) or (B > 90 and C > 75) or (B > 90 and E < 25) or (A > 90 and E < 10) or (B > 50 and C > 65 and D < 10 and E > 90):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 15 and C > 80 and D < 15) or (A < 40 and B > 70 and C < 50 and D > 75) or (C <= 10 and E < 60 and B < 60) or (A > 80 and B < 20 and C > 40 and E > 70) or (A < 25 and B > 80 and C > 65 and D > 90) or (A > 60 and B > 50 and C < 40 and D > 60) or (A > 80 and B < 20 and C > 40):
        return 3
    else:
        return 1