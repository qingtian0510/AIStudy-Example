import tensorflow as tf

#placeholder

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)
output1 = input1+input2
with tf.Session() as sess:
    print(sess.run(output1,feed_dict={input1:[7.],input2:[2.]}))
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))