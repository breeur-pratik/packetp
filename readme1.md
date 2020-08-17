# How to use github

Before creating github repository, install github from https://git-scm.com/downloads as well as install github extension in vscode for easy navigation to pull, push, fetch options. You also need to sign in with github in vscode.

Commit : It makes changes in local repository.
PUSH : It pushes changes from local repository to remote repository and make changes in remote repository.
PULL : It will pull changes from remote repository to local repository and makes changes.
Fetch : It will pull changes from remote repository to local repository and not will make changes.
Merge : It will merge old and new files. Here, you can review changes and after reviewing, make changes as you want. Then   clicK MERGE.
Combining FETCH and MERGE is better option than pulling. Also, it give advantage of reviewing.


## How to create repository 

### First Way
You can create repository by clicking "NEW" on top left hand side on github website. You have to give repository name, description as well as you can initialize this repository with a README file. Description and readme file are optional.

### Second Way 
you can initialize repository by clicking on it on left side under "SOURCE CONTROL => INITIALIZE YOUR REPOSITORY" in vscode.


## Remote Creation 

### First Way 
On topleft under "SOURCE CONTROL" , you will find 3 dots. Click on it, goto "REMOTE => ADD REMOTE" then choose repository. IF you want to pull repository from anyone. Then enter his "github_id/repository_name" for eg. "breeur-pratik/packetp". Set repository alias name. After setting name, this name will be shown instead of Repository name.

### Second Way
Use command,
```git remote add <remote_name>  < repository url >.git```
e.g. git remote add origin https://github.com/breeur-pratik/packetp.git


## Commit Changes
  During commiting changes, message should be written compulsorily or else it will give error.

### First way 
To commit changes, goto "SOURCE CONTROL" icon which is present on right hand side below explorer icon. Click on it, and after that press :heavy_check_mark: and it will commit changes. 

### Second way
``` git commit -m "MESSAGE" ```


## Pushing changes to remote repository

### First way
On topleft under "SOURCE CONTROL" , you will find 3 dots. Click on it, goto "PULL, PUSH" option then click on "PUSH TO...". After that, on top center, it will show bar in which your remote repository will be shown. If you set your repository name as ORIGIN, then origin will be seen in bar, click on it. AFter pushing, changes will get reflected in your remote repository. Now, you can refresh your github page and can see changes.

### Second way
``` git push -u <remote_name> <branch_name> ```
eg. git push -u origin master


## Pulling changes from remote repository

Pulling helps to load data from remote repository to your local machine. Remote repository can be of yourself or your colleague. If your local repository and remote repository have different file or same file with changes, it can leads to conflicts. To resolve this conflicts, you have to click "RESOLVE CONFLICTS". Choose part from conflicted section which you wannt and remove other part of conflicted section and then click on "MARK ON RESOLVED" then  "COMMIT MERGE" then "MERGE PULL REQUEST" then "CONFIRM MERGE".

### First Way
To pull, click on "SOURCE CONTROL" then click on 3 dots after that, click on "PULL, PUSH" option then click on "PULL FROM...". After that, on top center, they will show bar in which your remote repository will be present. If you set your repository name as ORIGIN, then origin will be seen in bar, click on it. AFter pulling, changes will get reflected in your local repository.

### Second Way
``` git pull <remote_name> <branch_name> ```

## Cloning && Forking

Cloning : Copying repository from remote to your local machine.
Forking : Copying repository from another person github account to yours github account.

### Cloning
``` git clone < repository url >.git ```

### Forking
There is a fork icon present in github page at right side. Click on it, repository will get forked.


## Pull Request: 
After forking anyone's repository or cloning it, if you had made any changes in it and want to collaborate to the  master repository, you can send "PULL REQUEST" along with message. This message convey your ideas what you improved. To pull request, go on Github website and click on it. 


## Creating a branch:
You can make changes in your main file by committing it or you can create a new branch. You can merge branch with main file, when you want branch features in main file. To merge, goto "PULL REQUEST" then click on "COMPARE AND PULL REQUEST" then click on "CREATE PULL REQUEST". After clcking, if you find some conflicts, then click "Resolve Conflicts".Choose part from conflicted section which you want and remove other part of conflicted section and then click on "MARK ON RESOLVED" then  "COMMIT MERGE" then "MERGE PULL REQUEST" then "CONFIRM MERGE".


## Collaborator 

To add a colaborator, do following steps:
Step 1 : Goto Setting
Step 2 : Goto Manage Access
Step 3 : Click on Invite Collaborator
Step 4 : After inviting, you can give him 3 access: a. Admin b.Read c. Write
    a. Admin => Team Member can read, clone, push and add collaborator to this repository.
    b. Write => Team Member can read, clone, push to this repository.
    c. Read => Team Member can read and clone this repository.

