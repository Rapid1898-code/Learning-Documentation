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
  myNewList = []

  codeBlock = False
  codeBlockCont = []
  descCont = []
  csvOutputAnki = []
  csvDesc = ""
  csvElem = ""
  for idx,line in enumerate(lines):
    if any(x in line for x in ["###########","### TOC","\n","///////////", "/// TOC"]):
        pass
    elif codeBlock == True and '""' not in line:
        codeBlockCont.append(line.rstrip())
    elif "#>" in line:
      continue
    elif "######" in line:
        val = line.split("###### ",1)[1].strip()
        myNewList.append('<!-- wp:heading {"canvasClassName":"cnvs-block-core-heading-1686125278519"} -->')
        myNewList.append(f'<h2 class="wp-block-heading">{val}</h2>')
        myNewList.append('<!-- /wp:heading -->')
    elif "=> " in line:
        code = line.split("=>",1)[0].strip()
        desc = line.split("=>",1)[1].strip()
        if desc != "" and code != "":
            myNewList.append('<!-- wp:paragraph {"canvasClassName":"cnvs-block-core-paragraph-1686132588595"} -->')
            myNewList.append(f'<p>{desc}</p>')
            myNewList.append('<!-- /wp:paragraph -->')
            myNewList.append('<!-- wp:code {"canvasClassName":"cnvs-block-core-code-1686132588597"} -->')
            myNewList.append(f'<pre class="wp-block-code"><code>{code}</code></pre>')
            myNewList.append('<!-- /wp:code -->')
        elif desc != "" and code == "":
          desc = line.replace("=>", "").strip()
          descCont.append(desc)
          # myNewList.append('<!-- wp:paragraph {"canvasClassName":"cnvs-block-core-paragraph-1686132588595"} -->')
          # myNewList.append(f'<p>{desc}</p>')
          # myNewList.append('<!-- /wp:paragraph -->')
    elif '""' in line and codeBlock == False:
      codeBlock = True
      for i in range(1,10,1):
        if "=> " in lines[idx-i]:
          csvDesc = lines[idx-i].replace("=> ","").replace("<br>","").strip()
          break
    elif '""' in line and codeBlock == True:
      codeBlockCont = [f"<a href='{x}' target='_blank'>{x}</a>" if x.startswith("https://") else x for x in codeBlockCont]
      codeBlockCont = "<br>".join(codeBlockCont)
      descCont = [f"<a href='{x}' target='_blank'>{x}</a>" if x.startswith("https://") else x for x in descCont]
      descCont = "<br>".join(descCont)
      myNewList.append('<!-- wp:paragraph {"canvasClassName":"cnvs-block-core-paragraph-1686132588595"} -->')
      myNewList.append(f'<p>{descCont}</p>')
      myNewList.append('<!-- /wp:paragraph -->')
      myNewList.append('<!-- wp:code {"canvasClassName":"cnvs-block-core-code-1686132588597"} -->')
      myNewList.append(f'<pre class="wp-block-code"><code>{codeBlockCont}</code></pre>')
      myNewList.append('<!-- /wp:code -->')
      codeBlock = False
      codeBlockCont = []
      descCont = []
    # else:
    #     myNewList.append(line.strip())

  # write final md file
  with open(fn.lower() + '.html', 'w') as f:
      for item in myNewList:
          f.write("%s\n" % item)
  print(f"File {fn.upper() + '.txt'} converted to {fn.lower() + '.html'}...")