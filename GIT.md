# GIT
---

#### BASICS, GITHUB [jump to...](#basics-github)
#### GITIGNORE [jump to...](#gitignore)
#### BRANCHES [jump to...](#branches)


---
## BASICS, GITHUB
[jump to top...](#git)<br><br>
- INIT, STATUS, ADD, COMMIT, LOG

<br>Installation (linux)
```markdown
sudo apt-get install git
```
Create repository in the actual directory
```markdown
git init
```
Config name for the repository
```markdown
git config --global user.name "Rapid1898"
```
Config mail for the repository
```markdown
git config --global user.email "x@gmx.com"
```
Add file to the repository (prepared for later commit)
```markdown
git add file.xyz
```
Remove file from the repository (not planned for later commit)
```markdown
git rm --cached file.xyz
```
Add alle html-files to the repo
```markdown
git add *.html
```
Add everything to the repository from the directory
```markdown
git add .
```
2nd way to add everything to the repository from the directory
```markdown
git add *
```
Actual status in the git-directoy (eg. added files, changed files, not added,...)
```markdown
git status
```
Commit files which are added / changed in the repo (with comment)
```markdown
git commit -m "comment"
```
Show overview about the last activities
```markdown
git log
```
Clone a repository in the actual path
```markdown
git clone github-link
```
Link the acutal folder/repo to the github-repo
```markdown
git remote add origin https://github.com/link/Test.git
```
Push (update) files on GitHub
```markdown
git push -u origin master
```

<br>Pull (update) files from GitHub<br>
(-u saves the paths - so at the next push - it must be only typed push)
```markdown
git pull -u origin master
```




---
## GITIGNORE
[jump to top...](#git)<br><br>
- create a file ".gitignore" in the root-folder of the respository<br>
- this files / folders will be ignored when comitting (and so for pushing to the remote repository)<br>
- github has for eg. some problems with files > 100MB<br>

<br>all files in this folder will be ignored
```markdown
add folder: /prg/dist/*
```
this specific file will be ignored
```markdown
add file: /prg.xlsx
```



---
## BRANCHES
[jump to top...](#git)<br><br>
- BRANCH, CHECKOUT, DIFF, MERGE)

<br>Create a new branch with the name "newFeature"
```markdown
git branch newFeature
```
Change to branch "newFeature" (from the master-branch)
```markdown
git checkout newFeature
```
Return to the master-branch
```markdown
git checkout master
```
Delete branch
```markdown
git branch -d newFeature
```
Create a new branch named "new"
```markdown
git checkout -b new
```
Show the difference in the files
```markdown
git diff head
```
Show only the differences for the files which are not commited yet
```markdown
git diff --staged
```
Merge the branch with the master
```markdown
git merge newFeature
```
