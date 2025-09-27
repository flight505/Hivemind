"""
Predictor 56
Generated on: 2025-09-09 19:33:57
Accuracy: 53.23%
"""


# PREDICTOR 56 - Accuracy: 53.23%
# Correct predictions: 5323/10000 (53.23%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 50 or C < 20:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                if E <= 25 or A > 60 or E > 80:
                    return 1
                elif D > 90:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if D >= 50:
                    return 1
                else:
                    if B < 50:
                        return 4
                    else:
                        return 1
            else:
                if D < 20:
                    return 3
                elif B + E > 150:
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
                elif E > 70:
                    return 4
                else:
                    return 3