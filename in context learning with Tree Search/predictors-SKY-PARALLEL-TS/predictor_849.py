"""
Predictor 849
Generated on: 2025-09-10 00:55:50
Accuracy: 52.56%
"""


# PREDICTOR 849 - Accuracy: 52.56%
# Correct predictions: 5256/10000 (52.56%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C > 90) or (E > 90 and D < 30) or (B < 10 and C > 60) or (C < 20 and D < 20 and E > 80) or (A > 80 and C < 20 and D > 70) or (A > 50 and E > 90 and D < 30):
        return 4
    elif (A < 10 and E > 90) or (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    elif (A > 70 and B < 30 and C > 70 and D < 10) or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1