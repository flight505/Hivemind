"""
Predictor 1018
Generated on: 2025-09-10 01:15:51
Accuracy: 58.11%
"""


# PREDICTOR 1018 - Accuracy: 58.11%
# Correct predictions: 5811/10000 (58.11%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and E > 70) or (C < 20 and D > 80 and B < 70 and E < 50) or (B < 20 and C > 40 and D < 30 and E > 40) or (A > 80 and C > 40 and D < 35 and E > 70):
        return 4
    elif (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40) or (A < 30 and B > 80 and C > 70) or (B > 90 and D > 90 and C < 40) or (B > 70 and E < 15 and D > 65 and C < 45 and A > 45):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 50 and D < 25 and E < 40 and B < 80) or (D < 15 and C > 40 and B < 80 and A < 70) or (C <= 10 and E < 60 and B < 50 and D > 20) or (A > 75 and B < 25 and C < 45 and D > 60) or (B > 80 and C > 85 and D > 80 and A < 50) or (A < 40 and B > 90 and D > 90) or (B > 80 and D > 90 and E < 30) or (A > 60 and B < 15 and C < 15 and D > 70) or (A < 25 and C < 25 and B > 40) or (C < 5 and D > 60) or (B > 70 and C < 10 and E < 10) or (A > 90 and B > 30 and C < 50 and D > 65) or (A > 55 and C < 25 and D < 25 and E < 5) or (B > 75 and D > 75 and A > 70) or (D > 85 and E > 70 and A > 70) or (B > 70 and C > 90) or (A > 70 and B < 15 and C < 15):
        return 3
    else:
        return 1