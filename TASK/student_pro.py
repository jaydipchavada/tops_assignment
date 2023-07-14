select = """
            PRESS 1 FOR COUNSELLOR
            PRESS 2 FOR FACULT
            PRESS 3 FOR STUDENT
"""
main_dic = {}

def counsellor():
    menu = """
            1. ADD STUDENT
            2. REMOVE STUDENT
            3. VIEW ALL STUDENT
            4. VIEW SPECIFIC STUDENT

    """
    print(menu)
    #print(select)
    add_id = True
    while add_id:
        student = {}
        s_name = {} 
        roll_no = int(input("Enter Student Roll no : "))
        if roll_no in main_dic:
            print("Roll no is allready Exiting. ")
        else:
            f_name = input("Enter First Name : ")
            l_name = input("Enter Last Name : ")
            contact = int(input("Enter Contact Number : "))
            student['f_name'] = f_name
            student['l_name'] = l_name
            student['contact'] = contact
            main_dic[roll_no] = student
            sub_add = True
            while sub_add:
                subject = input("Enter Subject : ")
                marks = int(input("Enter Marks : "))
                fees = int(input("Enter Fees : "))
                sub = {}

                sub['marks'] = marks
                sub['fees'] = fees
                s_name[subject] = sub
                student['subject'] = s_name
                add = input("Do you want to add more subject (y/n) : ")
                if add == 'y':
                    sub_add = True
                else:
                    sub_add = False
            faculty = input("Enter Faculty Name : ")
            student['faculty'] = faculty
        add_ids = input("Do you want to add more id (y/n) : ")
        if add_ids == 'y':
            add_id = True
        else:
            add_id = False
            

    
    # sub['subject'] = subject

counsellor()
print(main_dic)