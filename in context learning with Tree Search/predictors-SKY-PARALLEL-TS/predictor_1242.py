"""
Predictor 1242
Generated on: 2025-09-10 01:52:29
Accuracy: 50.29%
"""


# PREDICTOR 1242 - Accuracy: 50.29%
# Correct predictions: 5029/10000 (50.29%)

def predict_output(A, B, C, D, E):
    if (A < 30 and B > 70) or (C < 20 and D > 60) or (B > 70 and C < 30) or (A > 60 and B < 20 and C < 15) or (A > 90 and B > 80) or (C > 90 and A < 5) or (A > 50 and B < 10 and E > 80) or (D > 80 and C < 10):
        return 4
    elif (A > 90 and D > 70) or (A > 70 and B < 20 and C < 5) or (D > 80 and E < 10) or (A > 90 and E > 70 and D > 70):
        return 3
    elif (A > 90 and E < 10) or (B > 85 and C > 80) or (B > 70 and D < 20 and E > 40):
        return 2
    else:
        return 1