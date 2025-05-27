letters = True

while letters:
    moreLetters = input("More Letters? ")
    if moreLetters.lower() == "no":
        letters = False
        break

    letterType = input("Job Offer or Rejection? ")

    if letterType.lower() == "job offer":
        while True:
            firstName = input("First Name: ")
            if 2 <= len(firstName) <= 10 and firstName.isalpha() and firstName[0].isupper():
                break
            else:
                print("Input Error")
        while True:
            lastName = input("Last Name: ")
            if 2 <= len(lastName) <= 10 and lastName.isalpha() and lastName[0].isupper():
                break
            else:
                print("Input Error")
        while True:
            jobTitle = input("Job Title: ")
            if len(jobTitle) >= 10 and all(char.isalpha() or char.isspace() for char in jobTitle):
                break
            else:
                print("Input Error")
        while True:
            annualSalary = input("Annual Salary: ")
            try:
                x = annualSalary.replace(".", "")
                x = x.replace(",", ".")
                x = float(x)
                if (20000.00 <= x <= 80000.00):
                    break
            except ValueError:
                print("Input Error")
            else:
                print("Input Error")
        while True:
            startDate = input("Start Date: ")
            try:
                year, month, day = map(int, startDate.split("-"))
                if year in [2021, 2022] and 1 <= month <= 12 and 1 <= day <= 31:
                    break
                else:
                    print("Input Error")
            except ValueError:
                print("Input Error")
        print("Here is the final letter to send:")
        print(f"Dear {firstName} {lastName},")
        print(f"After careful evaluation of your application for the position of {jobTitle},")
        print(f"we are glad to offer you the job. Your salary will be {annualSalary} euro annually.")
        print(f"""Your start date will be on {startDate}.
        Please do not hesitate to contact us with any questions.""")
        print("Sincerely,")
        print("HR Department of XYZ")
    elif letterType.lower() == "rejection":
        while True:
            firstName = input("First Name: ")
            if 2 <= len(firstName) <= 10 and firstName.isalpha() and firstName[0].isupper():
                break
            else:
                print("Input Error")
        while True:
            lastName = input("Last Name: ")
            if 2 <= len(lastName) <= 10 and lastName.isalpha() and lastName[0].isupper():
                break
            else:
                print("Input Error")
        while True:
            jobTitle = input("Job Title: ")
            if len(jobTitle) >= 10 and any(char.isalpha() for char in jobTitle):
                break
            else:
                print("Input Error")
        feedback = input("Feedback: ").lower()
        if feedback == "yes":
            message = input("Enter your Feedback (One Statement): ")
            print("Here is the final letter to send:")
            print(f"Dear {firstName} {lastName},")
            print(f"After careful evaluation of your application for the position of {jobTitle},")
            print("at this moment we have decided to proceed with another candidate.")
            print("Here we would like to provide you our feedback about the interview.")
            print(message)
            print("""We wish you the best in finding your future desired career.
            Please do not hesitate to contact us with any questions.""")
            print("Sincerely,")
            print("HR Department of XYZ")
        else:
            print("Here is the final letter to send:")
            print(f"Dear {firstName} {lastName},")
            print(f"After careful evaluation of your application for the position of {jobTitle},")
            print("at this moment we have decided to proceed with another candidate.")
            print("""We wish you the best in finding your future desired career.
            Please do not hesitate to contact us with any questions.""")
            print("Sincerely,")
            print("HR Department of XYZ")
