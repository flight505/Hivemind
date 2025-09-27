"""
Predictor 55
Generated on: 2025-09-09 19:33:57
Accuracy: 49.65%
"""


# PREDICTOR 55 - Accuracy: 49.65%
# Correct predictions: 4965/10000 (49.65%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if (E + C) / 2 > 30 or D > 60:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            elif D > 95 or (A + E) < 80:
                return 3
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if D >= 50:
                    return 1
                else:
                    if B + A < 80:
                        return 4
                    else:
                        return 1
            else:
                if D < 20:
                    return 3
                elif (B + E) > 140:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                if D >= 50:
                    if B < 20:
                        return 1
                    else:
                        return 3
                else:
                    return 4
            else:
                if A > 50 and D < 50 and E > 40:
                    return 1
                elif E > 70 or (D + E) > 120:
                    return 4
                else:
                    return 3