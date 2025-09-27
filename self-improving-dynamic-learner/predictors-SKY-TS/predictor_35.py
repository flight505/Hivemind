"""
Predictor 35
Generated on: 2025-09-09 19:16:43
Accuracy: 47.40%
"""


# PREDICTOR 35 - Accuracy: 47.40%
# Correct predictions: 4740/10000 (47.40%)

def predict_output(A, B, C, D, E):
    sum_be = B + E
    diff_cd = C - D
    if B >= 80:
        if C < 50:
            if D + E < 60:
                return 1
            else:
                return 4
        else:
            if D > 80 or sum_be > 170:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D > 50:
                return 1
            elif E > 50:
                if D < 20 or diff_cd > 50:
                    return 2
                else:
                    return 1
            else:
                return 4
        else:
            if E < 20:
                if B < 30:
                    return 1
                else:
                    return 4
            else:
                if B >= 70:
                    return 4
                else:
                    if D >= 50:
                        if C + A >= 70:
                            return 1
                        else:
                            return 3
                    else:
                        if B > 50 or C > 25:
                            return 1
                        else:
                            return 3