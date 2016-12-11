def read_whole_stanfordIE_data(base_dir, emb_vocab,bottom_line,line_num,window_size):


	label_file_path = base_dir+"label"
	feature_file_path = base_dir+"feature"

	bipath_seq_lr_path = base_dir+"lPos.ids"
    	bipath_seq_rl_path = base_dir+"rPos.ids"
    	sentence_path = base_dir+"text.toks"

	dataset = {}

	dataset.label = 
	dataset.sparse_feature = 
	dataset.sents =
	dataset.sentences_bipath_seq_lr = read_seq_ids(bipath_seq_lr_path,bottom_line,line_num)
	dataset.trees_bipath_seq_lr = read_trees_from_seq_ids(dataset.sentences_bipath_seq_lr,window_size,dataset.sents,0,{},'l')


def read_labels(path,bottom_line,line_num):
	labels = {}
	file = open(path)
	count = 0
	
	while count < bottom_line + line_num:
		line = file.readlines()
		if line != None:
			if count >= bottom_line:
				labels[len(labels) + 1] = (int)line
			count++
		else break
	file.close()
	return labels
		
def read_features(path,bottom_line,line_num):
	features = {}
	file = open(path)
	count = 1

	whule count < botton_line + line_num:
		line = file.readlines()
		if line != None:
			tokens = line.split()
			tokens_len = len(tokens)
			feature_matrix = []		
			for i in range(0,tokens_len):
				feature_matrix.append([])				
				a[i].append((int)tokens[i] + 1)
				a[i].append(1)
			#end for i
		count++
	#end while
	
	file.close()
	return feature_matrix

def read_sentences(sentence_path,emb_vocab,bottom_line,line_num):
	sentences = []
	file = open(path)
	count = 1
	while count , bottem_line + line_num:
		line = file.readlines()
		if line != None and count > = bottom_line:
			tokens = line.split()
			tokens_len = len(tokens)
			#------------------
			snet = []
			
			for i in range(1,tokens_len):
				idx = emb_vocab[tokens[i]]
				if idx != None:
					sent[i] = idx
				else:
					sent[i] = emb_vocab['#UNKNOWN#']
					print "%s is not in the vocab." %(tokens[i])
				#end else
			#end for i
		sentences.append(snet)
		count++
	#end while
	
	file.close()
	return sentences

def read_seq_ids(seq_path,bottom_line,line_num):
	seq_id = []
	file = open(seq_path)
	count = 1
	
	while count < bottom_line + line_num:
			line = file.readlines()
			if line != None and count >= bottom_line:
				tokens = line.split()
				tokens_len = len(tokens)
				#--------
				ids = []
				for i in range(1,len):
					ids[i] = (int)(tokens[i]) +1
					
				seq_ids.append(ids)
			#end if
		count++
	#end while
	
	fiel.close()
	return seq_ids

def read_trees_from_seq_ids(seqs,window_size,sents,predict_root,filter_list,direction):
	tree = []
	
	for i in range(1, len(seqs)):
		temp_seq = seqs[i]
		temp_sent = sents[i]
		temp_parents = []
		for j in range(1, len(temp_seq))
			temp_parents[j] = j + 1
		
		tree = read_tree(parents,seq,window_size,sent,predict_root,filter_list,direction)
		trees.append(tree)
	#end for i
	return trees
