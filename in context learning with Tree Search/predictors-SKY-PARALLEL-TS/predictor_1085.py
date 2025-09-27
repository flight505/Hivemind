"""
Predictor 1085
Generated on: 2025-09-10 01:28:10
Accuracy: 61.50%
"""


# PREDICTOR 1085 - Accuracy: 61.50%
# Correct predictions: 6150/10000 (61.50%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 45 and C > 60 and D < 15) or (C < 20 and D > 80) or (A < 10 and B > 70) or (C < 25 and E > 65):
        return 4
    elif (B > 85 and C > 75) or (D < 10 and C > 60 and E > 45) or (B > 70 and D < 20 and A < 40 and E > 40) or (A < 40 and B > 80 and C > 70):
        return 2
    elif (A > 45 and C < 50 and D > 55 and B > 35) or (D < 15 and C > 40 and B < 80) or (A < 50 and D < 25 and E < 45) or (C <= 10 and E < 60 and B < 50) or (B < 15 and C < 25 and D > 35):
        return 3
    else:
        return 1