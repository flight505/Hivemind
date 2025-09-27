"""
Predictor 1461
Generated on: 2025-09-10 02:31:46
Accuracy: 60.84%
"""


# PREDICTOR 1461 - Accuracy: 60.84%
# Correct predictions: 6084/10000 (60.84%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 25 and E > 70 and D > 20) or (B > 90 and C < 20 and D > 80 and E < 20) or (C < 10 and D < 10 and E > 50):
        return 4
    elif (B > 80 and C > 30 and E < 25 and D > 70):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (40 < A < 60 and C < 20 and D < 25 and E < 30):
        return 3
    else:
        return 1