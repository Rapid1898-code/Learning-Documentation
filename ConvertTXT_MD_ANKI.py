# lines with 11 # or TOC in text are ignored
# overview / TOC is build with beginning #>
# headers are build with 6 # (must be identical to overview entries)
# singles lines are build with (left is code-content - right is description) - splitted with => or *>
# codeblock is build with "=> " as header and then the code between "" and ""
# textblock used with "=>" at every beginning line (makes bullet points)

import csv

files = ["GIT","JAVASCRIPT","HTML","CSS","PYTHON","SQL"]

for fn in files:
    # read initial txt file
    with open(fn+".txt","r") as f:
        lines = [x.rstrip() for x in f.readlines()]

    # convert file
    myNewList = ["# " + fn]
    myNewList.append ("---")
    # jumpToTop = "[jump to top...](#" + fn.lower() +")<br><br>"
    jumpToTop = "[jump to top...](#" + fn.lower() +")<br><br>"
    codeBlock = False
    codeBlockCont = []
    csvOutputAnki = []
    csvDesc = ""
    csvElem = ""
    for idx,line in enumerate(lines):
        if any(x in line for x in ["###########","### TOC","\n","///////////", "/// TOC"]):
            pass
        elif codeBlock == True and '""' not in line:
            codeBlockCont.append(line.rstrip())
        elif "#>" in line:
            val = line.split("#> ",1)[1].strip()
            anchorLink = val.replace (", ", "-").replace (",", "-").replace (" ", "-").lower().strip()
            anchorLink = " [jump to...](#" + anchorLink + ")"
            myNewList.append("#### " + val + anchorLink)
        elif "######" in line:
            val = line.split("###### ",1)[1].strip()
            myNewList.append("---")
            myNewList.append("## " + val)
            myNewList.append(jumpToTop)
        elif "*> " in line:
            code = line.split("*>",1)[0].strip()
            desc = line.split("*>",1)[1].strip()
            myNewList.append (desc)
            myNewList.append ("```markdown")
            myNewList.append (code)
            myNewList.append ("```")
        elif "=> " in line:
            code = line.split("=>",1)[0].strip()
            desc = line.split("=>",1)[1].strip()
            if desc != "" and code != "":
                csvOutputAnki.append([desc,code,fn.lower()])
                if idx > 0 and "=> " in lines[idx-1]:
                    myNewList.append(desc)
                    myNewList.append("```markdown")
                    myNewList.append(code)
                    myNewList.append("```")
                else:
                    myNewList.append("<br>" + desc)
                    myNewList.append("```markdown")
                    myNewList.append(code)
                    myNewList.append("```")
            elif desc != "" and code == "":
                if (idx < len(lines) -1) and ("=>" in lines[idx+1]) and (lines[idx+1].split("=>",1)[0].strip() != ""):
                    myNewList.append (line.split ("=>", 1)[1].strip () + "<br>")
                elif "######" in lines[idx-1]:
                    myNewList.append (line.split ("=>", 1)[1].strip ())
                else:
                    myNewList.append ("<br>" + line.split("=>",1)[1].strip())
        elif '""' in line and codeBlock == False:
            codeBlock = True
            for i in range(1,10,1):
                if "=> " in lines[idx-i]:
                    csvDesc = lines[idx-i].replace("=> ","").replace("<br>","").strip()
                    break
        elif '""' in line and codeBlock == True:
            myNewList.append ("```markdown")
            for elem in codeBlockCont:
                myNewList.append(elem)
                csvElem = csvElem + elem + "\n"
            myNewList.append("```")
            codeBlock = False
            codeBlockCont = []
            csvOutputAnki.append ([csvDesc, csvElem.strip(), fn.lower()])
            csvElem = ""
        else:
            myNewList.append(line.strip())

    # write final md file
    with open(fn.lower() + '.md', 'w') as f:
        for item in myNewList:
            f.write("%s\n" % item)
    print(f"File {fn.upper() + '.txt'} converted to {fn.lower() + '.md'}...")

    # writing csv file for anki
    while True:
        try:
            with open(fn.lower() + ".csv","w",newline="") as fp:               # Open csv-file in writemode
                a = csv.writer (fp, delimiter=";")                    # Define csv-writer with ","-delimiter
                a.writerows (csvOutputAnki)                                     # Writing individual rows
            print(f"Anki-Cards inputfile wrote to {fn.lower() + '.csv'}...")
            break
        except Exception as e:
            print ("Error: ", e)
            input (f"File Open not possible - pls close and press <Enter> for {fn.lower() + '.csv'}..")
