"""
Predictor 860
Generated on: 2025-09-09 21:32:05
Accuracy: 55.18%
"""


# PREDICTOR 860 - Accuracy: 55.18%
# Correct predictions: 5518/10000 (55.18%)

def predict_output(A, B, C, D, E):
    if C > 85 and E > 90:
        return 1
    if C <= 20 and E > 60:
        return 4
    if B > 60 and C > 75 and E >= 70:
        return 2
    if 50 < B < 70 and 50 < C < 70 and E > 80:
        return 2
    if B < 25 and C < 15 and E < 60:
        return 3
    if B > 60 and C < 60 and E < 40:
        return 3
    if 30 <= B <= 60 and C > 70 and E < 30:
        return 3
    return 1