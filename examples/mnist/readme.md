# MNIST Example

This is the code from the [Tensorflow MNIST tutorial](https://www.tensorflow.org/get_started/mnist/pros) adapted for use with Luk.ai.

## Dependencies

See [Installing Dependencies](../../dependencies.md).

## Create the model

Models for use in Luk.ai are created using standard Tensorflow python scripts
and then launched via the client library. The main additions to the standard
`mnist_deep.py` example is as follows.

```py
# Import the library.
import lukai

...

# Sets the Luk.ai API token.
lukai.set_api_token(FLAGS.api_token)

# Uploads the model to Luk.ai and creates a training job.
lukai.upload(
    session=sess,
    domain=FLAGS.domain,
    model_type=FLAGS.model_type,
    name=FLAGS.name,
    description=FLAGS.description,
    hyper_params=lukai.HyperParams(
        num_clients = 10,
        batch_size = 10,
        num_rounds = 100,
        learning_rate = learning_rate,
        num_local_rounds = 10,
    ),
    metrics={
      accuracy: lukai.REDUCE_MEAN,
    },
    event_targets={
      lukai.EVENT_TRAIN: (keep_prob.assign(0.5),),
      lukai.EVENT_INFER: (keep_prob.assign(1.0),),
      lukai.EVENT_EVAL: (keep_prob.assign(1.0),),
    },
)
```

```
python mnist_deep.py --api_token "<your api token>" --domain "<your domain>"
```

## Launch the Client

This example uses the Go library directly. Running this command will fetch the
MNIST training data and connect to Luk.ai to wait for work. Since there's an
already existing job, training should start immediately.

```
go run -v clients.go -domain=luk.ai -num_clients=2
```
