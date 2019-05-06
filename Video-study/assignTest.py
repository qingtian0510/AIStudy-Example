import tensorflow as tf


def test_1():
    a = tf.Variable([10, 20])
    b = tf.assign(a, [20, 30])
    c = a + [10, 20]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print("test_1 run a : ", sess.run(a))
        print("test_1 run c : ", sess.run(c))
        print("test_1 run b : ", sess.run(b))
        print("test_1 run a again : ", sess.run(a))
        print("test_1 run c again : ", sess.run(c))


def test_2():
    a = tf.Variable([10, 20])
    b = tf.assign(a, [20, 30])
    c = b + [10, 20]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(a))
        print(sess.run(c))
        print(sess.run(a))


def main():
    print("test")
    test_1()
    test_2()


if __name__ == '__main__()':
    main()
