"""
Predictor 1415
Generated on: 2025-09-10 02:26:25
Accuracy: 45.13%
"""


# PREDICTOR 1415 - Accuracy: 45.13%
# Correct predictions: 4513/10000 (45.13%)

def predict_output(A, B, C, D, E):
    if (E < 30 and (B > 60 or C > 60)) or (E > 90 and D < 30) or (D > 90 and E > 80):
        return 4
    elif B > 75 and C > 55 and E < 40:
        return 2
    elif D < 20 and E > 20 and (A > 60 or (B > 70 and C > 80)):
        return 3
    else:
        return 1