# GIT
---

#### BASICS, GITHUB [jump to...](#basics-github)
#### GITIGNORE [jump to...](#gitignore)
#### BRANCHES [jump to...](#branches)
#### WORKFLOW EXAMPLE [jump to...](#workflow-example)


---
## BASICS, GITHUB
[jump to top...](#git)<br><br>
- INIT, STATUS, ADD, COMMIT, LOG

<br>Installation (linux)
```markdown
sudo apt-get install git
```
Config name for the repository (onetime setting)
```markdown
git config --global user.name "Rapid1898"
```
Config mail for the repository (onetime setting - use the mail using for github.com)
```markdown
git config --global user.email "x@gmx.com"
```
Create repository in the actual directory
```markdown
git init
```
Add file to the repository / staging area (prepared for later commit)
```markdown
git add file.xyz
```
Add all html-files to the repo / staging area
```markdown
git add *.html
```
Add everything to the repository / staging area from the directory
```markdown
git add .
```
2nd way to add everything to the repository / staging area from the directory
```markdown
git add *
```
Add readme-file
```markdown
git add README.md
```
remove specific file from the repository / staging area (before commiting!)
```markdown
git rm --cached index.html
```
Actual status in the git-directoy (eg. added files, changed files, not added,...)
```markdown
git status
```
Commit files which are added / changed in the repo (with comment) - taking a "snapshot"
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
Push with upstream definition (shorthand - to the master)
```markdown
git push -u origin master
```
Push with upstream definition (longhand - to the branch "answer")
```markdown
git push --set -upstream origin answer
```
undo add command before (all files get set back to the initial state)
```markdown
git reset
```
undo the last commit
```markdown
git reset HEAD~
```

<br>Pull (update) files from GitHub<br>
(-u saves the paths - so at the next push - it must be only typed push)
```markdown
git pull -u origin master
```

<br>Enable pushing with ssh-key in Idea and VSCode
```markdown
Enable open ssh agent: https://dev.to/aka_anoop/how-to-enable-openssh-agent-to-access-your-github-repositories-on-windows-powershell-1ab8
Run commands: https://stackoverflow.com/questions/56490194/vs-code-bitbucket-ssh-permission-denied-publickey
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
Change name of the branch - eg. for renaming branch "master" to "main"
```markdown
git branch -m main
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



---
## WORKFLOW EXAMPLE
[jump to top...](#git)<br><br>
<br>fork the initial repository on github (select personal account as target)
```markdown
click fork-button in github
```
get the forked repository clone
```markdown
click code-button to grab link
```
clone the repository to the local folder
```markdown
git clone github-link
```
create branch "answer"
```markdown
git branch answer
```
set current branch to "answer"
```markdown
git checkout answer
```
see which branch is curently active (eg. main or answer)
```markdown
git status
```
add all files to the stage (all in the current folder)
```markdown
git add .
```
when something wrong were added (undo the whole add command)
```markdown
(git reset)
```
shows the actual files on the stage
```markdown
git status
```
commit files from stage ("take snapshot")
```markdown
git commit -m "Completed"
```
push with upstream definition (to the branch "answer")
```markdown
git push --set-upstream origin answer
```
change from main to the branch "answer"
```markdown
select branch on git hub with button
```
make an pull request to the original repository
```markdown
click pull request button
```





