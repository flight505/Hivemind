"""
Predictor 163
Generated on: 2025-09-09 20:33:55
Accuracy: 61.93%
"""


# PREDICTOR 163 - Accuracy: 61.93%
# Correct predictions: 6193/10000 (61.93%)

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
                    if D > 80 and C > 35:
                        return 3
                    elif C > 35:
                        return 2
                    else:
                        if A < 20:
                            return 1
                        else:
                            return 4
                elif E > 50 and C < 40:
                    if C > 25:
                        return 4
                    else:
                        return 2
                else:
                    if E < 40:
                        return 1
                    else:
                        return 2
        else:
            if D < 50:
                return 1
            else:
                if D > 90:
                    return 2
                elif E < 20:
                    return 4
                elif E <= 25 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if B >= 70 and E >= 10:
                    return 1
                elif B >= 70:
                    if E < 10:
                        return 1
                    else:
                        return 4
                else:
                    if A > 90 or D > 50:
                        return 1
                    elif D < 20 and E < 10:
                        return 3
                    else:
                        return 4
            else:
                if D < 20:
                    if A < 50:
                        return 2
                    elif E < 30:
                        return 3
                    elif E > 50:
                        return 1
                    else:
                        return 4
                else:
                    if B >= 75:
                        if D > 80 and E > 80:
                            return 3
                        else:
                            return 2
                    else:
                        if D <= 45 and C > 50 and E < 30:
                            return 4
                        elif D < 30 and E < 30 and C > 70:
                            return 4
                        else:
                            return 1
        else:
            if E < 20:
                if D > 50:
                    if E < 5:
                        return 4
                    elif B > 50 or C < 10:
                        return 3
                    else:
                        return 1
                else:
                    if A > 50:
                        return 1
                    else:
                        return 3
            else:
                if E > 45 and D < 40:
                    if E > 70:
                        return 4
                    elif C < 5:
                        return 4
                    elif B > 40:
                        return 1
                    else:
                        return 2
                elif D > 50:
                    if E <= 40:
                        if B < 50 and C < 20:
                            return 4
                        elif A > 90 and D > 70:
                            return 3
                        else:
                            return 1
                    elif B < 40:
                        if A < 10:
                            return 1
                        elif C < 10:
                            return 4
                        else:
                            return 1
                    else:
                        if C < 20:
                            return 4
                        elif D > 90 and E > 80:
                            return 3
                        elif A > 80 or C < 20:
                            return 3
                        elif B > 70 and D > 70 and E > 40:
                            return 3
                        else:
                            return 1
                else:
                    if C > 20:
                        if E > 70:
                            return 2
                        else:
                            if D < 25 and E < 40:
                                return 3
                            elif D < 25 and E < 50:
                                return 4
                            else:
                                return 1
                    else:
                        if E > 70:
                            return 4
                        else:
                            return 3