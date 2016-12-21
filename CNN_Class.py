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