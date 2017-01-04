import tensorflow as tf

class CNN_Class:
    def __init__(self, config):
        self.mem_dim = config.mem_dim or 200
        self.emb_dim = config.emb_dim or 200
        self.pos_dim = config.pos_dim or 70
        self.left_pos_window = config.left_pos_window or 50
        self.right_pos_window = config.right_pos_window or 50
        self.learning_rate = config.learning_rate or 0.05
        self.batch_size = config.batch_size or 100
        self.emb_vocab = config.emb_vocab
        self.emb_v2wvocab = config.emb_v2wvocab
        self.left_pos_model = tf.nn.embedding.lookup(self.left_pos_window, self.pos_dim)
        self.right_pos_model = tf.nn.embedding.lookup(self.right_pos_window, self.pos_dim)
        self.emb_vecs = config.emb_vecs
        self.combine = config.combine or False

        if self.emb_vecs:
            self.initLookupTable(self.emb_vecs, self.emb_vocab)

        config.emb_vecs = None

        self.structure = config.structure or 'pcnn'
        #?
        self.reg = config.reg or 1e-4
        self.pcnn_window = 3
        self.pcnn_step = 1
        # join talbe
        self.combine_feature_model =
        # padding for cnn

        #temporal convolution not support by tensorflow??