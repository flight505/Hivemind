"""
Predictor 82
Generated on: 2025-09-09 19:50:47
Accuracy: 38.53%
"""


# PREDICTOR 82 - Accuracy: 38.53%
# Correct predictions: 3853/10000 (38.53%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 50:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if D > 70:
                        return 4
                    else:
                        return 1
                else:
                    if C > 20 and E < 30:
                        return 2
                    else:
                        return 4
        else:
            if D < 50:
                return 1
            else:
                if E < 10:
                    return 3
                elif E < 50 or E > 70:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if A < 30:
                        return 3
                    else:
                        return 4
            else:
                if B < 50:
                    return 3
                else:
                    if D > 80 and E < 70:
                        return 3
                    else:
                        return 1
        else:
            if E < 20:
                if D < 40:
                    if E < 5:
                        return 3
                    else:
                        return 4
                else:
                    if B > 70:
                        return 3
                    else:
                        return 1
            else:
                if C < 10 and E > 70:
                    return 4
                if C < 15 and D < 10:
                    return 1
                elif D > 80 and E > 80:
                    if C > 40:
                        return 3
                    else:
                        return 4
                elif E > 90:
                    if D > 90:
                        return 4
                    else:
                        return 1
                elif B > 70:
                    return 1
                elif B < 50 and D > 80:
                    return 1
                elif A > 80 and D < 50:
                    return 1
                elif E > 80 and D < 30:
                    return 2
                else:
                    return 3