"""
Predictor 60
Generated on: 2025-09-09 23:24:50
Accuracy: 53.69%
"""


# PREDICTOR 60 - Accuracy: 53.69%
# Correct predictions: 5369/10000 (53.69%)

def predict_output(A, B, C, D, E):
    if A > 90 and E < 10:
        return 2
    if B > 90 and E < 20:
        return 2
    if D < 20 and E < 20 and C > 60:
        return 3
    if A < 10 and B > 70:
        return 4
    if C < 15 and E > 80:
        return 4
    if A > 90 and B > 90:
        return 4
    if B > 80 and D < 25 and E > 80:
        return 4
    if E < 20 and C > 50 and D > 50:
        return 4
    else:
        return 1