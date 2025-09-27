"""
Predictor 180
Generated on: 2025-09-09 20:44:34
Accuracy: 40.69%
"""


# PREDICTOR 180 - Accuracy: 40.69%
# Correct predictions: 4069/10000 (40.69%)

def predict_output(A, B, C, D, E):
    if C > 80:
        if E < 20:
            if D < 15:
                return 3
            else:
                return 4
        elif B > 90:
            if E > 60:
                return 2
            else:
                return 1
        else:
            return 1
    else:
        if B >= 80:
            if E > 50:
                return 4
            elif D < 40:
                return 1
            else:
                return 4
        else:
            if A > 50 and D < 40:
                return 1
            elif E < 20:
                return 1
            elif B > 70:
                return 2
            elif E > 80 and B < 30:
                return 1
            else:
                return 3