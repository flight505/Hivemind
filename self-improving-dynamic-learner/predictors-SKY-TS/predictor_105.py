"""
Predictor 105
Generated on: 2025-09-09 20:03:05
Accuracy: 54.93%
"""


# PREDICTOR 105 - Accuracy: 54.93%
# Correct predictions: 5493/10000 (54.93%)

def predict_output(A, B, C, D, E):
    if B >= 70:
        if C >= 50:
            if D > 80:
                return 3
            elif A > 50:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if A < 20 and E > 50:
                    return 1
                elif E < 20 and D > 90 and C > 30:
                    return 3
                else:
                    return 4
    else:
        if C >= 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            elif E >= 60:
                if A > 90:
                    return 3
                else:
                    return 1
            else:
                return 3