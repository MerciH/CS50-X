import cs50
import array as arr

def main():
    cardN = input("Credit card number: ")
    sum = luhn(cardN)  #luhn formular to get the tota_sum
    mod_sum = sum%10
    if mod_sum == 0:

        #visacard
        if len(cardN)==13 and cardN[0] == '4':
            print("VISA")

        #american express
        elif len(cardN)==15:
            if cardN[0] == '3':
                    if cardN[1] == '4' or cardN[1] == '7':
                        print("AMEX")

        #Visa n master Card
        elif len(cardN)==16:
            if cardN[0] == '4':
                print("VISA")
            elif cardN[0] == '5':
                    if cardN[1] == '1' or cardN[1] =='2' or cardN[1] == '3'or cardN[1] == '4' or cardN[1] =='5':
                        print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")

def luhn(nbr):

    secondLast = 0
    left = 0

    #find the sum
    j = len(nbr)-1
    for i in range(len(nbr)):
        if j == len(nbr)-1:
            j = j-i-1
            m = (int(nbr[j]))*2
            if m > 9:
                n = m%10
                n1 = m//10
                secondLast = secondLast + n1 + n
            else:
                secondLast = secondLast + m

            l = j+1
            left = left + int(nbr[l])

        elif j > 1:
            j = j-2
            m = (int(nbr[j]))*2
            if m > 9:
                n = m%10
                n1 = m//10
                secondLast = secondLast + n1 + n
            else:
                secondLast = secondLast + m

            l = j+1
            left = left + int(nbr[l])

    Total_sum = secondLast + left
    print(Total_sum)
    return Total_sum

main()








