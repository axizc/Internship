# Uncomment the below for "actual" scraping
# from selenium import webdriver
# options = webdriver.ChromeOptions()

# options.add_argument(r"--user-data-dir=C:\Users\vt\AppData\Local\Google\Chrome\User Data")
# options.add_argument(r'--profile-directory=Profile 4') #e.g. Profile 3
# ser = webdriver.ChromeService(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# driver = webdriver.Chrome(service=ser, options=options)
# with open("C:\\Users\\vt\\Downloads\\save.txt", "w", encoding='utf-8') as f:
#     f.write(driver.page_source)

#Opens the source as txt file replace with the actual state
with open('.\state.txt',encoding='utf-8') as f:
    # read file
    lines = f.readlines()
    print(lines)
    i=0
    # to identify the state
    state=""
    # to identify the line # where the schools appear
    listOfSchoolNumbers=[]
    for line in lines:
        #check if the line contains the state
        if '<span class="tenth">' in line:
              state = lines[i+1].strip("\t").strip("\n").strip('\u039c')[0:2]
        #check if the line contains school 
        if '<span class="twofifths">' in line:
            listOfSchoolNumbers.append(i)
        #check if line contains mail
        if "mailto:" in line:
            #remove \t and \n from the line
            nospaces = line.strip("\t").strip('\u039c').strip('\u03ad')
            #cut the mailto:
            removeMailTo = nospaces[16:-2]
            print(removeMailTo)
            print()
            #write it to the text file which is later formatted as csv
            with open(".\\data.txt", "a") as fee:
                fee.write(removeMailTo+","+lines[i+1].strip("\t")[1:-5].strip("\n").strip('\u039c').strip('\u03ad')+","+lines[max(z for z in listOfSchoolNumbers if z <= i)+1].strip("\t").strip("\n").strip('\u039c').strip('\u03ad')+","+state.strip("\u03ad")+"\n")
            
        i+=1
#remove last line bc that is tabroom email
print(listOfSchoolNumbers)
with open(".\\data.txt", 'r') as file:
            lines = file.readlines()
lines_without_last = lines[:-1]
with open(".\\data.txt", 'w') as file:
            file.writelines(lines_without_last)