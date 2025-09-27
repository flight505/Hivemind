"""
Predictor 306
Generated on: 2025-09-09 21:43:06
Accuracy: 63.66%
"""


# PREDICTOR 306 - Accuracy: 63.66%
# Correct predictions: 6366/10000 (63.66%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if C < 10:
                    return 1
                elif E > 50:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if D > 80 and C > 35:
                        return 3
                    elif C > 40:
                        return 2
                    else:
                        if A < 20:
                            return 1
                        else:
                            return 4
                elif E > 50 and C < 40:
                    if D > 90 and E > 90 and A < 25:
                        return 2
                    elif A < 25:
                        return 1
                    else:
                        return 4
                else:
                    if D >= 80 and E < 50:
                        return 4
                    elif C > 30 and E < 40:
                        return 2
                    elif E < 40:
                        return 1
                    elif D > 65 and E > 40 and C < 25:
                        return 4
                    else:
                        return 2
        else:
            if D < 50:
                if E > 80:
                    return 4
                else:
                    return 1
            else:
                if D > 90:
                    if E < 30:
                        return 1
                    elif E > 70:
                        return 1
                    else:
                        return 3
                elif E <= 35 or A > 60:
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
                    if 50 < B < 70 and E < 5 and C > 55:
                        return 2
                    if A > 90 or D > 50:
                        return 1
                    elif D < 20:
                        if E < 5:
                            return 4
                        else:
                            if A > 80:
                                return 1
                            else:
                                return 3
                    else:
                        return 4
            else:
                if D < 25:
                    if A < 50:
                        if D + E < 35 or (A > 30 and E < 40):
                            return 3
                        elif A < 20 and E < 50:
                            if D + E < 50:
                                return 3
                            else:
                                return 4
                        else:
                            if E > 50:
                                return 4
                            else:
                                return 1
                    elif E < 30:
                        return 3
                    elif E > 50:
                        return 1
                    else:
                        if E < 40:
                            return 1
                        else:
                            return 4
                else:
                    if B >= 75:
                        if A > 70 or C > 75:
                            return 1
                        else:
                            return 2
                    else:
                        if D < 40 and C > 60 and E < 35:
                            return 4
                        elif D < 30 and E < 30 and C > 70:
                            return 4
                        else:
                            return 1
        else:
            if E < 20:
                if D > 50:
                    if E < 10:
                        if C < 20:
                            return 1
                        else:
                            return 4
                    elif B > 50 or C < 10:
                        if A > 80:
                            return 2
                        else:
                            return 3
                    else:
                        return 1
                else:
                    if A > 50:
                        if D < 20 and E < 15:
                            return 3
                        else:
                            return 1
                    else:
                        if D > 40 and E < 10:
                            return 4
                        else:
                            return 3
            else:
                if E > 45 and D < 40:
                    if E > 70:
                        if A > 90:
                            return 4
                        elif B < 50:
                            return 1
                        else:
                            if B > 50:
                                if C > 30:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 4
                    elif C < 5:
                        return 4
                    elif A > 70 and B < 20 and C < 20:
                        return 4
                    elif B > 40 or C > 45:
                        return 1
                    else:
                        return 1
                elif D > 50:
                    if E <= 40:
                        if B < 50 and C < 20:
                            if D > 75:
                                return 3
                            else:
                                return 4
                        elif C > 35 and E < 25:
                            if B >= 70:
                                return 2
                            else:
                                return 4
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
                            if E > 90:
                                return 2
                            else:
                                return 4
                        elif D > 90 and E > 80:
                            return 3
                        elif A > 80 or C < 20:
                            return 3
                        else:
                            return 1
                else:
                    if A > 70:
                        return 1
                    else:
                        if C > 20:
                            if E > 70 and B >= 20:
                                return 2
                            elif E > 70:
                                return 1
                            else:
                                if D < 25 and E < 40:
                                    if B > 50:
                                        return 1
                                    else:
                                        return 3
                                elif D < 30 and E < 45:
                                    if B >= 40:
                                        return 4
                                    else:
                                        return 3
                                else:
                                    return 1
                        else:
                            if E > 70:
                                return 4
                            elif C < 20 and E > 50:
                                return 4
                            else:
                                if D < 10 and C < 15 and B > 75:
                                    return 1
                                else:
                                    return 3