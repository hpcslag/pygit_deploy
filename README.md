# pygit_deploy
Watching your github repo, auto download and deploy to your server deploy path by Python

##Introduction
When sometime, you need deploy your project to online server you can't go, or need long time to setup, this project will help you auto do 'git pull',it will watching your repo last commit is updated.

##Plugin need install
```pip install PyGithub```
```python -m pip install PyGithub```

##Using
python main.py [username] [password] [repo_name] [your-server-git-path-folder]

###Example
```python main.py ABCD AcDDsdfsd pygit_deploy /user/ACC/Desktop/pygit_deploy```
