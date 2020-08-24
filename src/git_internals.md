
## Under the hood

* Git isn't magic!
* Easier to understand why something goes wrong

## What is git?

"Global Information Tracker"

A filesystem that is indexed by information content rather than metadata (inodes).

## Internals

Git is a filesystem that uses hash-values instead of paths.

* Nothing gets stored twice

## Four types of data

* Blobs (are stored in)
* Trees (are stored in)
* Commits (are pointed at by)
* References

That's all there is to it!

(In addition to lots of procedures that operate on these data types)

## Blobs

* A blob is a piece of data.
* Reached using their hash value.
* Hashes are fingerprints

```
echo "same info" > a
echo "same info" > b
git hash-object a
>> 4775e6d574597fce6e46a19f27e275108ee2c76e 
git hash-object b
>> 4775e6d574597fce6e46a19f27e275108ee2c76e 
```

Separate files, same hash (fingerprint).

## Storage and retrieval



## Trees

* A tree is a filesystem
* Holds blobs and trees
* Trees have hash values too!

## Commits

* A commit is a reference to a tree.

## Plumbing and porcelain

* "Old git" forced deeper understanding
* "New git" wraps internals in nice(r) functions

