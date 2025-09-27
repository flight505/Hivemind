"""
Predictor 1427
Generated on: 2025-09-10 02:26:25
Accuracy: 52.93%
"""


# PREDICTOR 1427 - Accuracy: 52.93%
# Correct predictions: 5293/10000 (52.93%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 30 and E > 80) or (C < 25 and D > 90) or (E > 90) or (C > 30 and E < 20 and D > 30):
        return 4
    elif (B < 20 and C > 70 and D < 20 and E > 70):
        return 2
    elif (B > 70 and C > 70 and D > 80) or (A > 50 and C < 50 and D > 65 and B > 40) or (B < 20 and C > 20 and D < 25) or (A < 40 and B > 70 and C > 70):
        return 3
    else:
        return 1