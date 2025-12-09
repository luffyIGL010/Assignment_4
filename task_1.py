import os


#with open("sample.txt", "r") as file:
#    content = file.read()
#    print(content)
    


try:
    if os.path.exists("sample.txt"):
        with open("sample.txt", "r") as file:
            content = file.read()
            print(content)
        
        
        
    else:        
        raise FileNotFoundError
        print("The file does not exist. ")












except FileNotFoundError as Error:
  print("Error: Thefile \'sample_1.txt'\n was not found. ")
    
    
    