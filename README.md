# two-dart-checkouts
A Kata created by me!

## Problem
Alex wants to get better at darts. He's great at hitting trebles but not so great at hitting doubles or doing quick maths. From a starting point of 501 he can reliably get down to a score of under 99. He can hit a treble with one dart but he needs two attempts at the double. Since Alex is bad at maths he needs help to work out which treble and then double he needs to hit with his remaining three darts.

## Input
The input will include one integer between 98 and 60.

## Output
The output should include all possible two dart finishes for that number. Trebles should be prefixed with T and doubles with D.

## Sample Input
``` shell
86
```

## Sample Output
``` shell
T20 D10
T18 D16
T16 D19
```

## Test Cases
Test cases are held inside the directory data/secret

## Submissions
The submissions are held inside the submissions directory.

## Evaluation
To get started, install the Docker CLI, and then pull the image:

``` shell
docker pull problemtools/full
```
Problem tools is the engine that evaluates kata's, you can find the repo here https://github.com/Kattis/problemtools. Once the image has finished downloading, you can check that it exists on your system using `docker images`. To launch an interactive container run:
``` shell
docker run --rm -it problemtools/full
```
To run this problem package, you'll need to clone this repo and launch an interactive container with a bind mount to your local clone.
``` shell
docker run --rm -it -v "$(pwd)"/two-dart-checkouts:/two-dart-checkouts problemtools/full
```
To evaluate the submissions contained within this problem package, on the container run: 
``` shell
verifyproblem /two-dart-checkout
```
