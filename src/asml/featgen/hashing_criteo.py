#http://www.kddcup2012.org/c/kddcup2012-track2
from sklearn.metrics.pairwise import cosine_similarity
import sys
import csv
HASH_LENGTH=2
num_count_features=13
num_categorical_features=26
# length of the hash is going to be logm*8 bits
def hashing(vector, m=HASH_LENGTH):

	feature_vector=[0 for _ in xrange(1<<m)]
	for token in vector.split('|'):
		hashed_token=hash(token)
		index = hashed_token & ((1 << m) - 1)
		sign = (((hashed_token & (1 << m)) >> m) << 1) - 1
		feature_vector[index]+=sign
	return feature_vector

def init_agg_dict():
	dct_agg=defaultdict(float) #dictionary for aggregate measures 
	#initializing the dct_agg so that every output row has all the columns
	for clicked in target_fields.keys():
		dct_agg['Min_'+target_fields[clicked]]=0
		dct_agg['Count_'+target_fields[clicked]]=0
		dct_agg['Max_'+target_fields[clicked]]=0
		dct_agg['Mean_'+target_fields[clicked]]=0
	return dct_agg

def update_summary_vars(dct_agg,count_val, click):

	dct_agg['Min_'+target_fields[clicked]]=np.amin(dct_agg['Min_'+target_fields[clicked]],count_val)
	dct_agg['Max_'+target_fields[clicked]]=np.amax(dct_agg['Max_'+target_fields[clicked]],count_val)
	dct_agg['Mean_'+target_fields[clicked]]=dct_agg['Mean_'+target_fields[clicked]]* dct_agg['Count_'+target_fields[clicked]]
	dct_agg['Count_'+target_fields[clicked]]+=1
	return dct_agg

def update_similarity(dct_row, field1, field2):

	for i in range(len(hashable_fields)):
   		for j in range(i+1, len(hashable_fields)):
			field1=dct_row[hashable_fields[i]]
			field2=dct_row[hashable_fields[j]]
			hash1=hashing(field1)
			hash2=hashing(field2)
			similarity=cosine_similarity(hash1, hash2)[0][0]
	#print 'similarity_'+str(hashable_fields[i])+'_'+str(hashable_fields[j])
			dct_row['Similarity_'+str(hashable_fields[i])+'_'+str(hashable_fields[j])]=similarity								
	return dct_row
	
def readFile(filename):
	count_cols=['Count_'+str(i) for i in range(1,num_count_features+1)]
	categorical_cols=['Categorical_'+str(i) for i in range(1,num_categorical_features+1)]
	header=count_cols+categorical_cols
	target_fields={1:'click',0:'no_click'}
	header
	row_dict={}
	dct_agg=init_agg_dict()
	with open(filename,'r') as fin:
		line_count=0
		csv_r=csv.reader(fin)
		
		for row in csv_r:
			#print row	
			if line_count==0:
				print 'Header Read'
				line_count+=1
			else:
				dct_row={}

				# Populating the dictionary so that we can access each item by the field name
				# First elment is the click / no click
				for i in range(1,len(row)):
					dct_row[header[i]]=row[i]	
				clicked=row[0] # Clicked or not clicked
				for i in range(len(count_cols)):
					count_val=dct_row[count_cols[i]]
					dct_agg=update_summary_vars(dct_agg, count_val, clicked)
				# Handling categorical features
				hashable_fields=categorical_cols
				dct_row=update_smilarity(hashable_fields)
				dct_row.update(dct_agg)#merging the dictionaries
				row_dict[line_count-1]=dct_row# Accounting for header
				line_count+=1
	
	fout=open('out.txt','w')
	strout=','.join(each  for each in row_dict[0].keys())
	fout.write(strout+'\n')
	for each in row_dict:
		dct=row_dict[each]
		print dct
		strout=','.join(str(dct[each]) for each in dct)
		fout.write(strout+'\n')
	fout.close()
if __name__=='__main__':
	readFile(sys.argv[1])
