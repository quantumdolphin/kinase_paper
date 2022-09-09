with open('crds.txt','r') as f:
    list_of_lines = f.readlines()
    for i in list_of_lines:
        res = re.findall(r'\(.*?\)',i)
        print(res)