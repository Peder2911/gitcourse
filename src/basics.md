
## Follow along!

Get out your terminals!

---

## Creating a new repository 

Navigate to a folder of choice, then:

```
git init
```

<description>This creates a git repository</description>

<info>
   What this command does is create a folder called ".git" in your directory,
   with lots of stuff in it. This folder contains everything git uses to
   function (you don't need to worry about it).
</info>

## Your favorite command:

```
git status
```
<description>
   This very useful command prints out information about the current state of your repository.
</description>

Run git status after running other commands to see what git has picked up, and what it thinks you should do!

## Creating a file 

```
echo "print('hello world')" > main.py
```
<description>
   This creates a basic python script
</description>

git status now tells you that you have an untracked file.

## Adding a file

```
git add main.py
```
<description>
   This adds your file to the Index
</description>
<term>
   <h>Index</h>
   The Index is a staging area for changes you are about to make.
</term>
<term>
   <h>Staging</h>
   Staging means adding changes to the Index, staging (preparing) them to be committed.
</term>

Status now tells you that you have changes to be committed.

## Committing your change 

<term>
   <h>Commit</h>
   A commit is a snapshot of the entire repository.
</term>

Committing your work means saving your progress. It is useful to think of a commit as a "unit of work".

To create a new commit with the changes saved in the Index, run:

```
git commit -m "My first commit" -m "Wrote a script"
```
<description>
   -m flags add messages to the commit. This will be useful later on!
</description>

## See what you did 

```
git log
```
<description>This command shows you commits for the repository</description>

```
git show HEAD 
```
<description>This shows all changes associated with the current commit</description>
<info>
If you replace HEAD with the hash-value of a commit, it shows changes for that
commit. A hash-value is like a name!
</info>

## Modifying files 

Add some functionality to your script:

```
echo "import math" >> main.py
echo "print('Pi squared is:')" >> main.py
echo "print(math.pow(math.pi,2))" >> main.py
```

Git status now tells you that there is an unstaged modification to main.py. To see what exactly has been added, run:

```
git diff main.py
```
<description>This gives a line-by line overview of changes since the last commit</description>
<info>To see changes to all files, run git diff without specifying a file!</info>

## Commit modification

Add and commit modifications to a file by running:

```
git add main.py
git commit -m "Cool changes" -m "Added some math"
```

## Adding more files

```
echo "This is my fantastic codebase" > README
echo "" > requirements.txt
```

To add both, you could run either of these blocks:
```
# Both in one commit
git add README requirements.txt
git commit -m "Docs" -m "Requirements and README"
```
```
# In separate commits
git add README
git commit -m "Readme" -m "Added a readme"
git add requirements.txt
git commit -m "Requirements" -m "Added an empty req. file"
```

## Removing a file

The empty requirements.txt file isn't really useful yet, so let's remove it:

```
git rm requirements.txt
git commit -m "Removed useless file"
```

This creates a new commit in which your file is deleted.

## Oh no! 😱

Imagine the file you just deleted (and committed to deleting) contained
something really useful!  How do we get it back? This leads us to something a
bit more exiting than adding and removing files...

## Time travel 

Remember, commits are snapshots of a repository, and git stores them all! 
It is actually very hard to permanently delete files from a git repository.
Retrieving files from the past is a little tricky, but the process is a great
way to become a little more familiar with git's fundamentals: Commits and
commit histories.

## Looking back

Before time-travelling, get your bearings with:
```
git log --oneline
```
<info>I used the oneline-flag. This just makes the output a little smaller and easier to read, omit it if you want!</info>

To inspect commits:

```
git show [hash]
```

Notice how our commit-messages makes finding the right commit so much easier!

## Checking out 

To "jump" to a previous commit, meaning your folder will be exactly as it was when you made that commit, run:
```
git checkout [hash]
```
<description>Checkout is a versatile command that lets you jump between commits.</description>
<info>Git uses hashes, but you can add your own labels to commits with tagging, to make navigation easier.</info>

## Looking forwards 

After you have checked out to a previous commit, you might want to get back (to the future).
First, to see where you are on the chain of commits, run:
```
git log --oneline --all
```
<description>Adding the --all flag allows you to see future, as well as past commits.</description>

The current state is called HEAD (look for HEAD in the output of git log). HEAD is not on the latest commit, a state which is called "detached HEAD".

## Checking back

To go back to the latest commit (on the master branch), simply run
```
git checkout master
```
Now everything should be as you left it, before embarking on your journey.

## Finding the file

Let's find our file. This clever git log command shows you all commits
that relate to a file, in this case, our requirements.txt:

```
git log -- "requirements.txt"
```

This should show a commit related to deleting the file ("removed useless file"). Either find the commit before this one using git log, or append a caret to its hash value to find the right query to retrieve the file.

<info>Git has lots of clever ways to query using hash-values or tags. An appended caret means "the commit before this one", tilde plus a number means N commits before this one, et cetera.</info>


## Getting the file


Once you have figured out which query to use, you can get the file back by running this checkout:

```
git checkout [hash] requirements.txt
```

This retrieves the file and places it in your working directory. Git pretends
that this is just a new file that you just wrote, and will let you add it as a
new file:

```
git add requirements.txt
git commit -m "Mission complete"
```
Nice! 🥳

## Summary

This segment has brought you from initializing a new repository to travelling
through its commit history. Don't worry if this seemed a little dense, there
will be plenty of time to become familiar with these commands. Try creating
some test repositories and play around with the commands shown here.

The main takeaway should be that git repositories store everything, and that it is possible to get things back, so don't worry about making changes! Unless you start using some of the nastier commands, things can always be reverted.
