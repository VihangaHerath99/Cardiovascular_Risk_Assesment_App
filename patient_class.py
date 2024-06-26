

class Patient:
    def __init__(self, name=None, age=None, is_Male=None, diabetes_status=None, smoking_status=None, blood_pressure=None, cholesterol=None):
        self.name = name
        self.age = age
        self.is_Male = is_Male
        self.diabetes_status = diabetes_status
        self.smoking_status = smoking_status
        self.blood_pressure = blood_pressure
        self.cholesterol = cholesterol

    def risk_level(self):
        if self.cholesterol == 4:
            if self.blood_pressure >= 180:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("1")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("2")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("3")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("4")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("5")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("6")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("7")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("8")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("9")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("10")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("11")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("12")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("13")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("14")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("15")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("16")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("17")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("18")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("19")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("20")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("21")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("22")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("23")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("24")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("25")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("26")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("27")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("28")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("29")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("30")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("31")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("32")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 160:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("33")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("34")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("35")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("36")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("37")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("38")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("39")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("40")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("41")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("42")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("43")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("44")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("45")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("46")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("47")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("48")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("49")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("50")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("51")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("52")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("53")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("54")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("55")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("56")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("57")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("58")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("59")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("60")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("61")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("62")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("63")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("64")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 140:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("65")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("66")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("67")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("68")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("69")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("70")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("71")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("72")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("73")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("74")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("75")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("76")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("77")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("78")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("79")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("80")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("81")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("82")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("83")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("84")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("85")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("86")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("87")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("88")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("89")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("90")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("91")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("92")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("93")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("94")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("95")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("96")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 120:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("97")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("98")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("99")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("100")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("101")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("102")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("103")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("104")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("105")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("106")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("107")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("108")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("109")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("110")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("111")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("112")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("113")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("114")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("115")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("116")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("117")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("118")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("119")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("120")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("121")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("122")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("123")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("124")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("125")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("126")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("127")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("128")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            else: raise ValueError("Invalid input for self.blood_pressure (rannge>=120) or not defined")
        elif self.cholesterol == 5:
            if self.blood_pressure >= 180:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("129")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("130")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("131")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("132")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("133")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("134")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("135")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("136")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("137")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("138")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("139")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("140")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("141")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("142")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("143")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("144")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("145")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("146")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("147")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("148")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("149")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("150")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("151")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("152")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("153")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("154")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("155")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("156")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("157")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("158")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("159")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("160")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 160:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("161")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("162")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("163")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("164")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("165")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("166")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("167")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("168")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("169")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("170")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("171")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("172")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("173")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("174")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("175")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("176")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("177")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("178")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("179")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("180")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("181")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("182")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("183")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("184")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("185")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("186")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("187")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("188")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("189")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("190")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("191")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("192")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 140:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("193")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("194")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("195")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("196")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("197")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("198")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("199")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("200")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("201")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("202")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("203")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("204")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("205")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("206")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("207")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("208")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("209")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("210")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("211")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("212")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("213")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("214")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("215")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("216")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("217")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("218")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("219")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("220")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("221")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("222")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("223")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("224")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 120:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("225")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("226")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("227")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("228")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("229")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("230")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("231")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("232")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("233")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("234")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("235")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("236")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("237")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("238")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("239")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("240")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("241")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("242")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("243")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("244")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("245")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("246")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("247")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("248")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("249")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("250")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("251")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("252")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("253")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("254")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("255")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("256")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            else: raise ValueError("Invalid input for self.blood_pressure (rannge>=120) or not defined")
        elif self.cholesterol == 6:
            if self.blood_pressure >= 180:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("257")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("258")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("259")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("260")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("261")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("262")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("263")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("264")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("265")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("266")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("267")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("268")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("269")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("270")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("271")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("272")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("273")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("274")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("275")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("276")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("277")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("278")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("279")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("280")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("281")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("282")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("283")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("284")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("285")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("286")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("287")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("288")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 160:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("289")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("290")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("291")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("292")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("293")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("294")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("295")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("296")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("297")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("298")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("299")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("300")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("301")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("302")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("303")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("304")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("305")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("306")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("307")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("308")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("309")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("310")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("311")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("312")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("313")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("314")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("315")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("316")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("317")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("318")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("319")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("320")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 140:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("321")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("322")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("323")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("324")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("325")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("326")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("327")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("328")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("329")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("330")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("331")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("332")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("333")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("334")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("335")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("336")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("337")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("338")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("339")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("340")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("341")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("342")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("343")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("344")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("345")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("346")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("347")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("348")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("349")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("350")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("351")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("352")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 120:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("353")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("354")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("355")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("356")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("357")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("358")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("359")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("360")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("361")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("362")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("363")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("364")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("365")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("366")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("367")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("368")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("369")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("370")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("371")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("372")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("373")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("374")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("375")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("376")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("377")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("378")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("379")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("380")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("381")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("382")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("383")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("384")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            else: raise ValueError("Invalid input for self.blood_pressure (rannge>=120) or not defined")
        elif self.cholesterol == 7:
            if self.blood_pressure >= 180:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("385")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("386")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("387")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("388")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("389")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("390")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("391")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("392")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("393")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("394")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("395")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("396")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("397")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("398")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("399")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("400")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("401")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("402")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("403")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("404")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("405")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("406")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("407")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("408")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("409")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("410")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("411")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("412")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("413")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("414")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("415")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("416")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 160:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("417")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("418")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("419")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("420")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("421")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("422")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("423")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("424")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("425")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("426")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("427")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("428")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("429")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("430")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("431")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("432")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("433")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("434")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("435")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("436")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("437")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("438")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("439")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("440")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("441")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("442")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("443")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("444")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("445")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("446")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("447")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("448")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 140:
                if self.age >= 70:
                    ##
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("449")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("450")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("451")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("452")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("453")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("454")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("455")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("456")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("457")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("458")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("459")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("460")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("461")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("462")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("463")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("464")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("465")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("466")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("467")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("468")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("469")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("470")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("471")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("472")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("473")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("474")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("475")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("476")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("477")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("478")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("479")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("480")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 120:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("481")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("482")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("483")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("484")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("485")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("486")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("487")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("488")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("489")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("490")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("491")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("492")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("493")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("494")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("495")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("496")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("497")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("498")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("499")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("500")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("501")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("502")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("503")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("504")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("505")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("506")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("507")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("508")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("509")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("510")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("511")
                                return "green"
                            elif self.smoking_status == False: # non-smoker
                                print("512")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            else: raise ValueError("Invalid input for self.blood_pressure (rannge>=120) or not defined")
        elif self.cholesterol == 8:
            if self.blood_pressure >= 180:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("513")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("514")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("515")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("516")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("517")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("518")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("519")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("520")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("521")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("522")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("523")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("524")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("525")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("526")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("527")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("528")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("529")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("530")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("531")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("532")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("533")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("534")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("535")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("536")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("537")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("538")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("539")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("540")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("541")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("542")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("543")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("544")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 160:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("545")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("546")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("547")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("548")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("549")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("550")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("551")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("552")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("553")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("554")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("555")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("556")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("557")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("558")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("559")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("560")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("561")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("562")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("563")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("564")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("565")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("566")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("567")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("568")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("569")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("570")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("571")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("572")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("573")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("574")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("575")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("576")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 140:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("577")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("578")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("579")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("580")
                                return "brown"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("581")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("582")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("583")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("584")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("585")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("586")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("587")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("588")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("589")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("590")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("591")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("592")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("593")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("594")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("595")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("596")
                                return "red"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("597")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("598")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("599")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("600")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("601")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("602")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("603")
                                return "brown"
                            elif self.smoking_status == False: # non-smoker
                                print("604")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("605")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("606")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("607")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("608")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            elif self.blood_pressure >= 120:
                if self.age >= 70:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("609")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("610")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("611")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("612")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("613")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("614")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("615")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("616")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 60:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("617")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("618")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("619")
                                return "red"
                            elif self.smoking_status == False: # non-smoker
                                print("620")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("621")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("622")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("623")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("624")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 50:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("625")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("626")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("627")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("628")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("629")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("630")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("631")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("632")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                elif self.age >= 40:
                    if self.diabetes_status == True: # having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("633")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("634")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("635")
                                return "orange"
                            elif self.smoking_status == False: # non-smoker
                                print("636")
                                return "orange"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    elif self.diabetes_status == False: # not-having diabetes
                        if self.is_Male == True: # Male
                            if self.smoking_status == True: # smoker
                                print("637")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("638")
                                return "green"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        elif self.is_Male == False: # Female
                            if self.smoking_status == True: # smoker
                                print("639")
                                return "yellow"
                            elif self.smoking_status == False: # non-smoker
                                print("640")
                                return "yellow"
                            else: raise ValueError("self.smoking_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                        else: raise ValueError("self.is_Male is a logical (True/False) variable. It is not defined or incorrectly defined")
                    else: raise ValueError("self.diabetes_status is a logical (True/False) variable. It is not defined or incorrectly defined")
                else: raise ValueError("Invalid input for self.age (rannge>=40) or not defined")
            else: raise ValueError("Invalid input for self.blood_pressure (rannge>=120) or not defined")
        else: raise ValueError("Invalid input for self.cholesterol (4<=rannge<=8) or not defined")




if __name__ == "__main__":
    # Creating a patient object
    patient1 = Patient(name="John", age=45, is_Male=True, diabetes_status=False, smoking_status=False, blood_pressure=170, cholesterol=5)

    # Accessing patient attributes
    print("Patient Name:", patient1.name)
    print("Patient Age:", patient1.age)
    print("Patient is_Male:", patient1.is_Male)
    print("Patient Diabetes Status:", patient1.diabetes_status)
    print("Patient Smoking Status:", patient1.smoking_status)
    print("Patient Blood Pressure:", patient1.blood_pressure)
    print("Patient Cholesterol Level:", patient1.cholesterol)

    patient1.risk_level()