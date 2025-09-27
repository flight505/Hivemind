"""
Predictor 130
Generated on: 2025-09-09 20:17:06
Accuracy: 42.15%
"""


# PREDICTOR 130 - Accuracy: 42.15%
# Correct predictions: 4215/10000 (42.15%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if A > 80:
                    return 2
                elif E > 80:
                    return 1
                else:
                    if E > 50 or D > 90:
                        return 4
                    else:
                        return 2
        else:
            if E < 20 or D < 40 or A < 10:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    if E < 50:
                        if B < 30:
                            return 4
                        else:
                            return 3
                    else:
                        return 1
                else:
                    if E < 45:
                        return 4
                    else:
                        if A < 55:
                            return 3
                        else:
                            return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 40:
                    if A < 10:
                        return 2
                    elif E > 50:
                        return 1
                    else:
                        return 3
                else:
                    if B < 10 or (E > 70 and C < 25):
                        return 4
                    else:
                        if D < 45 or E > 65:
                            return 1
                        else:
                            return 3