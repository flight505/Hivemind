"""
Predictor 179
Generated on: 2025-09-09 20:44:34
Accuracy: 40.84%
"""


# PREDICTOR 179 - Accuracy: 40.84%
# Correct predictions: 4084/10000 (40.84%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D >= 30:
                return 4
            else:
                return 1
    else:
        if C >= 50:
            if D >= 50:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            else:
                return 3