#!/bin/bash

#git clone forked repository specifying milano branch
#git clone -b milano https://github.com/luigi-calori/lectures.git lectures_milano

#set up username and mail
#git config --global user.name "luigi-calori"
#git config --global user.email "l.calori@cineca.it"

#find where is the remote to push
#git remote show origin

#suppose we edited README, than status show but we have to add it
#git add README.md
#git commit -m " changed README "

#define upstream repo into local
#git remote add upstream https://github.com/cineca-scai/lectures.git

#here are the step to keep it in sync with upstream
git pull
git fetch upstream milano
git checkout milano
git merge upstream/milano -m "sync from upstream fork"
git push origin milano
