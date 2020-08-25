
## Remote? 

Git supports syncronizing repositories with a remote location. This is great
for collaboration!

Making a repository remote simply means uploading it. Git lets you work on this uploaded version in clever ways.

---

## Remote mindfully 

Using git together increases the importance of

* Using git safely
* Documentation and communication 

---

## Providers

* Bitbucket
* Gitlab
* MS Azure Dev Ops
* Overleaf
* You?

---

## Github

We are focusing on github

* Most widely used
* Simple, open, good
* But check out the others!

---

## Going remote 

Steps:

* Create a remote repository
* Add the remote url to your local repo
* Push to the remote

<term>
   <h>Push</h>
   With git, pushing means uploading your progress, bringing the remote up to speed with your progress.
</term>

---

## Create a remote

After logging into Github, click "new"

![](static/new.png)

Add a name, and click "create repository"

![](static/create.png)

Your repository now lives at "https://github.com/yourUserName/yourRepoName"

---

## Point local to remote

To add the remote to your local repo (from last time), write:
```
git remote add [remotename] [url]
```
For example:
```
git remote add origin \ https://github.com/yourUserName/yourRepoName
```

---

## Syncronization

One of the challenges with working with remotes is keeping your local copy in
sync with the remote, handling divergences. This is, of course, exacerbated by
working with multiple people.

