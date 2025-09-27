"""
Predictor 762
Generated on: 2025-09-09 20:28:56
Accuracy: 55.08%
"""


# PREDICTOR 762 - Accuracy: 55.08%
# Correct predictions: 5508/10000 (55.08%)

def predict_output(A, B, C, D, E):
    if B < 60 and ((C < 25 and E > 70) or (C > 60 and E < 25)):
        return 4
    if C < 15 and (B < 20 or (B > 55 and E < 25)):
        return 3
    if A < 50 and B > 50 and E >= 30 and not (C < 30 and D > 80):
        return 2
    return 1