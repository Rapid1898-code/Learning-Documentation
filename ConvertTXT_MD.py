fn = "GIT"
# fn = "JAVASCRIPT"

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
for line in lines:
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
        # desc = "<br>" + line.split("*>",1)[1].strip()
        desc = line.split("*>",1)[1].strip()
        myNewList.append (desc)
        myNewList.append ("```markdown")
        myNewList.append (code)
        myNewList.append ("```")
    elif "=> " in line:
        code = line.split("=>",1)[0].strip()
        # desc = "<br>" + line.split("=>",1)[1].strip()
        desc = line.split("=>",1)[1].strip()
        if desc != "" and code != "":
            myNewList.append(desc)
            myNewList.append("```markdown")
            myNewList.append(code)
            myNewList.append("```")
        elif desc != "" and code == "":
            # myNewList.append ("<br>" + line.split("=>",1)[1].strip())
            myNewList.append (line.split("=>",1)[1].strip())
    elif '""' in line and codeBlock == False:
        codeBlock = True
    elif '""' in line and codeBlock == True:
        myNewList.append ("```markdown")
        for elem in codeBlockCont:
            myNewList.append(elem)
        myNewList.append("```")
        codeBlock = False
        codeBlockCont = []
    else:
        myNewList.append(line.strip())

# for i in myNewList:
#     print(i)

# write final md file
with open(fn.lower() + '.md', 'w') as f:
    for item in myNewList:
        f.write("%s\n" % item)
