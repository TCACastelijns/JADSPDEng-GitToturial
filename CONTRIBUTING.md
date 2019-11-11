# Contributing

## Cloning the project
- <a href="https://github.com/TCACastelijns/JADSPDENG-GitToturial/fork">Fork the repository</a>
- Start Git Bash and navigate to a proper location.
- Clone your fork: `git clone https://github.com/<your_GitHub_username>/JADSPDEng-GitToturial.git`
- Navigate to your cloned repository: `cd JADSPDEng-GitToturial`

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
- If accepted, the `master` of your forked repository is out of synch with the orignal. Therefore, you need to checkout to your `master` and pull the original master (including the changes) from GitHub: `git pull https://github.com/TCACastelijns/JADSPDEng-GitToturial.git`
- Now your local forked repo is in synch, but your online version net yet. So push your local changes to your online forked version: `git push origin master`

### More about online repositories
Others are obviously submitting pull requests on the original repository, not in our fork. Our local copy is by default only connected with our own fork because this is where we cloned from. Online repositories are called remotes and the default remote is called origin. Therefore if we now check the connected remotes by running `git remote -v`, we will only see our own fork named origin. In order to connect our local copy with the original remote as well, we can issue `git remote add base https://github.com/TCACastelijns/JADSPDEng-GitToturial.git` where `base` is the name we select for this new remote. From now on everytime we want to push or pull changes we can do so by specifying the remote and branch. For example in order to get changes performed by others we can do: `git pull base master`. In order to push our branch called my-feature to our fork we can run `git push origin my-feature`. Please note that you don't have permission to push to base (try and see what happens), instead you need to push into origin and submit a PR as explained above.


