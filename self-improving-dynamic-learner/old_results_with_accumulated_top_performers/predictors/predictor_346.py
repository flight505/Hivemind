"""
Predictor 346
Generated on: 2025-09-09 09:02:23
Accuracy: 33.84%
"""


# PREDICTOR 346 - Accuracy: 33.84%
# Correct predictions: 3384/10000 (33.84%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    if E == max(A, B, C, D, E):
        return 4
    if C > 70:
        return 2
    return 1