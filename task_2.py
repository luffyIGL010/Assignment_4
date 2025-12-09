text_to_write=input("Enter text to write to the file: ")



with open("output.txt",'wt') as fh:
    fh.write(text_to_write +"\n")
    
    
print("Data successfully written to output.txt. ")



additional_text_to_write=input("Enter additional text to append: ")
    

with open("output.txt",'at') as fh:
    fh.write(additional_text_to_write +"\n")
    
print("Data successfully appended. ")




with open('output.txt','rt') as fh:
    data=fh.read()
    print(data)