import numpy as np
import tensorflow as tf

TIMESTEPS = 10                              # 循环神经网络的训练序列长度。
BATCH_SIZE = 32                             # batch大小。
TRAINING_EXAMPLES = 10000                   # 训练数据个数。
TESTING_EXAMPLES = 1000                     # 测试数据个数。
SAMPLE_GAP = 0.01

INPUT_NODE = 10
OUTPUT_NODE = 1

LAYER1_NODE = 256
LAYER2_NODE = 128

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.01
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 10000
MOVING_AVERAGE_DECAY = 0.99

def inference(intput_tensor, train, regularizer):


    with tf.variable_scope('layer1_fc1'):
        fc1_weights = tf.get_variable("weight", [INPUT_NODE, LAYER1_NODE], initializer= tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [LAYER1_NODE], initializer=tf.constant_initializer(0.0))
        fc1 = tf.nn.relu(tf.matmul(intput_tensor, fc1_weights)+fc1_biases)
        if train: fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope('layer2_fc2'):
        fc2_weights = tf.get_variable("weight", [LAYER1_NODE, LAYER2_NODE], initializer= tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [LAYER2_NODE], initializer= tf.constant_initializer(0.0))
        fc2 = tf.nn.relu(tf.matmul(fc1,fc2_weights)+fc2_biases)
        if train: fc2 = tf.nn.dropout(fc2, 0.5)

    with tf.variable_scope('layer3_fc3'):
        fc3_weights = tf.get_variable("weight", [LAYER2_NODE, OUTPUT_NODE], initializer= tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable("bias", [OUTPUT_NODE], initializer= tf.constant_initializer(0.0))
        logit = tf.matmul(fc2,fc3_weights)+fc3_biases

    return logit

def train(input_x,input_y):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name="x-input")
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name="y-input")

    y = inference(x, False, None)
    global_step = tf.Variable(0, trainable=False)

    # 定义损失函数、学习率、滑动平均操作以及训练过程。
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())

    # 计算损失函数。
    loss = tf.losses.mean_squared_error(labels=y_, predictions=y)
    # 创建模型优化器并得到优化步骤。
    train_op = tf.contrib.layers.optimize_loss(
        loss, tf.train.get_global_step(),
        optimizer="Adagrad", learning_rate=0.1)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        #test_feed = {x: input_x, y_: input_y}
        for i in range(TRAINING_STEPS):
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: input_x, y_: input_y})
            if i%100 == 0:
                print("After %d training step(s), loss on training batch is %g." % (i, loss_value))

        # test_acc = sess.run(accuracy, feed_dict=test_feed)
        # print("After %d training step(s),test accuracy using average model is %g" % (step, test_acc))


    return y, loss, train_op

def generate_data(seq):
    X = []
    y = []
    # 序列的第i项和后面的TIMESTEPS-1项合在一起作为输入；第i + TIMESTEPS项作为输
    # 出。即用sin函数前面的TIMESTEPS个点的信息，预测第i + TIMESTEPS个点的函数值。
    for i in range(len(seq) - TIMESTEPS):
        X.append(seq[i: i + TIMESTEPS])
        y.append([seq[i + TIMESTEPS]])
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

def main(argv=None):
    test_start = (TRAINING_EXAMPLES + TIMESTEPS) * SAMPLE_GAP
    test_end = test_start + (TESTING_EXAMPLES + TIMESTEPS) * SAMPLE_GAP
    train_X, train_y = generate_data(np.sin(np.linspace(
        0, test_start, TRAINING_EXAMPLES + TIMESTEPS, dtype=np.float32)))
    test_X, test_y = generate_data(np.sin(np.linspace(
        test_start, test_end, TESTING_EXAMPLES + TIMESTEPS, dtype=np.float32)))

    # 将训练数据以数据集的方式提供给计算图。
    ds = tf.data.Dataset.from_tensor_slices((train_X, train_y))
    ds = ds.repeat().shuffle(1000).batch(BATCH_SIZE)
    X, y = ds.make_one_shot_iterator().get_next()

    train(train_X,train_y)


if __name__ == "__main__":
    tf.app.run()
