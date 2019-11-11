# Contributing

## Cloning the project
- <a href="https://github.com/TCACastelijns/JADSPDENG-GitToturial/fork">Fork the repository</a>
- Start Git Bash and navigate to a proper location.
- Clone your fork: `git clone https://github.com/<your_GitHub_username>/JADSPDEng-GitTutorial.git`
- Navigate to your cloned repository: `cd JADSPDEng-GitTutorial`

- Right now your local copy is connected with your forked repository (`origin`). Running `git remote -v` will show:

   ```
   origin  https://github.com/<your_GitHub_username>/JADSPDEng-GitTutorial.git (fetch)
   origin  https://github.com/<your_GitHub_username>/JADSPDEng-GitTutorial.git (push)
   ```
   Therefore we want to connect to the original repository as well:
   
   `git remote add base https://github.com/TCACastelijns/JADSPDEng-GitTutorial.git`

## Pulling and pushing changes
- Every time the original repository (`base`) is updated you can pull the most recent changes via `git pull base master`
- You don't have permission to push changes to the original repository. To do this you have to make a pull request as explained below!

## Work on a new feature
- Start a new branch for developing new code/features:  `git checkout –b <feature>`
- Implement your changes and check status and add changes to git:  (1) `git status` and (2) `git add <filename>`
- Commit your changes: `git commit –m "<your commit message>"`
- Repeat steps 2/3 if you have more additions over time
- Push your feature to the forked repository in GitHub: `git push origin <feature>`
- [Create a PR](https://help.github.com/articles/creating-a-pull-request/) on Github. Write a **clear description** for your PR, including all the context and relevant information, such as:
   - The issue that you fixed or functionality you added, e.g. 'Fixes bug with...' or 'Adds plots in EDA'
   - Motivation: why did you create this PR? What functionality did you set out to improve? What was the problem + an overview of how you fixed it? Whom does it affect and how should people use it?
   - Any other useful information: links to other related Github or mailing list issues and discussions, benchmark graphs, academic papers.

## Back in sync
- If accepted, the `master` of your forked repository is out of synch with the orignal. Therefore, you need to checkout to your `master` and pull the original master (including the changes) from GitHub: `git pull https://github.com/TCACastelijns/JADSPDEng-GitTutorial.git`
- Now your local forked repo is in synch, but your online version net yet. So push your local changes to your online forked version: `git push origin master`
