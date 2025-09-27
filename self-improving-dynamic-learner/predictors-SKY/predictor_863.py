"""
Predictor 863
Generated on: 2025-09-09 21:33:32
Accuracy: 31.36%
"""


# PREDICTOR 863 - Accuracy: 31.36%
# Correct predictions: 3136/10000 (31.36%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 30 and E > 80:
        return 4
    if B > 80 or (B + C > 100):
        return 2
    if B > 60 and C > 70:
        return 2
    if B > 50 and C < 50 and E < 50:
        return 3
    if B < 30 and C > 60 and E < 40:
        return 3
    return 1