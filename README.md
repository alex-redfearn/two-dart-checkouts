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
## Using kattis/problemtools to Evaluate
To get started, install the Docker CLI, and then pull the image:

``` shell
docker pull problemtools/full
```
Once the image has finished downloading, you can check that it exists on your system using docker images. To launch an interactive container and play around with verifyproblem, problem2pdf, and problem2html run:

``` shell
docker run --rm -it problemtools/full
```

The kattis problem tools program is the engine that evaluates kata's. A kata submission can be evaluated by executing verifyproblem -s ${submission-dir}, where ${submission-dir} is a valid kattis problem package. To run this problem package, first, you'll need to clone this repo to a local dir on your machine. Next run the problemtools/full image and use a bind mount to mount a local dir into the docker container. You'll need to bind your local copy of this repo into the problemtools/full container:
``` shell
docker run --rm -it -v "$(pwd)"/two-dart-checkouts:/submission problemtools/full
```
## Submission
The submissions are held inside the submissions dir

## Test Cases
Test cases are held inside the dir data/secret
