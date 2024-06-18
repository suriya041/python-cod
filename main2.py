import smtplib
import datetime

def send_email(total):

    
    # Get the current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        receiver_email = "lovelyboy16113@gmail.com"
        for i in receiver_email:
          s= smtplib.SMTP('smtp.gmail.com', 587)
          s.starttls()
          s.login("sender_emai", "password")
        message=f"your bill is {total}"
        s.sendmai("sendeer_mailid",i,message)
        s.quit()
        print("Email sent successfully!")
    except :
        print("mail is no send")
send_email()

def main():
    print("** welcome to suriya super market **")
    print("** available products **")

    with open("menu.txt", "r") as f:
        print(f.read())

    def fruits():
        apple_per_kg = 30
        orange_per_kg = 40
        banana_per_kg = 20
        mango_per_kg = 30
        fruit = input("Enter fruits name: ")
        how_kg = int(input("How many kg you want? "))
        
        if fruit == "apple":
            total = apple_per_kg * how_kg
        elif fruit == "orange":
            total = orange_per_kg * how_kg
        elif fruit == "banana":
            total = banana_per_kg * how_kg
        elif fruit == "mango":
            total = mango_per_kg * how_kg
        else:
            print("Sorry, we don't have that fruit.")
            return
        
        print(f"Your total bill is {total}")
        with open("bill.txt", "w") as f:
            f.write(f"Your bill amount is {total}\n")
        
        # Send the email with the bill
        send_email(total)

    def vegetables():
         tomato_per_kg= 35
         carrot_per_kg = 70
         onion_per_kg = 50
         potato_per_kg = 45
         fruit = input("Enter vegetables name: ")
         how_kg = int(input("How many kg you want? "))
        
         if fruit == "tomato":
            total = tomato_per_kg * how_kg
         elif fruit == "carrot":
            total = carrot_per_kg * how_kg
         elif fruit == "onion":
            total = onion_per_kg * how_kg
         elif fruit == "potato":
            total = potato_per_kg * how_kg
         else:
            print("Sorry, we don't have that vegetable.")
            return
        
         print(f"Your total bill is {total}")
         with open("bill.txt", "w") as f:
            f.write(f"Your bill amount is {total}\n")
        
        

    choice = input("Do you want to continue (yes/no)? ").lower()
    if choice == "yes":
        section = input("Do you want to buy fruits or vegetables? ").lower()
        if section == "fruits":
            fruits()
        elif section == "vegetables":
            vegetables()
        else:
            print("Invalid choice!")
    else:
        print("Thank you for visiting!")

if __name__== "__main__":
    main()