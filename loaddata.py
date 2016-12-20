import util_StanfordData as utilSIE
import util_loadEmbedding as utilEMB

#emb_path = '/home/che313/data/embedding/SKIP_GRAM_200_v5_FIGER_Stanford_0d001_50iter.txt'
#test_dir = '/data/che313/reTF2016/bipath_stanford/test/'

emb_path = '/data/che313/reTF2016/embedding/SKIP_GRAM_200_v5_FIGER_Stanford_0d001_50iter.txt'
test_dir = '/data/che313/reTF2016/bipath_stanford/test'

max_line = 10000

#load embedding
emb_vectors, emb_vocab = utilEMB.load_embedding(emb_path)

#load file including test data
test_dataset = utilSIE.read_whole_stanfordIE_data(test_dir, emb_vocab, 1, max_line, 0)

