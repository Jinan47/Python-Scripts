import time 

# s_c = secret_code
s_c = '1234'

while True: 

    # c_q = code_question
    c_q = input('Enter the secret code: ')
    
    if c_q == '1234':

        print('You are the real user..')
        time.sleep(1)

        print('Opening your passwords file')
        time.sleep(1)

        print('~~~~~~~~~~~~~~~~~')
        time.sleep(1)


        lines = []
        with open('passwords.txt') as f:
            print('The passwords inside your file are:')
            time.sleep(1)
            lines = f.readlines()
            
            for line in lines:
                print(line)    
            

        time.sleep(1)
        edit = input('Do you want to edit the file? Type yes or no: ').lower()
       

        if edit == 'yes':
            edit2 = input('Do you want to edit lines, delete lines, or add lines? Enter 1, 2, or 3: ')

            if edit2 == '1':
                edit_option = input('Do you want to edit the whole line, or just some characters? Enter 1 or 2: ')

                if edit_option == '1':
                  # line_indicator
                    line_ind = input('Which line do you want to edit? Enter 1, 2, etc: ')
                    
                    int_ind = int(line_ind)
            
                    if line_ind == '1':
                        line[int_ind] = "Here is my modified Line\n"
  
                        with open('passwords.txt', 'w') as file:
                            file.writelines(line  )
                            print(f'Successfully line {line_ind} has been modified!')
                            break
                    
                    if line_ind == '2':
                        pass
                    
                    if line_ind == '3':
                        pass

                    if line_ind == '4':
                        pass


                elif edit_option == '2':
                    pass
                
                else:
                    print('Invalid choice!')
                    exit

            elif edit2 == '2':
                pass
            
            elif edit2 =='3':
                pass

            else:
                print('Invalid choice!')
                exit

        elif edit == 'no':
            exit

        else:
            print('Invalid word')
            break
            
    else:
        print('This is an invalid password,You are not the real user.')
        quit