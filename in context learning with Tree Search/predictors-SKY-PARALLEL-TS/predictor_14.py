"""
Predictor 14
Generated on: 2025-09-09 23:16:45
Accuracy: 44.18%
"""


# PREDICTOR 14 - Accuracy: 44.18%
# Correct predictions: 4418/10000 (44.18%)

def predict_output(A, B, C, D, E):
    if (B > 60 and E < 20) or (D > 80 and E > 80):
        return 4
    elif A > 80 and E > 50:
        return 2
    elif C < 10 and A > 60:
        return 3
    else:
        return 1