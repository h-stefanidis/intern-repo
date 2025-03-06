# Debugging with `git bisect`

## What does `git bisect` do?

`git bisect` helps track down the commit that introduced a bug by using **binary search**. It checks out commits between a known "good" and "bad" commit, allowing you to test step by step until the problematic commit is found.

## When would you use `git bisect` in a real-world debugging situation?

- When a bug appears, but you don’t know which commit caused it.
- In large projects with multiple contributors where manually checking commits is impractical.
- When debugging regressions in production code.

## How does it compare to manually reviewing commits?

**git bisect** Fast, automates commit checking, and narrows down the issue efficiently. Requires some manual testing and setup.
**Manual review** Provides full context on changes and commit messages. Time-consuming, especially in large projects.
