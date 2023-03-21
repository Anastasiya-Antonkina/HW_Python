def read_phonebook():
    file = open('file_name.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    res_list = []
    for line in lines:
        res_list.append(line)
    file.close()
    return res_list
def add_contact(cont):
    data = open('file_name.txt', 'a', encoding='utf-8')
    data.write(cont['last_name']+' '+cont['name']+' '+cont['phone']+'\n')
def find(): 
    f = input("")
    lines = read_phonebook()
    cnt = 0
    for line in lines:
        if f in line:
            print(line)
        else:
            print("Контакт не найден")    
def find_first(text): 
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if text in line:
                return [line]
        return [] 
def find_and_change(old_text, new_text):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if old_text in line:
                with open("file_name.txt", "r", encoding='utf-8') as file:
                    lines = file.readlines()
                del lines[count]
                
                with open("file_name.txt", "w", encoding='utf-8') as file:
                    file.writelines(lines)
                data = open('file_name.txt', 'a', encoding='utf-8')
                data.write(new_text['family']+' '+new_text['name']+' '+new_text['phone']+'\n')
            else:
                count += 1
    
def find_and_del_first(text): 
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if text in line:
                with open("file_name.txt", "r", encoding='utf-8') as file:
                    lines = file.readlines()
                del lines[count]
                with open("file_name.txt", "w", encoding='utf-8') as file:
                    file.writelines(lines)
                return True
            else: 
               count += 1
        
        return False
                                                       