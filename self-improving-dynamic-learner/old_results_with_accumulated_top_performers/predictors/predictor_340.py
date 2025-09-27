"""
Predictor 340
Generated on: 2025-09-09 08:50:58
Accuracy: 12.25%
"""


# PREDICTOR 340 - Accuracy: 12.25%
# Correct predictions: 1225/10000 (12.25%)

def predict_output(A, B, C, D, E):
    if C > B + D + E:
        return 1
    elif B > A + C + D + E:
        return 2
    elif D > A + B + C + E:
        return 4
    else:
        return 3