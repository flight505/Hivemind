"""
Predictor 230
Generated on: 2025-09-09 21:08:18
Accuracy: 52.96%
"""


# PREDICTOR 230 - Accuracy: 52.96%
# Correct predictions: 5296/10000 (52.96%)

def predict_output(A, B, C, D, E):
    sum_be = B + E
    sum_bc = B + C
    sum_ab = A + B
    sum_cd = C + D
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if sum_be > 90:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if D < 30:
                    return 4
                else:
                    return 1
            else:
                if D >= 50:
                    return 1
                else:
                    if sum_bc > 130:
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D < 50:
                    return 3
                else:
                    return 1
            else:
                if D < 50:
                    if E > 50:
                        if sum_ab > 100:
                            return 1
                        else:
                            return 4
                    else:
                        return 3
                else:
                    if E > 50:
                        if sum_cd > 80:
                            return 3
                        else:
                            return 4
                    else:
                        if B > 60:
                            return 1
                        else:
                            return 3