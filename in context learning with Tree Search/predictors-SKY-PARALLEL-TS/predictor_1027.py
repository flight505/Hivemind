"""
Predictor 1027
Generated on: 2025-09-10 01:20:29
Accuracy: 55.55%
"""


# PREDICTOR 1027 - Accuracy: 55.55%
# Correct predictions: 5555/10000 (55.55%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 10 and D > 90) or (A < 30 and B > 65 and C < 35 and D > 50 and E < 20) or (A > 70 and B < 20 and C < 10 and D > 50) or (A > 70 and B > 95 and C < 25 and D > 80 and E < 25) or (A < 20 and B > 85 and C > 70 and D < 20 and E > 80):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80 and D > 45) or (A < 35 and B > 75 and C > 50 and D > 55 and E < 40) or (B > 90 and C < 40 and D > 60):
        return 2
    elif (B < 10 and D > 80) or (A > 70 and B > 40 and C < 50 and D > 55):
        return 3
    else:
        return 1