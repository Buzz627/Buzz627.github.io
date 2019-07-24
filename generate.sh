#!/bin/bash
mkdir -p testResumes
hackmyresume build resume/resume.json to testResumes/myResume.all
hackmyresume build resume/resume.json to testResumes/myResume.pdf -t node_modules/jsonresume-theme-stackoverflow2/
hackmyresume build resume/resume.json to testResumes/myResume.html -t node_modules/jsonresume-theme-eloquent/
hackmyresume build resume/resume.json to testResumes/onePageResume.pdf -t node_modules/jsonresume-theme-onepage-wide/
rm testResumes/*.css
rm testResumes/myResume.json
sed -i "s/icon-lg icon-stackoverflow/fab fa-stack-overflow/" testResumes/myResume.html
sed -i '/<\/head>/i/<link rel="stylesheet" href="https:\/\/use.fontawesome.com\/releases\/v5.8.1\/css\/all.css">/' testResumes/myResume.html

