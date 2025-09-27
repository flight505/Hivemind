"""
Predictor 309
Generated on: 2025-09-09 15:19:41
Accuracy: 53.27%
"""


# PREDICTOR 309 - Accuracy: 53.27%
# Correct predictions: 5327/10000 (53.27%)

def predict_output(A, B, C, D, E):
    if B + C < 40:
        return 3
    if E > 90:
        return 4
    if B > 60 and C > 70 and E >= 70:
        return 2
    return 1