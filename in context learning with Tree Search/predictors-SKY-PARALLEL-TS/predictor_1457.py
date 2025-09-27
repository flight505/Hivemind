"""
Predictor 1457
Generated on: 2025-09-10 02:31:46
Accuracy: 53.45%
"""


# PREDICTOR 1457 - Accuracy: 53.45%
# Correct predictions: 5345/10000 (53.45%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 70 and C > 70 and E < 5) or (C < 30 and D > 70 and E > 90) or (C < 10 and D > 60 and B > 50) or (A > 60 and B < 20 and C < 20 and E > 50) or (C < 25 and D > 70) or (B > 70 and C > 70 and E < 10) or (A > 60 and B > 50 and C < 10 and D > 60):
        return 4
    elif (B > 90 and C > 70 and E < 10) or (A < 5 and B > 90 and D > 90 and E < 15) or (C > 80 and D < 15 and E > 80) or (B > 80 and E < 15 and A < 40) or (A < 40 and B > 90 and C > 70 and E < 20):
        return 2
    elif (A > 50 and B < 20 and C < 15 and E < 20) or (A > 80 and D > 60) or (A > 70 and B > 40 and C < 40 and D > 50) or (A > 80 and B > 40 and C < 40 and D > 60 and E > 60):
        return 3
    else:
        return 1