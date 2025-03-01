Research what causes merge conflicts in Git.
Merge conflicts are caused in Git when two different branches have made changes to the same line of code in a file, causing Git to be unable to automatically merge them together and thus requiring manual fixing to choose what changes are to be kept when merging branches.

What caused the conflict?
I chose to add new text to this specific question and the following questions after changing branches from feature/git_understanding to main. Afterwards, I committed the file itself to GitHub and had to go through the merge conflict resolution process. Here is the new text.

How did you resolve it?
By looking at the current changes in my branch versus the incoming changes from another branch, I could determine which branch needed to be kept. Typically, the incoming branch changes involve new code that is brought into a file, and thus should be made compatible with the original branch's changes, otherwise committing this would result in many errors in the main codeframe.

What did you learn?
To find alternatives to minimise the need for merge conflicts. This can be done by frequently pulling from the main code to ensure the code I'm working with is up to date. Additionally, isolating my work from the main branch by creating a new one allows me to specifically sort out defined changes and then resolve any conflicts with ease in the main branch.
