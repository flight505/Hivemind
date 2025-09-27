"""
Predictor 1403
Generated on: 2025-09-10 02:19:06
Accuracy: 49.60%
"""


# PREDICTOR 1403 - Accuracy: 49.60%
# Correct predictions: 4960/10000 (49.60%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 90) or (A > 80 and E > 90 and D < 30) or (B > 80 and E > 90 and D < 20) or (A > 70 and C < 30 and D > 70) or (A < 10 and B > 80 and D < 30) or (A < 25 and B < 25 and C < 35) or (A > 70 and B > 90 and C < 25 and D > 60):
        return 4
    elif (A > 90 and E < 10) or (A > 50 and B > 90 and C < 45 and D > 80 and E < 35):
        return 2
    elif (B < 10 and D > 80) or (A > 70 and B < 20 and E < 10 and C < 30 and D < 30):
        return 3
    else:
        return 1