"""
Predictor 1331
Generated on: 2025-09-10 02:07:02
Accuracy: 52.00%
"""


# PREDICTOR 1331 - Accuracy: 52.00%
# Correct predictions: 5200/10000 (52.00%)

def predict_output(A, B, C, D, E):
    if (E < 20 and (C > 25 or (A < 10 and B > 70))) or (C < 15 and D > 80 and E > 50):
        return 4
    elif C > 60 and D < 15:
        return 2
    elif A > 90 and D > 80 and E > 50:
        return 3
    else:
        return 1