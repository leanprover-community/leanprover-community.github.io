# How to install Lean 4 and mathlib a Docker container

This document explains how to get started with Lean and mathlib if you
are using a container running Docker (or Podman).

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for assistance.

A Dockerfile (or, in Podman, the Containerfile) contains
```
FROM ubuntu:23.04

WORKDIR /opt/

RUN apt -y update && apt upgrade
RUN apt install -y curl

# The following doesn't work 
#RUN curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
# because
# elan: Unable to run interactively. Run with -y to accept defaults, --help for additional options                                                    
# therefore, as per https://stackoverflow.com/a/53605439/1164295 
RUN curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf |\
       bash -s -- --default-toolchain leanprover/lean4:stable -y
# -s = --silent;     Do not show progress meter or error messages. Makes Curl mute.
# -S = --show-error; When used with -s, --silent, it makes curl show an error message if it fails.
# -f = --fail;       (HTTP) Fail fast with no output at all on server errors. This is useful to enable scripts and users to better deal with failed attempts.

# if "nightly" is desired, replace
# --default-toolchain leanprover/lean4:stable
# with
# --default-toolchain leanprover/lean4:nightly
# as per https://leanprover-community.github.io/archive/stream/270676-lean4/topic/elan.20update.html

ENV PATH "/root/.elan/bin:$PATH"
```

You can compile that Dockerfile using a Makefile:
```
Makefile 
IMAGE_NAME=lean4onubuntu

docker: docker_build docker_run

docker_build:
	docker build -t $(IMAGE_NAME) .

docker_run:
	docker run -it --rm \
             -v `pwd`:/scratch \
             --user $(id -u):$(id -g) \
             $(IMAGE_NAME) /bin/bash
```
Once the container is built, you run it using
```bash
$ docker run -it --rm lean4onubuntu lean --version
Lean (version 4.0.0, commit 7dbfaf9b7519, Release)
```
To run a script, use
```bash
$ docker run -it --rm -v `pwd`:/scratch --workdir /scratch lean4onubuntu lean --run hello.v4.lean
Hello, world!
```
where
```bash
$ cat hello.lean
def main : IO Unit := IO.println "Hello, world!"
```


## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
