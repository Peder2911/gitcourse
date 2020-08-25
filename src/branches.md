
## Git's "killer app" 

Branches are a big deal!

* Elegant management of concurrent development 
* Trying out features 
* Simple, yet powerful

<term>
   <h>Branch</h>
   In the context of git, a branch is a line of development. Think of it as a
   highway-lane: Everything moves forward, some lanes diverge and might go
   somewhere else, while most lanes eventually merge back into a single lane.
</term>

---

## Listing branches 

You start on a branch, by default named "master". To list all branches in the repository, run:
```
git branch
```
<description>
   By default, this should show master with an asterisk prepended.
   This means that master is the active branch.
</description>
<description>
   This is one of two commands for checking which branch you are currently on,
   the other being the always-useful git status.
</description>

---

## Creating a branch

To create a branch, run: 

```
git branch [name]
```

Running git branch without the name should now show two entries. Note that your
branch does not currently have an asterisk. This means you are still on master.

---

## Check out your branch

To switch to working on your new branch, run:

```
git checkout [name]
```

Now git branch shows your new branch with the asterisk! Any new commits you make will be made to your new branch.

---

## Shorthand

Instead of writing

```
git branch [name]
git checkout [name]
```

You can simply write

```
git checkout -b [name]
```

This creates a new branch, and sets it as the active branch.

---

## Working with branches

There is no given way to work with github branches. Instead, there are many
proposed workflows, that are essentially rulesets that make collaboration
easier:

* Git flow
* Gitlab flow
* Github flow
* Forking WF
* Feature branching

---

## Basic "Feature Branch"

Rules:

* No commits directly to master
* Development happens in feature-branches
* Each branch should introduce one new feature
* Merging should be reviewed (covered later).

---

## Example 

```
git checkout -b my_feature
echo "print('😎')" >> main.py
git commit -m "Added a cool print" 
```

Now your feature is added to a branch! Check out the log:
```
git log --oneline --all
```
<info>The --all flag lets you see all branches, not just the one you are currently on!</info>
Note that master is now still at the previous commit, while your branch is one commit ahead.

---

## Local merging

Merging coolprint back into master can be done locally (note that when working on github, merges are instead done in pull requests!)

To merge your feature branch, run:
```
# Go to the destination branch
git checkout master
# Merge the feature
git merge my_feature
```
Since there are no conflicts, this just brings master "up to speed" with your work. Check the log!

---

## Cleaning up

Since the branches "my_feature" and "master" now point to the same commit, it means that they are equivalent. You can now safely delete the feature branch. To do this, run:
```
git branch -d my_feature
```
<info>
   git branch -d won't let you delete anything that isn't fully merged, and
   thus won't ever delete any of your code. If you want to get dangerous, and
   force-delete a branch, use a capital -D.
</info>

Now master contains the commit introduced in the feature branch!

---

## Merge conflicts

Let's try to create some conflict, and then resolve it.
<term>
   <h>Conflict</h>
   In git terminology, a conflict is defined as the merging of two different
   versions of the same file. Conflicts can get quite intense, and difficult to
   resolve.
</term>

## Branching off

First, make a change in a branch, ex:

```
git checkout -b feature_branch
echo "print('on branch')" >> main.py
```

Then, go back to master, and _change the same file_

```
git checkout master
echo "print('on master')" >> main.py
```

---

## Mapping the conflict 

Now the file main.py exists in two concurrent versions! Check out:

```
git log --all --oneline --graph
```

<info>
   The "graph" flag lets you see branches sort-of graphically, in the terminal!
</info>

You can also diff the two branches, to figure out what their differences are:

```
git diff master feature_branch
```
---

## Why create conflict?

Editing the same file concurrently might be really useful to flesh out ideas.
Branching, conflict and resolution makes coding less constraining and frees
people up to be creative!

---

## Resolving conflict

With this simple example, resolving the conflict shouldn't be too bad. However, a simple merge won't do it:

```
git checkout master
git merge feature_branch
```

This alters the affected file to contain code from both branches. Now, when you
run git status, it tells you that there are unmerged paths that you need to
sort out!

---

## Picking sides

Do you want one version, or the other? Or maybe both? Edit the file (main.py)
so that it only contains the code that you want, and then add it with:

```
git add main.py
```

Then create a commit that represents the merge:

```
git commit -m "Merged the feature" 
```

---

## Mission complete!

The conflict is resolved, you can now delete the branch and keep working on master!

```
git branch -d feature_branch
```

---

## What about pull requests?

Pull requests are related to remoting, which is covered in the next component.
Stay tuned!
