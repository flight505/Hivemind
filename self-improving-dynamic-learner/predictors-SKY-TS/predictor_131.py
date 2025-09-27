"""
Predictor 131
Generated on: 2025-09-09 20:17:06
Accuracy: 49.24%
"""


# PREDICTOR 131 - Accuracy: 49.24%
# Correct predictions: 4924/10000 (49.24%)

def predict_output(A, B, C, D, E):
    sum_be = B + E
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if A > 80 or sum_be > 150:
                    return 2
                elif sum_be < 100:
                    return 1
                else:
                    return 4
        else:
            if D + C > 120:
                return 2
            else:
                return 1
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                if D < 20:
                    return 3
                elif B > 65:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                diff_de = D - E
                if B > 30 and C > 20 and E < 70 and D < 60:
                    return 1
                elif D > 70 or diff_de > 20:
                    return 3
                elif E > 60 or diff_de < -30:
                    return 4
                else:
                    return 3