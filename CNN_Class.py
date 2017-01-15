import tensorflow as tf

class CNN_Class:

    def __init__(self, cnn_config):
        self.emb_dim = cnn_config.emb_dim or 200
        #number of embedding vocabulary can be set or use Stanford IE dataset's value 4139168
        self.emb_vocab_num = cnn_config.emb_vocab_num or 4139168

        self.cnn_window = 3
        self.cnn_step = 1
        self.cnn_num_windows = 128

        self.sequence_length = cnn_config.sequence_length
        self.num_classes = cnn_config.num_classes

        self.l2_reg_lambda= 0.0


        # Placeholders for input, output and dropout

        self.input_x = tf.placeholder(tf.int32, [None, self.sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, self.num_classes], name="input_y")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")
        self.embedding = tf.placeholder(tf.float32, [self.emb_vocab_num, self.emb_dim], name = "embedding")
        self.embedding_expanded = tf.expand_dims(self.embedding, -1)
        l2_loss = tf.constant(0.0)

        with tf.name_socpe("conv-maxpool"):
            #convolution layer
            window_shape = [self.cnn_window, self.emb_dim, 1, self.cnn_num_windows]
            #randomly initialize W
            W = tf.Variable(tf.truncated_normal(window_shape, stddev = 0.1), name = "W")
            b = tf.Variable(tf.constant(0.1, shape = [self.cnn_num_windows]), name = "b")
            conv = tf.nn.conv2d(
                self.embedding,
                W,
                strides = [1,1,1,1],
                padding = "VAILD",
                name = "conv"
            )
            h = tf.nn.relu(tf.nn.bias_add(conv, b), name = "relu")
            pooled = tf.nn.max_pool(
                h,
                ksize= [1, self.sequence_length - self.cnn_window + 1, 1, 1],
                strides = [1,1,1,1],
                padding = "VAILD",
                name = "pool"
            )

        self.h_pool = tf.concat(1,pooled)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1, self.cnn_num_windows])

        # Add dropout
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)

        with tf.name_scope("output"):
            W = tf.get_variable(
                "W",
                shape = [self.cnn_num_windows, self.num_classes],
                initializer = tf.contrib.layers.xavier_initialzer()
            )
            b = tf.Variable(tf.constant(0.1, shape = [self.num_classes]), name = "b")
            l2_loss += tf.nn.l2_loss(W)
            l2_loss += tf.nn.l2_loss(b)
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            self.predictions = tf.argmax(self.scores, 1, name="predictions")

        # CalculateMean cross-entropy loss
        with tf.name_scope("loss"):
            losses = tf.nn.softmax_cross_entropy_with_logits(self.scores, self.input_y)
            self.loss = tf.reduce_mean(losses) + self.l2_reg_lambda * l2_loss

        # Accuracy
        with tf.name_scope("accuracy"):
            correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")