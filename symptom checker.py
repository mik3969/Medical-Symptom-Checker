
print("Welcome! This app is designed to for anyone who is believed to have contracted Covid-19. A list of symptoms will appear to help with the diagnosis")

symptom_list = ["Fever,Cough,Shortness of breath,Tiredness,Aches,Runny Nose,Sore Throat,Headache,Diarrhea, Vomiting"]

print("These are the symptoms most commonly associated with the virus:", symptom_list)

symptoms=[]
patient_symp =[]
symptom1= input("Are you experencing a high fever(A body tempature of 100.0 degrees or more)? (1 for yes) or (0 for No): ")
while True:
    if symptom1 == "1":
        print("A High fever is a sign that you may be infected. We advise for you to regulary check your tempature and seek medical help if needed")
        symptoms += "1"
        patient_symp.append("Fever")
        break
    elif symptom1 == "0":
        break
    else:
        if symptom1 > "1":
            symptom1 = input("Please type either 1 for yes, or , 0 for no: ")
        
symptom2 = input("Have you experienced a dry cough within the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom2 == "1":
        symptoms += "1"
        patient_symp.append("Cough")
        break
    elif symptom2 == "0":
        break
    else:
        if symptom2 > "1":
            symptom2 = input("Please type either 1 for yes, or , 0 for no: ")

symptom3 = input("Have you experienced a shortness of breath within the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom3 == "1":
        symptoms +="1"
        patient_symp.append("Shortness of breath")
        break
    elif symptom3 =="0":
        break
    else:
        if symptom3 >"1":
            symptom3 = input("Please type either 1 for yes, or, 0 for no: ")

symptom4 = input("Have you felt abnormaly tired in the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom4 == "1":
        symptoms +="1"
        patient_symp.append("Tiredness")
        break
    elif symptom4 =="0":
        break
    else:
        if symptom4 >"1":
            symptom4 = input("Please type either 1 for yes, or, 0 for no: ")

symptom5 = input("Have you had any aches recently? (1 for yes) or (0 for no): ")
while True:
    if symptom5 == "1":
        symptoms +="1"
        patient_symp.append("Aches")
        break
    elif symptom5 =="0":
        break
    else:
        if symptom3 >"1":
            symptom3 = input("Please type either 1 for yes, or, 0 for no: ")

#Print out the symptom list
#If patient has >3 of the symptoms , bring up a message
#If patient has "fever" bring up alternative message, asking if X has been near an infected location or person



    