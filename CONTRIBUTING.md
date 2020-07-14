# Contributing Guidelines and Git Flow
This document plans to outline the following for *all* contributers of the Flameboi Slack API. Please follow these guidelines to the best of your knowledge and understanding, and feel free to ask @stucamp or @KevinThePepper if you have any questions or need help!

### Table of Contents
1. [Chain of Command](#chain-of-command)
1. [Git Flow Overview](#git-flow-overview)
1. [Workflow Contribution Requirements](#contribution-requirements)
1. [Workflow Examples](#workflow-examples)
1. [Quality of Code Requirements](#quality-of-code)
1. [Git Cheatsheet](#git-cheatsheet)
1. [Good Resources](#good-resources)

---

# Chain of Command
The Flameboi Slack API project managers are Stu Campbell (@stucamp) and Kevin Shelley (@KevinThePepper). They control the day-to-day opperation of this project, with oversight and policy ditacted by the CodeDevil Officers.

> To see your CodeDevil officers, visit the #about channel of the CodeDevils Slack.



# Git Flow
Overall, the git flow is relaxed and laidback. You, as a contributer, have lots of wiggle room to make your own inputs in your commits to this repo. Forking is not neccesary - use the origin repo's branches for your own code bases. You have full control over your own development branches and git flow. That said, there are some general guidelines you need to follow.

## Overview
#### Dev Branch
The dev branch contains the *latest source code* for the Flameboi Slack API. It is a protected branch, and is the default branch you will submit pull requests to when submitting your contributions.

#### Master Branch
The master branch is the *production code* that Flameboi is currently opperating on. Whatever is in master is what will be on Slack. Pull requests from dev to master will **only be intiated and managed by the project manager(s)**.

## Contribution Requirements
Observe the following in your git flow:
- Make an Issue prior to working on your code. We don't want you to work on something that is actually banned or already implemented!
- Your personal development branches must start with your name and be consistent. E.g., `bobby-dev`, `bobby-new-feature-here`
- Though there is no limit to the number of reviewers you request, your pull requests to dev **must** at least include **all the project managers**.
- Comment in your code following the functionality and process within it.

### Workflow Examples
#### Marlee's Quick Patch (Simple)
> My name is Marlee, and I noticed a mispelling in the README.
> 
> I would create a branch called `marlee-hotfix`, make the correction, then submit a pull request to `dev` making sure to request review from @stucamp and @KevinThePepper.

Good job Marlee!

#### Clyde & Darryl's Calendar (Collab)
> My name is Clyde, and I'm working with Darryl on a sweet new command that allows something to do with calendars.
> 
> I would checkout a new branch entitled `calendar-dev`, acting as the default branch for the calendar between me and Darryl, making sure to keep it updated with `dev`. Me and Darryl would then have our own branches whatever we want to call them following the guideline, say  `darryl-calendar` and `clyde-dev`. We push and pull from `calendar-dev` for development.
> 
> When our cool new command is done, *making sure to pull `calendar-dev` from `dev` so that there are not merge conflicts*, I would then make a pull request on `dev`. Billy-Bob is good with calendars, so I would like his review too. I would request review from @BillyBobUSA along with the project managers @stucamp and @KevinThePepper.

Nicely done boys!

---

# Quality of Code
> TODO - TBD by Stu and/or Kev

----

# Git Cheatsheet
#### Checkout Existing Branch
```
git checkout existing-branch
```

#### Checkout a New Branch
```
git checkout -B your-new-branch
```

#### Push to Repo
```
git push origin destination-branch
```
Pro tip: add `-u` to skip the naming of the branch in future pushes.

#### Update Current Branch from Repo
```
git fetch && git pull
```

#### Update Current Branch from Target Branch
```
git fetch ; git merge target-branch
```
Use Case: Your development branch (current branch) is behind `dev` and you want to update your branch with the code from `dev` (or some other target branch). 

---

# Good Resources
**Installing Git** - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

**Git Basics** - https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
