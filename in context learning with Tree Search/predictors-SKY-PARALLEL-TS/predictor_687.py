"""
Predictor 687
Generated on: 2025-09-10 00:34:06
Accuracy: 54.25%
"""


# PREDICTOR 687 - Accuracy: 54.25%
# Correct predictions: 5425/10000 (54.25%)

def predict_output(A, B, C, D, E):
    if (D > 40 and ((C < 40 and (B > 60 or E > 60)) or (C > 90 and E < 20))) or (A > 50 and B > 60 and C < 40 and D > 40 and E > 60):
        return 4
    if ((A < 10 and C < 15 and E > 70) or (B > 90 and E > 80) or (C > 50 and D < 20 and E > 60 and A < 55) or (B > 30 and C > 50 and D < 20 and E > 60)):
        return 2
    if ((A > 75 and D > 60 and E > 70) or (C < 20 and E < 10 and B < 50) or (A > 70 and B < 40 and D > 60)):
        return 3
    else:
        return 1