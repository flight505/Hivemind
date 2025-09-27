"""
Predictor 70
Generated on: 2025-09-09 03:30:08
Accuracy: 44.55%
"""


# PREDICTOR 70 - Accuracy: 44.55%
# Correct predictions: 4455/10000 (44.55%)

def predict_output(A, B, C, D, E):
    # Simple rule based on A+B+C vs D+E
    if A + B + C > D + E:
        if B < 25:
            return 3
        else:
            return 1
    else:
        return 4