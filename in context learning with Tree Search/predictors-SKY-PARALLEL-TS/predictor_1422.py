"""
Predictor 1422
Generated on: 2025-09-10 02:26:25
Accuracy: 53.22%
"""


# PREDICTOR 1422 - Accuracy: 53.22%
# Correct predictions: 5322/10000 (53.22%)

def predict_output(A, B, C, D, E):
    if (C > 70 and E < 5) or (A < 10 and B > 70) or (C < 15 and D > 80) or (A > 80 and B < 20 and E > 90) or (A > 90 and C < 10 and D > 60) or (E < 15 and D > 50) or (A > 95 and C < 5 and E > 80) or (C > 90 and D < 30) or (A > 50 and C < 20 and E > 80):
        return 4
    elif (C > 65 and D < 10 and E > 90) or (B >= 85 and C > 80) or (B > 70 and D < 20 and E > 40) or (B > 80 and C > 65 and E > 60):
        return 2
    elif (A > 80 and B < 20 and E > 70) or (B > 80 and D > 90) or (A > 60 and D > 60 and C < 40) or (A > 50 and C < 50 and D > 65 and B > 40):
        return 3
    else:
        return 1