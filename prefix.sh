#!/bin/bash
sudo pip3 install -r requirements.txt
sudo service mysql start
git config --global user.email '<email>'
git config --global user.name '<name>'
git remote add upstream https://github.com/LouPlus/jobplus6-11
