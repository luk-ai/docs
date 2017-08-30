# Architecture

There's three main components to Lukai you'd be interacting with.
* Web Interface
* Client Library
* Python Model Creation Library

## Web Interface

The web interface provides all the feedback and information you need about the
trained model.

## Client Library

[![GoDoc](https://godoc.org/github.com/luk-ai/lukai?status.svg)](https://godoc.org/github.com/luk-ai/lukai)

The client takes care of all training and model deployment. It's designed to be
used as a black box that you can log your training data into and get
predictions out. It also provides hooks so you can tell it when it's allowed to
train, to avoid impacting users.

The client library is written in Go, but it's easy to use it in Java (Android)
and Objective-C/Swift (iOS).

## Python Model Creation Library

This library is used by the data scientists creating the models. It's a small
library that packages up your model and launches a job to train it. It only
takes a handful of lines of code to integrate and use.
