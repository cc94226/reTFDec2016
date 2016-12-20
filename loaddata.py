import util_StanfordData as utilSIE
import util_loadEmbedding as utilEMB

#=========================

#data path for loacl test

#=========================
#emb_path = '/home/che313/data/embedding/SKIP_GRAM_200_v5_FIGER_Stanford_0d001_50iter.txt'
#test_dir = '/home/che313/data/bipath_stanford/test/'
#label_list_path = '/home/che313/data/bipath_stanford/LabelList'
#feature_list_path = '/home/che313/data/bipath_stanford/FeaturesList'

#=========================

#data path for server

#=========================
emb_path = '/data/che313/reTF2016/embedding/SKIP_GRAM_200_v5_FIGER_Stanford_0d001_50iter.txt'
test_dir = '/data/che313/reTF2016/bipath_stanford/test/'
label_list_path = '/data/che313/reTF2016/bipath_stanford/LabelList'
feature_list_path = '/data/che313/reTF2016/bipath_stanford/FeaturesList'

max_line = 10000

#load embedding
M, emb_vocab = utilEMB.load_embedding(emb_path)

#load label list
label_list = utilSIE.read_label_or_feature(label_list_path)

#load feature list, get its sie number and empty feature list
feature_list = utilSIE.read_label_or_feature(feature_list_path)
feature_size = len(feature_list)


#load file including test data
test_dataset = utilSIE.read_whole_stanfordIE_data(test_dir, emb_vocab, 1, max_line, 0)

