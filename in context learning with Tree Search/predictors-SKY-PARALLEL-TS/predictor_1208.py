"""
Predictor 1208
Generated on: 2025-09-10 01:46:44
Accuracy: 53.03%
"""


# PREDICTOR 1208 - Accuracy: 53.03%
# Correct predictions: 5303/10000 (53.03%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E < 5 and D > 50) or (B < 10 and E > 70) or (B > 60 and E > 70 and C < 35) or (A < 30 and C > 75 and D < 30):
        return 4
    elif (A < 5 and E > 50 and B < 40) or (B > 85 and E > 70) or (A > 60 and B < 30 and C > 60):
        return 2
    elif (B < 10 and D > 80) or (A + B + C + D + E < 100) or (A < 50 and D < 25 and E < 20):
        return 3
    else:
        return 1