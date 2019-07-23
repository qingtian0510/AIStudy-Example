import tensorflow as tf

with tf.variable_scope("foo"):
    v2 = tf.get_variable("v",[1])
    print(v2.name)

with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v3 = tf.get_variable("v",[1])
        print(v3.name)

with tf.variable_scope("foo",reuse=True):
    v4 = tf.get_variable("foo/v",[1])
    print(v4==v2)

