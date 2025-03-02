# Deepening Git Understanding

## Research & Testing

### `git checkout main -- <file>`

**What it does:**  
Restores a specific file from the `main` branch without affecting other changes in the working directory.

**When to use it:**

- When you accidentally modify a file and want to restore it to its last committed state in `main` without discarding other changes.
- When you need to revert a single file but don’t want to reset the entire working directory.

**Surprise factor:**  
It’s a powerful yet simple way to undo unintended changes without affecting the rest of the working tree.

### `git cherry-pick <commit>`

**What it does:**  
Applies a specific commit from another branch to the current branch without merging the whole branch.

**When to use it:**

- When you need a specific bug fix or feature from another branch without bringing in unrelated changes.
- When you made an important commit on the wrong branch and need to apply it elsewhere.

**Surprise factor:**  
It’s useful for selective changes but can lead to conflicts if the commit modifies files that have since changed.

### `git log`

**What it does:**  
Displays the commit history, showing who made each change, when, and with what commit message.

**When to use it:**

- To review past changes and understand the evolution of the codebase.
- To find specific commits related to a bug fix or feature.
- To get commit hashes needed for operations like `cherry-pick` or `revert`.

**Surprise factor:**  
The different formatting options (`git log --oneline`, `git log --graph --all --decorate`) make it much easier to navigate complex histories.

### `git blame <file>`

**What it does:**  
Shows who last modified each line of a file and when.

**When to use it:**

- To track down when a bug was introduced and who made the change.
- To understand the reasoning behind a specific piece of code by seeing past contributors.
- To assign responsibility when debugging issues in a team.

**Surprise factor:**  
It’s a great debugging tool, but it can also highlight messy commit histories when a file has been changed many times.

## Reflection

Testing these commands gave me a deeper understanding of how Git handles changes and history. `git cherry-pick` stood out as a powerful tool for managing commits selectively, while `git blame` provided surprising insights into the development history of files. These commands are invaluable in large projects with multiple contributors, helping with debugging, version control, and maintaining a clean workflow.
