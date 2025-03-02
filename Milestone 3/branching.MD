# Branching & Collaboration

## Why is pushing directly to `main` problematic?

Pushing directly to `main` can introduce untested or incomplete code, potentially breaking the production or shared codebase. It bypasses code reviews and collaboration, increasing the risk of errors.

## How do branches help with reviewing code?

Branches allow developers to work on features or fixes independently. They enable **pull requests (PRs)** and **code reviews**, ensuring that changes are reviewed, tested, and approved before merging into `main`. This maintains code quality and stability.

## What happens if two people edit the same file on different branches?

If two people modify the same file on different branches, Git may detect **merge conflicts** when merging. The conflicting sections must be manually reviewed and resolved to ensure both changes are integrated correctly.
