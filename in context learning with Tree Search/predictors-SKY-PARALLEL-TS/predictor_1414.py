"""
Predictor 1414
Generated on: 2025-09-10 02:26:25
Accuracy: 50.08%
"""


# PREDICTOR 1414 - Accuracy: 50.08%
# Correct predictions: 5008/10000 (50.08%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 65 and E < 30) or (C < 20 and E > 80) or (B > 65 and C > 60 and E < 20) or (E > 90 and D < 30) or (C > 90 and A > 65) or (A > 70 and B < 25 and C > 60 and E < 20) or (C < 15 and D > 90):
        return 4
    elif (B > 75 and C > 55 and E < 80 and A > 20) or (A < 20 and D < 25 and E > 50 and C > 40 and B > 60) or (B > 80 and E < 15) or (A > 70 and B > 70 and E < 25):
        return 2
    elif (A > 60 and B < 20) or (D < 15 and C > 35 and B < 40) or (C < 15 and B > 60 and E < 20) or (A > 80 and B < 10) or (B > 80 and D > 90) or (A < 15 and B > 70 and C > 80):
        return 3
    else:
        return 1