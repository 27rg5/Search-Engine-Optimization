import os

def create_directory(Project_Name):
    if not os.path.exists(Project_Name):
        os.makedirs(Project_Name)

def crete_files(Project_Name,base_url):
    queue=Project_Name + '/queue.text'
    crawled=Project_Name + '/crawled.text'
    if not os.path.isfile(queue):
        make_file(queue,base_url)
    if not os.path.isfile(crawled):
        make_file(crawled,'')
        

def make_file(fileName,data):
    with open(fileName, 'w') as f:
        f.write(data)

def edit_file(fileName,data):
    with open(fileName, 'a') as app:
        app.write(data+'\n')

def delete_file(fileName):
    open(fileName, 'w').close()

def file_to_set(fileName):
    result= set()
    with open(fileName,'r') as file:
        for line in file:
            result.add(line.replace("\n",''))
    return result

def set_to_file(set_name,fileName):
    with open(fileName,'w') as file:
        for lines in set_name:
            file.write(lines+'\n')
