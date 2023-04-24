local setup to replicate this video
https://www.youtube.com/watch?v=qCCj7qy72Bg&t=8s

From code folder in terminal:

steps to install/run locally and verify failing tests

1. pip3 install -r requirements.txt
2. python3 -m unittest

steps to build and run docker container and verify successful tests (or see below to name image as part of build and run)

1. docker build .
2. docker run [image sha] unittest

OR

1. docker build . -t debug-docker
2. docker run debug-docker unittest
