"""
Predictor 12
Generated on: 2025-09-09 17:12:00
Accuracy: 58.08%
"""


# PREDICTOR 12 - Accuracy: 58.08%
# Correct predictions: 5808/10000 (58.08%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if B + C > 140 and A < 40:
        return 2
    if B + C < 30 and E < 40:
        return 3
    return 1