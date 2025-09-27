"""
Predictor 1071
Generated on: 2025-09-10 01:25:44
Accuracy: 45.65%
"""


# PREDICTOR 1071 - Accuracy: 45.65%
# Correct predictions: 4565/10000 (45.65%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (D > 65 and E < 10) or (B > 80 and C > 60 and A < 80 and D < 50):
        return 4
    elif A > 90 or (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50):
        return 2
    elif (A > 50 and C < 50 and D > 70) or (C < 10 and E < 60) or (A < 50 and D < 25 and E < 20) or (C > 50 and D > 70 and E > 70):
        return 3
    else:
        return 1