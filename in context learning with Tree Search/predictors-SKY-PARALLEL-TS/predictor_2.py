"""
Predictor 2
Generated on: 2025-09-09 23:16:45
Accuracy: 36.62%
"""


# PREDICTOR 2 - Accuracy: 36.62%
# Correct predictions: 3662/10000 (36.62%)

def predict_output(A, B, C, D, E):
    ratio_ac_bd = (A + C) / (B + D)
    if ratio_ac_bd < 0.5:
        return 4
    elif A * E > 5000:
        return 2
    elif B - C < -40:
        return 3
    else:
        return 1