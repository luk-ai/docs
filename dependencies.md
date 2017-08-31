# Installing Dependencies

## Python Management Library

You will need to install [Tensorflow](https://www.tensorflow.org/install/). This
can be done via `pip` in most cases:
```
$ pip install tensorflow
```
You can also install `tensorflow-gpu`, but GPU support doesn't matter since
we're only creating a model and not training it.

You can install the `lukai` library via `pip` as well.

```
$ pip install lukai
```

## Go Client Library

You'll need to make sure you have a recent version of [Go installed](https://golang.org/doc/install).

The Go client requires [Tensorflow for Go](https://www.tensorflow.org/install/install_go).

Once you have Tensorflow installed you can actually install the library via
`go get`.

```
$ go get -u github.com/luk-ai/lukai
```
