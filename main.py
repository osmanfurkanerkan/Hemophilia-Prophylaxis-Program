other_patients=True
Numbers_of_Hemophilia_A=0
Numbers_of_Hemophilia_B=0
total_patients=0
numbers_of_severe=0
numbers_of_moderate=0
numbers_of_mild=0
inhibitorpositive_Hemophilia_A=0
inhibitorpositive_Hemophilia_B=0
numbers_of_prophylaxis_Hemophilia_A=0
numbers_of_prophylaxis_Hemophilia_B=0
numbers_of_prophylaxis_moderate=0
numbers_of_used_recombinant_Hemophilia_A=0
numbers_of_used_plasmaderived_Hemophilia_A=0
numbers_of_used_recombinant_Hemophilia_B=0
numbers_of_used_plasmaderived_Hemophilia_B=0
total_cost_of_patients_4week=0
total_prophylaxis_patients=0
total_IU=0
max_medication_amount_for_4_week_factor8=0
max_medication_amount_for_4_week_factor9=0
highest_medication_cost_for_4_week =0
hemophilia_A_plasma_totalIU,hemophilia_A_plasma_2000,hemophilia_A_plasma_1500,hemophilia_A_plasma_1000,hemophilia_A_plasma_500,hemophilia_A_plasma_250=0,0,0,0,0,0
hemophilia_B_plasma_totalIU,hemophilia_B_plasma_2000,hemophilia_B_plasma_1500,hemophilia_B_plasma_1000,hemophilia_B_plasma_500,hemophilia_B_plasma_250=0,0,0,0,0,0
hemophilia_A_recombinant_totalIU,hemophilia_A_recombinant_2000,hemophilia_A_recombinant_1500,hemophilia_A_recombinant_1000,hemophilia_A_recombinant_500,hemophilia_A_recombinant_250=0,0,0,0,0,0
hemophilia_B_recombinant_totalIU,hemophilia_B_recombinant_2000,hemophilia_B_recombinant_1500,hemophilia_B_recombinant_1000,hemophilia_B_recombinant_500,hemophilia_B_recombinant_250=0,0,0,0,0,0

while other_patients:
    #we take the patient's informations
    ID_number=input("enter the ıd number (11 digit) :")
    name_surname=input("enter the your name and surname :")

    # Prompt the user to enter their factor proteins number (8 or 9).
    # Keep asking until the user enters a valid value (either "8" or "9").
    factor_proteins_number=input("enter your factor proteins number  (8 or 9) ? :")
    while factor_proteins_number!="8" and factor_proteins_number!="9":
        print("Please enter the value 8 or 9.")
        factor_proteins_number=input("enter your factor proteins number  (8 or 9) ? :")

    factor_proteins_number=int(factor_proteins_number)

    #We defined the name of the disease
    if factor_proteins_number==8:
        type_disease="Hemophilia-A"
    if factor_proteins_number==9:
        type_disease="Hemophilia-B"

    if factor_proteins_number==8:
        Numbers_of_Hemophilia_A+=1
        # Protein level in blood (%)
        factor_proteins_8_percantage=float(input("enter your factor protein 8 percentage (0-50) : "))
        while not (0<=factor_proteins_8_percantage<50):
            print("please try enter factor protein 8 percentaige:")
            factor_proteins_8_percantage=int(input("enter your factor protein 8 percentage (0-50) : "))

        # We defined the patient's severity
        if factor_proteins_8_percantage<1:
            severity_of_hemophilia="severe"
            numbers_of_severe+=1     
        elif 1<=factor_proteins_8_percantage and factor_proteins_8_percantage<=5:
            severity_of_hemophilia="moderate"
            numbers_of_moderate+=1
        elif 5<factor_proteins_8_percantage<50:
            severity_of_hemophilia="mild"
            numbers_of_mild+=1


    elif factor_proteins_number==9:
        Numbers_of_Hemophilia_B+=1
        # Protein level in blood (%)
        factor_proteins_9_percantage=int(input("enter your factor protein 9 percentaige  (0-50) :"))
        while not (0<=factor_proteins_9_percantage<50):
                print("please try enter factor protein 9 percentaige:")
                factor_proteins_9_percantage=int(input("enter your factor protein 9 percentaige  (0-50) :"))

        # We defined the patient's severity
        if 0<=factor_proteins_9_percantage<1:
            severity_of_hemophilia="severe"
            numbers_of_severe+=1       
        elif 1<=factor_proteins_9_percantage<=5:
            severity_of_hemophilia="moderate"
            numbers_of_moderate+=1         
        elif 5<factor_proteins_9_percantage<50:
            severity_of_hemophilia="mild"
            numbers_of_mild+=1

        
    # We obtained the antibody amount
    amount_of_BU=float(input("enter your amount of the BU (0 or 0 greater) :"))
    while amount_of_BU<0:
        print("please , enter again BU's value.")
        amount_of_BU=float(input("enter your amount of the BU (0 or 0 greater) :"))

    # We obtained the number of bleeding incidents in patients with a moderate disease level.
    if severity_of_hemophilia=="moderate":
        bleeding_episodes=int(input("enter your the number of bleeding episodes (0 or greater then 0 ) :"))
        while bleeding_episodes<0:
            print("Bleeding episodes must be greater than 0.")
            bleeding_episodes=int(input("enter your the number of bleeding episodes (0 or greater then 0 ) :"))


    #We checked whether the user has an inhibitor based on their level for prophylactic treatment.
    if amount_of_BU>=5:
        inhibitorpositive_patient=True
        if factor_proteins_number==8:
            inhibitorpositive_Hemophilia_A+=1
        elif factor_proteins_number==9:
            inhibitorpositive_Hemophilia_B+=1           
    else:
        inhibitorpositive_patient=False

    

    #We checked whether prophylactic treatment would be applied to the patient.
    if (amount_of_BU==0 and severity_of_hemophilia=="severe") or (severity_of_hemophilia=="moderate" and bleeding_episodes>=3 and inhibitorpositive_patient==False):
        total_prophylaxis_patients+=1
        if severity_of_hemophilia=="moderate":
            numbers_of_prophylaxis_moderate+=1

        prophylaxis_will_be_applied="Apply"
        
        #If prophylaxis is being applied, we obtained the patient's weight.
        weight_of_patient=float(input("enter your weight (0 or greater than 0) : "))
        while weight_of_patient<0:
            print(" please , enter again your weight")
            weight_of_patient=float(input("enter your weight (0 or greater than 0) : "))
        
        #If prophylaxis is being applied, we also obtained the medication's production type, R or P.
        production_type_of_factor=input("Please enter the production type of the factor medication to be used. (plasma-derived/recombinant)   P/p/R/r: ")
        while production_type_of_factor not in ["P","p" ,"r" ,"R"]:
            print("You must enter one of the following values: P, p, R, r.")
            production_type_of_factor=input("P/p/R/r: ")
    
    else:
        prophylaxis_will_be_applied="Prophylaxis will not be applied."


    if prophylaxis_will_be_applied=="Apply":
        #We defined the expected value of the protein level in the patient's blood.
        factor_target_percentage=40

        #We calculated the required IU amounts to raise the protein level in the blood to the necessary level.
        if factor_proteins_number==8:
            if factor_proteins_8_percantage >=factor_target_percentage:
                print("There is no need to administer medication to the patient.")
            else:
                required_increase_8=factor_target_percentage-factor_proteins_8_percantage
                required_IU= weight_of_patient*required_increase_8/2

        #We calculated the required IU amounts to raise the protein level in the blood to the necessary level.
        if factor_proteins_number==9:
            if factor_proteins_9_percantage>=factor_target_percentage:
                print("There is no need to administer medication to the patient.")
            else:
                required_increase_9= factor_target_percentage-factor_proteins_9_percantage
                required_IU=weight_of_patient*required_increase_9 

    if prophylaxis_will_be_applied=="Apply":
        
        bottle_count_2000=0
        bottle_count_1500=0
        bottle_count_1000=0
        bottle_count_500=0
        bottle_count_250=0
        bottle_capacity_2000,bottle_capacity_1500,bottle_capacity_1000,bottle_capacity_500,bottle_capacity_250=2000,1500,1000,500,250

        while required_IU>0:
            if  1750<required_IU:
                required_IU-=2000
                bottle_count_2000+=1
            elif 1250<required_IU<=1750:
                required_IU-=1500
                bottle_count_1500+=1
            elif 750<required_IU<=1250:
                required_IU-=1000
                bottle_count_1000+=1
            elif 250<required_IU<=750:
                required_IU-=500
                bottle_count_500+=1
            elif required_IU>0:
                required_IU-=250
                bottle_count_250+=1

        #We calculated how many vials would be used in a single dose and the given dose amount for the patient's treatment
        number_of_bottle=bottle_count_2000+bottle_count_1500+bottle_count_1000+bottle_count_500+bottle_count_250
        total_dose_amount=bottle_count_2000*bottle_capacity_2000+bottle_capacity_1500*bottle_count_1500+bottle_count_1000*bottle_capacity_1000+bottle_count_500*bottle_capacity_500+bottle_capacity_250*bottle_count_250
        
        if factor_proteins_number==8:
            if production_type_of_factor in ["P", "p"]:
                #We defined the total IU and vial count for patients using factor 8 and plasma medication.
                hemophilia_A_plasma_2000+=bottle_count_2000
                hemophilia_A_plasma_1500+=bottle_count_1500
                hemophilia_A_plasma_1000+=bottle_count_1000
                hemophilia_A_plasma_500+=bottle_count_500
                hemophilia_A_plasma_250+=bottle_count_250
                hemophilia_A_plasma_totalIU+=total_dose_amount
                   
            elif production_type_of_factor in ["r", "R"]:
                #We defined the total IU and vial count for patients using factor 8 and rekombinant medication.
                hemophilia_A_recombinant_2000+=bottle_count_2000
                hemophilia_A_recombinant_1500+=bottle_count_1500
                hemophilia_A_recombinant_1000+=bottle_count_1000
                hemophilia_A_recombinant_500+=bottle_count_500
                hemophilia_A_recombinant_250+=bottle_count_250
                hemophilia_A_recombinant_totalIU+=total_dose_amount

        
        if factor_proteins_number==9:
            if production_type_of_factor in ["P", "p"]:
                #We defined the total IU and vial count for patients using factor 9 and plasma medication.
                hemophilia_B_plasma_2000+=bottle_count_2000
                hemophilia_B_plasma_1500+=bottle_count_1500
                hemophilia_B_plasma_1000+=bottle_count_1000
                hemophilia_B_plasma_500+=bottle_count_500
                hemophilia_B_plasma_250+=bottle_count_250
                hemophilia_B_plasma_totalIU+=total_dose_amount
                
            elif production_type_of_factor in ["R", "r"]:
                #We defined the total IU and vial count for patients using factor 9 and rekombinant medication.
                hemophilia_B_recombinant_2000+=bottle_count_2000
                hemophilia_B_recombinant_1500+=bottle_count_1500
                hemophilia_B_recombinant_1000+=bottle_count_1000
                hemophilia_B_recombinant_500+=bottle_count_500
                hemophilia_B_recombinant_250+=bottle_count_250
                hemophilia_B_recombinant_totalIU+=total_dose_amount

        
        if factor_proteins_number==8 and factor_proteins_8_percantage<factor_target_percentage:
            required_increase_8=factor_target_percentage-factor_proteins_8_percantage
            required_IU= weight_of_patient*required_increase_8/2
        if factor_proteins_number==9 and factor_proteins_9_percantage<factor_target_percentage:
            required_increase_9= factor_target_percentage-factor_proteins_9_percantage
            required_IU=weight_of_patient*required_increase_9 
    
    print(f"ID :{ID_number}")         # Print the patient's ID number.                 
    print(f"name and surname :{name_surname}")      # Print the patient's name and surname.                             
    print(f"{type_disease} and {severity_of_hemophilia}")  #Print the type of disease and severity of hemophilia.
    print(f"Will prophylaxis be applied? {prophylaxis_will_be_applied}")                     # Print whether prophylaxis will be applied.
 
    if prophylaxis_will_be_applied=="Apply":

        # Check if the factor protein is 8 and production type is plasma-derived
        if factor_proteins_number==8 and (production_type_of_factor in ["P", "p"]):
            print("factor 8 and plasma-derived")
            numbers_of_used_plasmaderived_Hemophilia_A+=1
        
        # Check if the factor protein is 8 and production type is recombinant
        elif factor_proteins_number==8 and (production_type_of_factor in ["R","r"]):
            print("factor 8 and recombinant")
            numbers_of_used_recombinant_Hemophilia_A+=1

        # Check if the factor protein is 9 and production type is plasma-derived
        elif factor_proteins_number==9 and (production_type_of_factor in ["P", "p"]):
            print("factor 9 and plasma-derived")
            numbers_of_used_plasmaderived_Hemophilia_B+=1

        # Check if the factor protein is 9 and production type is recombinant
        elif factor_proteins_number==9 and (production_type_of_factor in ["R","r"]):
            print("factor 9 and recombinant")
            numbers_of_used_recombinant_Hemophilia_B+=1
        
        #We defined and printed how many times the medication should be used per week.
        if factor_proteins_number==8:
            How_many_times_a_week_to_use_the_medication=3
            print(f"How many times a week does he/she use (it)? :{How_many_times_a_week_to_use_the_medication}")
        #We defined and printed how many times the medication should be used per week.
        elif factor_proteins_number==9:
            How_many_times_a_week_to_use_the_medication=2
            print(f"How many times a week does he/she use (it)? :{How_many_times_a_week_to_use_the_medication}")

        #We calculated the total amount of IU the patient will receive in 4 weeks.
        week4_total_medication=How_many_times_a_week_to_use_the_medication*4*total_dose_amount
        total_IU+=week4_total_medication

        #We calculated the total amount of IU the patient will receive in 4 weeks.
        if production_type_of_factor in ["P", "p"]:
                total_cost_for_4week=float(0.3*week4_total_medication)
        if production_type_of_factor in ["R","r"]:
                total_cost_for_4week=float(0.4*week4_total_medication)           

        #We defined the information of the patient with the highest 4-week medication cost.
        if total_cost_for_4week>highest_medication_cost_for_4_week:
            highest_medication_cost_for_4_week=total_cost_for_4week
            highest_medication_cost_patients_informations=f"""Highest medication cost patient's Tr identification number: {ID_number} , name and surname: {name_surname} , type of disease: {type_disease} , disease severitie: {severity_of_hemophilia} , weight: {weight_of_patient} , production types of medications used (plasma-derived/recombinant): {production_type_of_factor} ,  total medication amounts for 4 weeks (IU): {week4_total_medication}IU ,total medication costs for 4 weeks($): {highest_medication_cost_for_4_week}($) """
        
        total_cost_of_patients_4week+=total_cost_for_4week

        #We defined the information of the patient with the maximum 4-week medication amount.
        if factor_proteins_number==8:
            if week4_total_medication> max_medication_amount_for_4_week_factor8:
                max_medication_amount_informations_hemophilia_A=f"""The Hemophilia-A patient with the highest 4-week medication amount's TR identification number: {ID_number}, name and surname: {name_surname}, disease severitie: {severity_of_hemophilia}, weight: {weight_of_patient}, production types of medications used (plasma-derived/recombinant): {production_type_of_factor}, total medication amounts for 4 weeks (IU): {week4_total_medication}IU, total medication costs for 4 weeks($): {total_cost_for_4week}($)"""

        if factor_proteins_number==9:
            if week4_total_medication> max_medication_amount_for_4_week_factor9:
                max_medication_amount_informations_hemophilia_B=f"""The Hemophilia-B patient with the highest 4-week medication amount's TR identification number: {ID_number}, name and surname: {name_surname}, disease severitie: {severity_of_hemophilia}, weight: {weight_of_patient}, production types of medications used (plasma-derived/recombinant): {production_type_of_factor}, total medication amounts for 4 weeks (IU): {week4_total_medication}IU, total medication costs for 4 weeks($): {total_cost_for_4week}($)"""

        print(f"minimum reuqired dose of medication at one time (IU) = {required_IU}")        #Minimum required dose of medication at one time (IU)
        print(f"Number of 2000 IU vials per dose : {bottle_count_2000} , Number of 1500 IU vials : {bottle_count_1500} , Number of 1000 IU vials : {bottle_count_1000} , Number of 500 IU vials : {bottle_count_500} , Number of 250 IU vials : {bottle_count_250}")
        print(f"Total amount of medication used in 4 weeks : {week4_total_medication}")
        print(f"Number of 2000 IU vials used in 4 weeks :{bottle_count_2000*How_many_times_a_week_to_use_the_medication*4} , Number of 1500 IU vials :{bottle_count_1500*How_many_times_a_week_to_use_the_medication*4} , Number of 1000 IU vials :{bottle_count_1000*How_many_times_a_week_to_use_the_medication*4} , Number of 500 IU vials :{bottle_count_500*How_many_times_a_week_to_use_the_medication*4} , Number of 250 IU vials :{bottle_count_250*How_many_times_a_week_to_use_the_medication*4}")
        print(f"Total cost for 4 week is: {total_cost_for_4week:.2f}$")   
    #We are asking if information for another patient will be entered.
    other_patients = input("Are there next patient? (Y/y/N/n): ")
    while other_patients not in ["Y","y","N","n"]:
        other_patients = input("Are there next patient? (Y/y/N/n): ")
    if other_patients in ["Y","y"]:
        other_patients = True
    else:
        other_patients = False


total_patients=Numbers_of_Hemophilia_A+Numbers_of_Hemophilia_B
numbers_of_prophylaxis_Hemophilia_A=numbers_of_used_plasmaderived_Hemophilia_A+numbers_of_used_recombinant_Hemophilia_A
numbers_of_prophylaxis_Hemophilia_B=numbers_of_used_plasmaderived_Hemophilia_B+numbers_of_used_recombinant_Hemophilia_B


print(f"numbers of Hemophilia-A ={Numbers_of_Hemophilia_A}  ,   numbers of Hemophilia-B = {Numbers_of_Hemophilia_B} and numbers of all patients = {total_patients}  ")
print(f"numbers and percentages of patients with severe ={numbers_of_severe} - %{(numbers_of_severe/total_patients)*100} \n numbers and percentages of patients with moderate ={numbers_of_moderate} - %{(numbers_of_moderate/total_patients)*100}\n numbers and percentages of patients with mild = {numbers_of_mild} - %{(numbers_of_mild/total_patients)*100}")
print(f"Percentage of inhibitor presence in Hemophilia-a patients = %{(inhibitorpositive_Hemophilia_A/Numbers_of_Hemophilia_A)*100} and Percentage of inhibitor presence in Hemophilia-B patients = %{(inhibitorpositive_Hemophilia_B/Numbers_of_Hemophilia_B)*100}")
print(f"Percentage and numbers of inhibitor presence in Hemophilia-A patients = {numbers_of_prophylaxis_Hemophilia_A} - %{(numbers_of_prophylaxis_Hemophilia_A/Numbers_of_Hemophilia_A)*100} \n Percentage and numbers of inhibitor presence in Hemophilia-B patients = {numbers_of_prophylaxis_Hemophilia_B} , %{(numbers_of_prophylaxis_Hemophilia_B/Numbers_of_Hemophilia_B)*100 }")
print(f"The percentage of patients receiving prophylaxis among hemophilia patients whose disease severity is moderate = %{(numbers_of_prophylaxis_moderate/numbers_of_moderate)*100} ")
print(f"Percentage of Hemophilia-A patients using plasma-derived factor medications for prophylaxis = %{(numbers_of_used_plasmaderived_Hemophilia_A/numbers_of_prophylaxis_Hemophilia_A)*100} - Percentage of Hemophilia-A patients using recombinant factor medications for prophylaxis = %{(numbers_of_used_recombinant_Hemophilia_A/numbers_of_prophylaxis_Hemophilia_A)*100} /n  Percentage of Hemophilia-B patients using plasma-derived factor medications for prophylaxis = %{(numbers_of_used_plasmaderived_Hemophilia_B/numbers_of_prophylaxis_Hemophilia_B)*100 } - Percentage of Hemophilia-B patients using recombinant factor medications for prophylaxis = %{(numbers_of_used_recombinant_Hemophilia_B/numbers_of_prophylaxis_Hemophilia_B)*100 }"  )
print(f"""
total plasma-derived factor-8:  Total IU:{hemophilia_A_plasma_totalIU*12} , amount of bottle 2000IU  : {hemophilia_A_plasma_2000*12} , amount of bottle 1500IU  : {hemophilia_A_plasma_1500*12} , amount of bottle 1000IU  : {hemophilia_A_plasma_1000*12} ,amount of bottle 500IU  : {hemophilia_A_plasma_500*12} , amount of bottle 250IU  : {hemophilia_A_plasma_250*12}
total recombinant-derived factor-8:   Total IU:{hemophilia_A_recombinant_totalIU*12} , amount of bottle 2000IU  : {hemophilia_A_recombinant_2000*12} , amount of bottle 1500IU  : {hemophilia_A_recombinant_1500*12} , amount of bottle 1000IU  : {hemophilia_A_recombinant_1000*12} ,amount of bottle 500IU  : {hemophilia_A_recombinant_500*12} , amount of bottle 250IU  : {hemophilia_A_recombinant_250*12}
total plasma-derived factor-9:   Total IU:{hemophilia_B_plasma_totalIU*8} , amount of bottle 2000IU  : {hemophilia_B_plasma_2000*8} , amount of bottle 1500IU  : {hemophilia_B_plasma_1500*8} , amount of bottle 1000IU  : {hemophilia_B_plasma_1000*8} ,amount of bottle 500IU  : {hemophilia_B_plasma_500*8} , amount of bottle 250IU  : {hemophilia_B_plasma_250*8}
total recombinant-derived factor-9:   Total IU:{hemophilia_B_recombinant_totalIU*8} , amount of bottle 2000IU  : {hemophilia_B_recombinant_2000*8} , amount of bottle 1500IU  : {hemophilia_B_recombinant_1500*8} , amount of bottle 1000IU  : {hemophilia_B_recombinant_1000*8} ,amount of bottle 500IU  : {hemophilia_B_recombinant_500*8} , amount of bottle 250IU  : {hemophilia_B_recombinant_250*8}
""")
print(f"4-weeks factor medication cost  {total_cost_of_patients_4week} and 1-year factor medication cost {total_cost_of_patients_4week*13} ") 
print(f"Average annual total medication amount {(total_IU*13 /total_prophylaxis_patients):.2f} and avarage annual total medication cost {(total_cost_of_patients_4week*13/total_prophylaxis_patients)}")
print(max_medication_amount_informations_hemophilia_A)
print(max_medication_amount_informations_hemophilia_B)
print(highest_medication_cost_patients_informations)
