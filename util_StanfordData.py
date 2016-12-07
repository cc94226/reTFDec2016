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
	count = 1
	
	try:
		while count < bottom_line + line_num:
			line = file.readlines()
			if line != null:
				if count >= bottom_line:
					labels 
