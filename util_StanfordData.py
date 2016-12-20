import treelstm_util as treelstm
import tree_Class as Tree_Class


def read_whole_stanfordIE_data(base_dir, emb_vocab, bottom_line, line_num, window_size):
    label_file_path = base_dir + 'label'
    feature_file_path = base_dir + 'feature'

    bipath_seq_lr_path = base_dir + 'lSeq.ids'
    bipath_seq_rl_path = base_dir + "rSeq.ids"
    sentence_path = base_dir + "text.toks"

    dataset = {}

    dataset['label'] = read_labels(label_file_path, bottom_line, line_num)
    dataset['sparse_feature'] = read_features(feature_file_path, bottom_line, line_num)
    dataset['sents'] = read_sentences(sentence_path, emb_vocab, bottom_line, line_num)
    dataset['sentences_bipath_seq_lr'] = read_seq_ids(bipath_seq_lr_path, bottom_line, line_num)
    dataset['trees_bipath_seq_lr'] = read_trees_from_seq_ids(dataset['sentences_bipath_seq_lr'], window_size,
                                                             dataset.sents, 0, {}, 'l')
    dataset['sentences_bipath_seq_rl'] = read_seq_ids(bipath_seq_rl_path, bottom_line, line_num)
    dataset['trees_bipath_seq_rl'] = read_trees_from_seq_ids(dataset['sentences_bipath_seq_rl'], window_size,
                                                             dataset.sents, 0, {}, 'r')
    dataset['size'] = len(dataset)
    return dataset

def read_labels(path, bottom_line, line_num):
    labels = []
    file = open(path)
    count = 0

    while count < bottom_line + line_num:
        line = file.readlines()
        if line:
            if count >= bottom_line:
                labels.append( int(line) )
            count += 1
        else:
            break
    file.close()
    return labels


def read_features(path, bottom_line, line_num):
    features = []
    file = open(path)
    count = 0

    while count < bottom_line + line_num:
        line = file.readline()
        if line:
            tokens = line.split()
            tokens_len = len(tokens)
            feature_matrix = []
            for i in range(0, tokens_len):
                feature_matrix.append([])
                feature_matrix[i].append(int(tokens[i]))
                feature_matrix[i].append(1)
            # end for i
            features.append(feature_matrix)
        count += 1
    # end while

    file.close()
    return features


def read_sentences(sentence_path, emb_vocab, bottom_line, line_num):
    sentences = []
    file = open(sentence_path)
    count = 0
    while count < bottom_line + line_num:
        line = file.readline()
        if line and count >= bottom_line:
            tokens = line.split()
            tokens_len = len(tokens)
            # ------------------
            sent = []

            for i in range(0, tokens_len):
                idx = emb_vocab[tokens[i]]
                if idx:
                    sent[i] = idx
                else:
                    sent[i] = emb_vocab['#UNKNOWN#']
                    print "%s is not in the vocab." % (tokens[i])
                # end else
            # end for i
            sentences.append(sent)
        count += 1
    # end while

    file.close()
    return sentences


def read_seq_ids(seq_path, bottom_line, line_num):
    seq_ids = []
    file = open(seq_path)
    count = 0

    while count < bottom_line + line_num:
        line = file.readline()
        if line and count >= bottom_line:
            tokens = line.split()
            tokens_len = len(tokens)
            # --------
            ids = []
            for i in range(0, tokens_len):
                ids.append( int(tokens[i]) + 1 )

            seq_ids.append(ids)
        # end if
        count += 1
    # end while

    file.close()
    return seq_ids


def read_trees_from_seq_ids(seqs, window_size, sents, predict_root, filter_list, direction):
    trees = []

    for i in range(0, len(seqs)):
        temp_seq = seqs[i]
        temp_sent = sents[i]
        temp_parents = []
        for j in range(0, len(temp_seq)):
            temp_parents[j] = j + 1

        tree = read_tree(temp_parents, temp_seq, window_size, temp_sent, predict_root, filter_list, direction)
        trees.append(tree)
    # end for i
    return trees

def read_tree(parents, seqs, window_size, sent, predict_root, filter_list, direction):
    size = len(parents)
    trees = []
    root = Tree_Class.Tree()
    root_count = 0

    for i in range(0,size):
        if not trees[i]:
            idx = i

            while True:
                temp_parent = parents[idx]
                sent_idx = seqs[idx]
                tree = Tree_Class.Tree()
                #?????
                tree.is_root = False

                prev = None
                if prev:
                    tree.add_child(prev)

                trees[idx] = tree
                tree.sent_idx = sent_idx
                tree.idx = idx

                treelstm.set_spans(tree)

                c = 0
                for j in range(tree.lo - window_size, tree.hi + window_size):
                    if j >= 1 and j <= len(sent) and (j > tree.hi or j < tree.lo):
                        if not filter_list[sent[j][1]]:
                            c += 1
                            treelstm.addtoset(tree.context_word_id_set, sent[j][1])

                        else:
                            treelstm.addtoset(tree.context_word_id_set, sent[j][1])

                if trees[temp_parent]:
                    trees[temp_parent].add_child(tree)
                elif temp_parent == size + 1:
                    root = tree
                    root_count = root_count + 1
                    tree.is_root = True
                else:
                    prev = tree
                    idx = parents

    if predict_root == 2:
        root.context_word_id_set = []
        temp_lo = 0
        temp_hi = 0
        if direction == 'l':
            temp_lo = root.lo +1
            temp_hi = root.hi
        elif direction == 'r':
            temp_lo = root.lo
            temp_hi = root.hi -1
        for j in range(temp_lo, temp_hi):
            treelstm.addtoset(root.context_word_id_set, sent[j][1])

    return root

#origin: torchIE -> IEUnsupervisieiedPretrain/FileFOrmatConvertFuncs.lua/read_si_map
#!!!!!! no filter_realtion option
def read_label_or_feature(path):
    file = open(path)
    map = {}
    map.i2s, map.s2i = {}, {}
    count = 0
    while (True):
        temp_line = file.readline()
        if temp_line != 'no_relation':
            count += 1
            map.i2s[count] = temp_line
            map.s2i[temp_line] = count

    map.size = count
    file.close()
    return map