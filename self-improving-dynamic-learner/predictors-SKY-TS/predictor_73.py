"""
Predictor 73
Generated on: 2025-09-09 19:45:42
Accuracy: 54.82%
"""


# PREDICTOR 73 - Accuracy: 54.82%
# Correct predictions: 5482/10000 (54.82%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 80:
                    return 4
                else:
                    return 1
            else:
                if E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 2
            else:
                if E <= 25:
                    return 1
                elif D > 90:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if A > 90 or D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    if A < 50:
                        return 2
                    else:
                        return 4
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    if B > 50:
                        return 3
                    else:
                        if E < 5:
                            return 4
                        else:
                            return 1
                else:
                    if E < 10:
                        return 4
                    else:
                        return 3
            else:
                if E > 45 and D < 40:
                    return 4
                elif D > 50:
                    if E <= 40:
                        if C < 10:
                            return 3
                        else:
                            return 1
                    elif B < 40:
                        if B < 20:
                            return 1
                        else:
                            return 3
                    else:
                        return 3
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3