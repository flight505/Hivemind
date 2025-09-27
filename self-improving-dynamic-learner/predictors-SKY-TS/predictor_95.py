"""
Predictor 95
Generated on: 2025-09-09 19:57:12
Accuracy: 30.61%
"""


# PREDICTOR 95 - Accuracy: 30.61%
# Correct predictions: 3061/10000 (30.61%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 20:
            if D < 30 and E < 20:
                return 1
            elif E > 50:
                return 2
            else:
                return 4
        else:
            if C > 70:
                return 2
            else:
                return 4
    else:
        if C > 50:
            if E > 50:
                if B > 50:
                    return 1
                else:
                    return 2
            else:
                return 4
        else:
            if B >= 70:
                return 1
            elif E < 20:
                return 1
            elif B < 20 and D > 60:
                return 1
            elif A > 70 and E > 70:
                return 4
            elif E > 80:
                return 1
            else:
                return 3