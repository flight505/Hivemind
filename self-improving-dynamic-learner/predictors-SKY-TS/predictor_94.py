"""
Predictor 94
Generated on: 2025-09-09 19:57:12
Accuracy: 44.52%
"""


# PREDICTOR 94 - Accuracy: 44.52%
# Correct predictions: 4452/10000 (44.52%)

def predict_output(A, B, C, D, E):
    sum_abe = A + B + E
    if B >= 80:
        if C < 50:
            if D < (B / 3):
                return 1
            elif E > 80:
                return 2
            else:
                return 4
        else:
            if sum_abe > 150:
                return 3
            else:
                return 2
    else:
        if C >= 50:
            if E < 20:
                return 4
            elif D < 30:
                if E < 40:
                    return 4
                else:
                    if B < 40:
                        return 2
                    else:
                        return 1
            else:
                return 1
        else:
            if A > 70 and D > 60 and E > 70:
                return 4
            elif A < 20 or B >= 70 or E < 20:
                return 1
            else:
                return 3