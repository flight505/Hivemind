"""
Predictor 1134
Generated on: 2025-09-10 01:35:54
Accuracy: 46.93%
"""


# PREDICTOR 1134 - Accuracy: 46.93%
# Correct predictions: 4693/10000 (46.93%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (D < 20 and E > 70 and A > 30 and C < 50) or (B < 10 and E > 80) or (C > 80 and D < 10 and E > 90):
        return 4
    elif B > 80 or E > 80:
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A > 40 and D < 20 and C > 35 and B < 50):
        return 3
    else:
        return 1