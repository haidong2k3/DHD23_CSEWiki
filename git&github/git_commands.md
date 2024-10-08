## On MacOS

### Check Homebrew version
brew --version
brew update

### Interact with git through homebrew
brew list => find 'git'
brew install git
brew upgrade git
brew uninstall git

### git info
git --version
git config --global --list
git config --local --list

### basic configuration
git config --global user.name "username"
git config --global user.email "username@example.com"

### Change default branch name
git config --global init.defaultBranch main
default branch name of git is 'master'
However, for modern naming convention purpose, we usually change in to 'main'

### ignoring file
create a file name '.gitignore'
put all the file name that need ignore into this file
EX: filename: .gitignore
__pycache__/ (for python program)
.DS_Store (for MacOS env)

### initialize
git init
git status (so sanh file hien tai - trong staging area - local repo)

git add <file> ((them file vao staging area))
git rm --cached <file> (remove new file out of index (commit list))
git reset (remove all file that have been add)
git restore <file> (abandoned changes since the last commit)
git restore --staged <file>

### Commit the changes
git commit -m "Commit title"
git commit -am "Commit title"
(commit dua cac thay doi trong local repo vao staging area)

### Commit history
git log
git log --pretty=oneline

### Checking out previous commits
git checkout <first_6_chars_of_commit_ID> (leave the current branch and acces Detached HEAD State)
ex: % git log --pretty=oneline
ff5be08c2adbfb1262d5e2202b63c70cfe8b6eb6 (HEAD -> main) Getting Started 2.
=> ff5be0
90cb04f3ff9bb3cb7cd60772c0fc735d7f8c7d7c Getting Stated.
=> 90cb04

### Working state and branching
'HEAD' is the pointer to the state of current commit.
- **Normal State**: normally 'HEAD' point to the latest commit (HEAD -> main). In this case, you are staying in a branch and new made commits will automatically added to the current branch.
- **Detached HEAD State**: 'HEAD detached at <commit_ID>'. You are not in the branch, all changes will be abandoned when you return to a branch unless you create a new branch to retain it.

git switch - (return to previous branch)
git config --local advice.detachedHead false (not check)

### Branch list
git branch (list all local branch)
git branch -r (list all remote branch)

### Create Branch
git branch <new_branch_name> (tao branch moi)
git switch -c <new_branch_name> (create new branch and switch to it)
git checkout -b <new_branch_name> (create new branch and switch to it)
git switch <branch_name> (switch to existed branch)
git checkout <branch_name> (switch to existed branch)

### Delete local branch (khac voi delete remote branch)
git branch -d <branch_name> (delete branch if it has been merged - safe to delete)
git branch -D <branch_name> (force deletion for branch hasn't been merged - use caution)

### Completely return to the previous state 
(Return to the earlier commit as the normal state)
git reset --hard <first_6_chars_of_commit_ID>

### Delete repository of the project
rm -rf .git/ (recheck by git status)

### Remote repository
git remote
git remote -v
git remote show <remote_repo_name>
<remote_repo_name>: usually 'origin' - default name Git uses for remote repository

### Connect to remote repo
git remote add <remote_repo_name> <link_to_remote_repo>
ex: 
<link_to_remote_repo> = https://github.com/lesterduong/PlayWithGit.git

### Sync local repo to remote repo => Push
git push -u <remote_repo_name> <branch_name>
'-u': or '--set-upstream' link <local_branch> to <remote_branch>
git push

### Sync remote repo to local repo => Pull
git pull

### Resolve Conflict

### Join to an exited remote repo => Clone
git clone <link_to_remote_repo>

### Merge code, Pull request
git merge

### Delete remote branch
git push <remote_repo_name> --delete <branch_name>

### Advanced
git rebase
git cherry-pick

### Size of the push issues
Issues:
"error: RPC failed; HTTP 400 curl 22 The requested URL returned error: 400 
send-pack: unexpected disconnect while reading sideband packet"

Analyze:
The problem might because the size of data in one push is too big.

Solution:
increase buff size: git config http.postBuffer 524288000

Ref:
https://stackoverflow.com/questions/62753648/rpc-failed-http-400-curl-22-the-requested-url-returned-error-400-bad-request