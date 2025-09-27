"""
Predictor 1021
Generated on: 2025-09-10 01:15:51
Accuracy: 50.73%
"""


# PREDICTOR 1021 - Accuracy: 50.73%
# Correct predictions: 5073/10000 (50.73%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 80) or (A > 60 and B < 30 and C > 40) or (B < 5 and E > 70):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80) or (C < 10 and E > 80) or (B > 70 and E > 70) or (D < 10 and E > 60):
        return 2
    elif (B < 10 and D > 80) or (A > 80 and D > 50 and C < 40) or (A < 20 and C < 15):
        return 3
    else:
        return 1