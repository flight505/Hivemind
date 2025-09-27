"""
Predictor 198
Generated on: 2025-09-09 08:02:41
Accuracy: 35.08%
"""


# PREDICTOR 198 - Accuracy: 35.08%
# Correct predictions: 3508/10000 (35.08%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif A > 40 and C < 20:
        return 3
    elif C > 70:
        return 2
    else:
        return 1