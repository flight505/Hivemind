"""
Predictor 859
Generated on: 2025-09-09 21:30:54
Accuracy: 53.49%
"""


# PREDICTOR 859 - Accuracy: 53.49%
# Correct predictions: 5349/10000 (53.49%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90 and C < 25:
        return 4
    elif B > 60 and C > 75:
        return 2
    else:
        return 1