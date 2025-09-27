"""
Predictor 18
Generated on: 2025-09-09 19:07:34
Accuracy: 50.75%
"""


# PREDICTOR 18 - Accuracy: 50.75%
# Correct predictions: 5075/10000 (50.75%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            elif E < 25:
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
                    if B >= 75:
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D > 50:
                    if D > 95:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if E > 70:
                    return 2
                elif D > 50:
                    if A <= 40:
                        return 3
                    else:
                        if E > 55:
                            return 3
                        else:
                            return 1
                elif E > 45 and D < 40:
                    return 4
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3