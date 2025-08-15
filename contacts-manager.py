import os
from unicodedata import digit


# path for all the code
dir_path = 'C:\\Users\\' + os.getlogin() + '\\Contacts'

question = input('Do you want to add, view, or delete contact? Enter add, view or delete:  ').lower()

if not question == 'add' and not question == 'view' and not question == 'delete':
    print(question, 'is an invalid choice!')

def add_contact(): 
    if question == 'add':
        contact_name = input('Enter the name of the contact you want to add: ')

        join_input = dir_path + "\\" + contact_name + ".txt"
        #join_input = os.joinpath(dir_path, contact_name)

        os.makedirs(dir_path, exist_ok=True)

        if os.path.exists(join_input):
            print('this contact is founded')

        else:
                
                while True:   
                    contact_number = input("Enter the contact's number: ")
                    
                    if not contact_number.isdigit():
                        print('Type a number next time.')
                        continue
                    
                    else:

                        f = open(join_input, "a")
                        f.write('Phone number: ' + contact_number)
                        f.write('\n')
                        f.close()


                        email_print = input('Would you like to add an email address? Type yes or no: ').lower()
                        if email_print == 'yes':
                            contact_email = input("Enter the contact's email: ")

                            f = open(join_input, "a")
                            f.write('Email Adress: ')
                            f.write(contact_email)
                            f.close()
                            
                            print('Contact', contact_name, 'is succesfuly created!')
                            break
                        
                        elif email_print == 'no':
                            print('Contact', contact_name, 'is succesfuly created!')
                            break
                    
                        else:
                            continue
                        

def view_contact():
    if question == 'view':
        # list the files and folders found 
        dir_list = os.listdir(dir_path)
        
        print('Files and directories in "Contacts" ', dir_path, ":")
        
        for i in dir_list:   
            print(i)
        
        
def delete_contact():
    if question == 'delete':
        contact_delete = input('Enter the name of contact you want to delete: ')
        
        join_delete = dir_path + "\\" + contact_delete + ".txt"
        
        if os.path.exists(join_delete):
            os.remove(join_delete)
            
            print("File", contact_delete, "is succesfully removed!")
            
        
        else:
            print("This contact don't exists!")
        
        
def edit_contact():
    while True:
        if question == 'edit':
            contact_edit = input('Enter the name of the contact you want to add: ')
            
            join_edit = dir_path + "\\" + contact_edit + ".txt"
            
            if os.path.exists(join_edit):
                contact_input_delete = input('Do you want to edit phone number, or email adress? Type number, or email: ').lower()
                
                if contact_input_delete == 'number':
                    
                    with open(join_edit, 'w') as file:
                        data = file.readlines()
                        file.writelines(data)
                
            else:
                print("This contact doesn't exists.")
                continue
    
add_contact()
view_contact()
delete_contact()
edit_contact()
