# Render-test
A basic website -- just enough to test out hooking things up to render, and not much more.

We will go over steps in lecture. You should fill out the following:

## What steps do I need to do when I download this repo to get it running?
- Ensure python version in Pipfile matches that on your computer
- `pipenv install` to install libraries/dependencies

## What commands starts the server?
- `pipenv run flask --app server.py run` to run the development flask app
- `pipenv run gunicorn server:app` to run in production

## Before render

Before render you will need to set up a more production-grade backend server process. We will do this together in lecture, once that's done you should update the command above for starting the server to be the **production grade** server.