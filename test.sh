#!/bin/bash

cat links.txt|awk -F# '{system("python get_url_pass.py "$3)}'>pass.txt


