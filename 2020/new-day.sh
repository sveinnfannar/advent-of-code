#!/bin/bash

if [[ -z $1 ]]; then
  echo "usage: new-day.sh <day>"
  exit 1
fi

if [[ -z $AOC_SESSION ]]; then
  echo "AOC_SESSION environment var is unset"
  exit 1
fi

set -xe

mkdir $1
cp template.py $1/$1_1.py
touch $1/$1_2.py

curl --cookie "session=$AOC_SESSION" https://adventofcode.com/2020/day/$1/input > $1/input.txt 2> /dev/null
head $1/input.txt
