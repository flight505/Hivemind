"""
Predictor 298
Generated on: 2025-09-09 07:38:42
Accuracy: 49.69%
"""


# PREDICTOR 298 - Accuracy: 49.69%
# Correct predictions: 4969/10000 (49.69%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif E > 80:
        return 4
    elif B > 70 and C > 60:
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 1