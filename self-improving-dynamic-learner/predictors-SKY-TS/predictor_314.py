"""
Predictor 314
Generated on: 2025-09-09 21:46:25
Accuracy: 42.19%
"""


# PREDICTOR 314 - Accuracy: 42.19%
# Correct predictions: 4219/10000 (42.19%)

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
            if D + E > 100:
                return 1
            else:
                return 4
        else:
            if D > 50 and E < 20:
                return 1
            else:
                return 3