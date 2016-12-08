def read_whole_stanfordIE_data(base_dir, emb_vocab,bottom_line,line_num,window_size):


	label_file_path = base_dir+"label"
	feature_file_path = base_dir+"feature"

	bipath_seq_lr_path = base_dir+"lPos.ids"
    	bipath_seq_rl_path = base_dir+"rPos.ids"
    	sentence_path = base_dir+"text.toks"

	dataset = {}

	dataset.label = 

def read_labels(path,bottom_line,line_num):
	labels = {}
	file = open(path)
	count = 0
	
	while count < bottom_line + line_num:
		line = file.readlines()
		if line != null:
			if count >= bottom_line:
				labels[len(labels) + 1] = (int)line
			count++
		else break
	file.close()
	return labels
		
def read_features(path,bottom_line,line_num):
	features = {}
	file = openpath()
	count = 1

	whule count < botton_line + line_num do
		line = file.readlines()
		if line != null:
			tokens = line.split()
			tokens_len = len(tokens)
			feature_matrix = numpy.zeros((tokens_len, 2))
		
			for i in range(0,tokens_len):
				
