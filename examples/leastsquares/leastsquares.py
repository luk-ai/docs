import tensorflow as tf
from lukai import saver

x = tf.placeholder(tf.float32, [None, 1], name="x")
y_ = tf.placeholder(tf.float32, [None, 1], name="y_")

b = tf.Variable(tf.zeros([1]), name="b")
w = tf.Variable(tf.zeros([1, 1]), name="w")

y = tf.identity(w * x + b, name="y")

loss = tf.reduce_sum((y - y_) * (y - y_))
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(loss, name="train")

sess = tf.Session()
sess.run(tf.initialize_all_variables())

"""
for step in range(10):
    sess.run(train_step, feed_dict={x:[[2.3],[1.7],[-3.8],[0.5],[-4.1],[-1.5],[-2.5],[6.2]],
                                    y_:[[-4.4],[-3.6],[7.7],[-0.9],[8.3],[2.9],[4.9],[-12.2]]})
    print step, sess.run(w), sess.run(b)
"""


print('Node names: x = {}, y_ = {}, train_step = {}, w = {}, b = {}, y = {}'.format(
  x.name, y_.name, train_step.name, w.name, b.name, y.name,
))

saver.save(sess)
