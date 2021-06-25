def password_cracker():
    binary_dict={"a":"01100001","b":"01100010","c":"01100011","d":"01100100","e":"01100101","f":"01100110","g":"01100111","h":"01101000","i":"01101001","j":"01101010","k":"01101011","l":"01101100","m":"01101101","n":"01101110","o":"01101111","p":"01110000","q":"01110001","r":"01110010","s":"01110011","t":"01110100","u":"01110101","v":"01110110","w":"01110111","x":"01111000","y":"01111001","z":"01111010"}
    digit=5
    real_password=input("Type your 5-letter password: ")
    print("This is the binary for each letter of your password: ")
    for letter in real_password.lower():
        if letter in binary_dict:
            letter=binary_dict.get(letter)
            print(letter)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    frag_pass=["."]*digit   
    while digit>0:
        for char in alphabet:
            frag_pass[0]=char
            for char in alphabet:
                frag_pass[1]=char
                for char in alphabet:
                    frag_pass[2]=char
                    for char in alphabet:
                        frag_pass[3]=char
                        for char in alphabet:
                            frag_pass[4]=char
                            password=frag_pass[0]+frag_pass[1]+frag_pass[2]+frag_pass[3]+frag_pass[4]
                            if password==real_password:
                                print(f"This is your password: {password}")
                                return
        digit-=1        
password_cracker()