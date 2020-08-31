
## Branches

,,,graph
digraph G {
   node[shape=box]
   rankdir=LR;
   nodesep=1.5;
   subgraph cluster_0 {
      label = "Main";

      master_1 -> master_2 -> master_3 -> master_4 -> master_5 -> master_6 -> master_7;
      color="#ddd0d0";
      style=filled;
   }

   subgraph cluster_1 {
      label = "Feature";

      feature_1 -> feature_2 -> feature_3;

      color="#d0ddd0";
      style=filled;
   }

   subgraph cluster_2 {
      label = "Idea";

      idea_1 -> idea_2;

      color="#d0d0dd";
      style=filled;
   }   

   feature_1 -> idea_1;
   idea_2 -> feature_3;
   master_2 -> feature_1;
   feature_3 -> master_6;
}
,,,


## Git's "killer app" 

* Elegant management of concurrent development 
* Trying out features 
* Simple, yet powerful

<term>
   <h>Branch</h>
   In the context of git, a branch is a line of development. Think of it as a
   highway-lane: Everything moves forward, some lanes diverge, but every lane
   is headed in the same direction.
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

To list all branches, run:

```
git branch
```

Note that your new branch does not currently have an asterisk. This means you
are still on master.

---

## Check out your branch

To switch to working on your new branch, run:

```
git checkout [name]
```

Now git branch shows your new branch with the asterisk! Any new commits you make will be made to your new branch.

,,,graph{150,600}
digraph G {
   rankdir=LR;
   node[shape=box];

   past[label="..."];
   future_1[label="..."];
   future_2[label="..."];

   subgraph cluster_0 {
      label = "*your_branch";

      branch[label="new commit"]
      branch->future_2;

      color="#d0ddd0";
      style=filled;
   } 

   subgraph cluster_1 {
      label = "master";
      master[label="current commit"];
      color="#ddd0d0";
      style=filled;
      master->future_1
   }

   past->master;
   master-> branch;
}
,,,


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

Now your feature is added to a branch: 

,,,graph{200,600}
digraph G {
   node[shape=box];
   rankdir=LR;

   past[label="..."]
   future_1[label="..."]
   future_2[label="..."]

   subgraph cluster_1 {
      main->future_1;
      label="master";
      style=filled;
      color="#ddd0d0";
   }

   subgraph cluster_0 {
      feature->future_2;
      label="*my_feature";
      style=filled;
      color="#d0ddd0";
   }

   past->main
   main->feature
}
,,,

---

## Log

The git log command is helpful for figuring out commit histories

```
git log --oneline --all
```
<info>The --all flag lets you see all branches, not just the one you are currently on!</info>
<info>The --graph flag lets you sort-of see the commit history as a graph! There are also tools for making nicer graphs if you need one.</info>
Note that master is now still at the previous commit, while your branch is one commit ahead.

---

## Local merging

To merge your feature branch, run:
```
# Go to the destination branch
git checkout master
# Merge the feature
git merge my_feature
```
Since there are no conflicts, this just brings master "up to speed" with your
work:

,,,graph{150,600}
digraph G {
   node[shape=box];
   rankdir=LR;

   past[label="..."]
   future[label="..."]

   subgraph cluster_1 {
      main->merged->future;
      label="master";
      style=filled;
      color="#ddd0d0";
   }

   subgraph cluster_0 {
      feature;
      style=filled;
      color="#d0ddd0";
   }

   past->main
   main->feature
   feature->merged
}

,,,

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

Conflicts occur when branches contain different versions of the same file that
"overlap".  Let's try to create some conflict, and then resolve it.
<term>
   <h>Conflict</h>
   In git terminology, a conflict is defined as the merging of two different
   versions of the same file. Conflicts can get quite intense, and difficult to
   resolve.
</term>

,,,graph{200,600}
digraph {
   compound=true;
   node [shape=box];
   edge[arrowhead=none]
   
   subgraph cluster_0{
      {
         node[
            shape=record, 
            label="<l>|<r>" 
            margin=0 width=3 
            height=.1 
            style=filled 
            color="#b0b0b0"
            ];

         graph[
            nodesep=.1 
            pad=.2 
            ranksep=2
            ];

         b[color="#fdc0c0"]
         d[color="#b0ddb0"]
         f[color="#b0ddb0"]
         a[color="#b0ddb0"]

         a->b->c->d->e->f[style=invis];
         rankdir=TB;
      }
   }
   b1[label="Branch 1"]
   b2[label="Branch 2"]

   b1 -> a[style=invis; lhead=cluster_0;]
   b2 -> f[style=invis; lhead=cluster_0;]

   b1 -> b:r;
   b1 -> d:r;
   b1 -> f:r;
   b:l -> b2 
   a:l -> b2;
}
,,,

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
