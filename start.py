import os

#new dir for each website you crawl
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
    else:
        print("project already exists")

# create_project_dir("poojadir");

# Creating the queue and the crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url) #start of the list of links to crawl with the homepage
    if not os.path.isfile(crawled):
        write_file(crawled, '')     #havent crawled anything yet so starts out empty

#creating a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#adding data onto existing file
def append_to_file(path, data):
    with open(path, 'a') as file: # a is append mode, file is the reference to what youre opening
        file.write(data + '\n');

#delete file contents
def delete_file_contents(path):
    with open(path,'w'):        #create file with same name and do nothing to it - pass is like loop with nothing
        pass   #does nothing

#read a file and convert each line to set - make sure its not repeated in queue and crawled so convert to set and then back to file
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f: #refer to file we re reading as f; rt - read text file
        for line in f:
            results.add(line.replace('\n',''))      #getting rid of all newlines
    return results

#go through set, each item in set is new line in fil
def set_to_file(links, file):
    delete_file_contents(file)  #all data in links set
    for link in sorted(links):
        append_to_file(file, link)
