"""
Predictor 995
Generated on: 2025-09-10 01:13:58
Accuracy: 52.11%
"""


# PREDICTOR 995 - Accuracy: 52.11%
# Correct predictions: 5211/10000 (52.11%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20 and C > 5) or
        (C < 15 and D > 90) or
        (A > 60 and B < 15 and C < 20 and D > 60 and E < 15)):
        return 4
    elif ((A > 90 and E < 10 and C < 25) or
          (B > 65 and D < 20 and E > 50) or
          (A > 60 and E < 10 and B > 50 and C < 50 and D < 50)):
        return 2
    elif ((A < 10 and B > 70 and C < 5 and E > 20) or
          (C > 90 and D < 5) or
          (C > 90 and D > 70) or
          (B > 80 and D > 85) or
          (A < 50 and B > 60 and C > 90 and D > 70)):
        return 3
    else:
        return 1