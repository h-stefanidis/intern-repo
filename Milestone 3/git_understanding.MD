# Git: Staging vs. Committing

## What is the difference between staging and committing?

- **Staging** (`git add`): Prepares specific changes to be included in the next commit.
- **Committing** (`git commit`): Saves the staged changes to the repository’s history with a message describing the update.

## Why does Git separate these two steps?

Git separates staging and committing to give developers more control. This allows selective commits, grouping related changes together, and reviewing updates before finalising them.

## When would you want to stage changes without committing?

- When you’re working on multiple changes but only want to commit part of them.
- When you need to organise and review changes before making a final commit.
- When you're preparing multiple commits with different purposes from the same work session.
