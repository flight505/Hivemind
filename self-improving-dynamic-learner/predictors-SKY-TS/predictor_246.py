"""
Predictor 246
Generated on: 2025-09-09 21:15:09
Accuracy: 41.04%
"""


# PREDICTOR 246 - Accuracy: 41.04%
# Correct predictions: 4104/10000 (41.04%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if D < 50:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                return 3