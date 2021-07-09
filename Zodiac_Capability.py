##
#Zodiac Capatibility
#
# @Author Saillesh
# @date 10/22/2019
# @course ICs 3UC




#Subprogram fro Get Birthday

def getBirthday():
    day = 1
    month=1
    #Ask user for Day and Month
    valid = False
    while(not valid):
        try:

            day = int(input("What is your Birth Day?: "))
            if(day <32):
                valid = True

            else:
                print("Plese enter the day in number form (range from 1-31) ")
        except:
            print("Enter something valid")
  #Ask user for thier brith month
    valid = False
    while(not valid):
        try:
            month = int(input("What is your Birth Month?: "))
            if(month<13):
                valid = True
            else:
                print("Plese enter the month in number formd. Ex:(jan=1, Feb=2)")
        except:
            print("Enter something valid")
    return month,day    














#Subprogram for Get Zodiac

def getZodiac(month,day):

    result = "result"

    if (month == 1):
        if(day < 20):
            result = "Sagittarius"
        else:
            result = "Capricorn"

    elif(month == 2):
        if (day < 16):
            result = "Capricorn"

        else:
            result = "Aquarius"

    elif(month == 3):
        if (day < 11):
            result = "Aquarius"

        else:
            result = "Pisces"


    elif(month == 4):
        if (day < 18):
            result = "Pisces"

        else:
            result = "Aries"

    elif(month == 5):
        if (day < 13):
            result = "Aries"

        else:
            result = "Taurus"

    elif(month == 6):
        if (day < 21):
            result = "Taurus"

        else:
            result = "Gemini"

    elif(month == 7):
        if (day < 20):
            result = "Gemini"

        else:
            result = "Cancer"

    elif(month == 8):
        if (day < 20):
            result = "Cancer"

        else:
            result = "Leo"

    elif(month == 9):
        if (day < 16):
            result = "Leo"
        else:
            result = "Virgo"

    elif(month == 10):
        if (day < 30):
            result = "Virgo"
        else:
            result = "Libra"

    elif(month == 11):
        if (day < 23):
            result = "Libra"

        elif(day < 29):
            result = "Scorpio"

        else:
            result = "Ophiuchus"

    elif(month == 12):
        if (day < 17):
            result = "Ophiuchus"

        elif(day < 31):
            result = "Sagittarius"

    return result




#Subprogram for Compatibility
def getCompatability(sign):


    fire = ["Aries" , "Leo", "Sagittarius"]
    water = ["Pisces", "Cancer", "Scorpio", "Ophiuchus"]
    air = ["Gemini", "Aquarius", "Libra"]
    earth = ["Capricorn" , "Taurus" , "Virgo"]

    if (sign1==sign2):
       element = "Compatibe"

    elif(sign1 in fire and sign2 in fire):
        element = "Compatible"

    elif (sign1 in water and sign2 in water):
        element = "Compatible"

    elif (sign1 in earth and earth in fire):
        element = "Compatible"

    elif (sign1 in air and earth in air):
        element = "Compatible"

    else:
        element = "Not Comaptible"

    return  element



#main
if __name__=="__main__":
    #get Birthday From Person 1
    month1,day1 = getBirthday()
    #get Birthday From Person 1

    month2,day2 = getBirthday()

    #Get Zodiac Sign
    sign1 = getZodiac(month1,day1)
    sign2 = getZodiac(month2,month2)


    #Determind Capatibility
    element = getCompatability(sign1)
    print(sign1 + " and " +  sign2 + " are: " + element)