import binascii

hex_string = "0123456789ABCDEF"
hex_key = "133457799BBCDFF1"

num_of_bits = 64
binary_string = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
binary_key = bin(int(hex_key, 16))[2:].zfill(num_of_bits)

random_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl"

''' key generation starts here'''
permuted_choice1 = {}

permuted_choice1 = {
	'1' : '57',
	'2' : '49',
	'3' : '41',
	'4' : '33',
	'5' : '25',
	'6' : '17',
	'7' : '9',
	'8' : '1',
	'9' : '58',
	'10': '50',
	'11': '42',
	'12': '34',
	'13': '26',
	'14': '18',
	'15': '10',
	'16': '2',
	'17': '59',
	'18': '51',
	'19': '43',
	'20': '35',
	'21': '27',
	'22': '19',
	'23': '11',
	'24': '3',
	'25': '60',
	'26': '52',
	'27': '44',
	'28': '36',
	'29': '63',
	'30': '55',
	'31': '47',
	'32': '39',
	'33': '31',
	'34': '23',
	'35': '15',
	'36': '7',
	'37': '62',
	'38': '54',
	'39': '46',
	'40': '38',
	'41': '30',
	'42': '22',
	'43': '14',
	'44': '6',
	'45': '61',
	'46': '53',
	'47': '45',
	'48': '37',
	'49': '29',
	'50': '21',
	'51': '13',
	'52': '5',
	'53': '28',
	'54': '20',
	'55': '12',
	'56': '4'

}
# print(binary_key)

# temp_key1 = binary_key[int(permuted_choice1.get('7'))]
# print(temp_key1)


permuted_key = ''
for i in range(1, 57):
	
	# print(random_string[int(permuted_choice1.get(str(i)))])
	permuted_key += binary_key[int(permuted_choice1.get(str(i)))-1]

print('----------------------------------------------------------------')
# print(permuted_key)
# print(len(permuted_key))
'''permuted key's data type is string'''

# print(binary_string[57])
# print(binary_string[49])
# print(binary_string[41])
# print(binary_string[33])
# print(random_string[25])
# print(random_string[17])
# print(random_string[9])

'''Populating a dictionary in order to get the value for the number of shifts in each iteration'''
shift_subkey = {
	'1' : '1',
	'2' : '1',
	'3' : '2',
	'4' : '2',
	'5' : '2',
	'6' : '2',
	'7' : '2',
	'8' : '2',
	'9' : '1',
	'10': '2',
	'11': '2',
	'12': '2',
	'13': '2',
	'14': '2',
	'15': '2',
	'16' :'1'
}
subkey_list = []


first_half_pk = permuted_key[0:int(len(permuted_key)/2)]
second_half_pk = permuted_key[int(len(permuted_key)/2):int(len(permuted_key))]
print(first_half_pk)
print(second_half_pk)
print(type(first_half_pk))

print('--------------------------------------------------------------------------------------')
concatentaed_keys_list = [].   # spelling mistake for concatenated
for x in range(0, 16):
	shift_amount = int(shift_subkey.get(str(x+1)))
	shift_bits_first = first_half_pk[0:shift_amount]
	first_half_pk = first_half_pk[shift_amount:int(len(first_half_pk))]+shift_bits_first
	shift_bits_second = second_half_pk[0:shift_amount]
	second_half_pk = second_half_pk[shift_amount:int(len(second_half_pk))]+shift_bits_second
	concatentaed_keys_list.append(first_half_pk+second_half_pk)

print('Now we will be using PC-2 table to get only 48 bits out of 56 bits of each subkey stored in concatentaed_keys_list')
permuted_choice2 = {}
permuted_choice2 = {
	'1' : '48',
	'2' : '17',
	'3' : '11',
	'4' : '24',
	'5' : '1',
	'6' : '5',
	'7' : '3',
	'8' : '28',
	'9' : '15',
	'10': '6',
	'11':'21',
	'12':'10',
	'13':'23',
	'14':'19',
	'15':'12',
	'16':'4',
	'17':'26',
	'18':'8',
	'19':'16',
	'20':'7',
	'21':'27',
	'22':'20',
	'23':'13',
	'24':'2',
	'25':'41',
	'26':'52',
	'27':'31',
	'28':'37',
	'29':'47',
	'30':'55',
	'31':'30',
	'32':'40',
	'33':'51',
	'34':'45',
	'35':'33',
	'36':'48',
	'37':'44',
	'38':'49',
	'39':'39',
	'40':'56',
	'41':'34',
	'42':'53',
	'43':'46',
	'44':'42',
	'45':'50',
	'46':'36',
	'47':'29',
	'48':'32'
}
final_subkey_list = []
for x in range(0, 16):
	new_key = ''
	key = concatentaed_keys_list[x]
	new_key += key[int(permuted_choice2.get(str(x+1)))-1]
	final_subkey_list.append(new_key)

print('After generating the list of 16 for the number of sub keys, we now generate the permutaion for the 64 bit block of data')

Initial_Permuation = {}
Initial_Permuation = {
	'1' : '58',
	'2' : '50',
	'3' : '42',
	'4' : '34',
	'5' : '26',
	'6' : '18',
	'7' : '10',
	'8' : '2',
	'9' : '60',
	'10': '52',
	'11': '44',
	'12': '36',
	'13': '28',
	'14': '20',
	'15': '12',
	'16': '4',
	'17': '62',
	'18': '54',
	'19': '46',
	'20': '38',
	'21': '30',
	'22': '22',
	'23': '14',
	'24': '6',
	'25': '64',
	'26': '56',
	'27': '48',
	'28': '40',
	'29': '32',
	'30': '24',
	'31': '16',
	'32': '8',
	'33': '57',
	'34': '49',
	'35': '41',
	'36': '33',
	'37': '25',
	'38': '17',
	'39': '9',
	'40': '1',
	'41': '59',
	'42': '51',
	'43': '43',
	'44': '35',
	'45': '27',
	'46': '19',
	'47': '11',
	'48': '3',
	'49': '61',
	'50': '53',
	'51': '45',
	'52': '37',
	'53': '29',
	'54': '21',
	'55': '13',
	'56': '5',
	'57': '63',
	'58': '55',
	'59': '47',
	'60': '39',
	'61': '31',
	'62': '23',
	'63': '15',
	'64': '7'
}

IP = ''
for x in range (1, 65):
	IP += binary_string[int(Initial_Permuation.get(str(x)))-1]

def fiestel_network(IP):
	L0 = IP[0:32]
	R0 = IP[32:len(IP)]

	L0 = R0


def f_function(R0, K0):



def R_value_expanison(R0):
	expansion = {}
	expansion = {
	'1' : '32',
	'2' : '1',
	'3' : '2',
	'4' : '3',
	'5' : '4',
	'6' : '5',
	'7' : '4',
	'8' : '5',
	'9' : '6',
	'10': '7',
	'11': '8',
	'12': '9',
	'13': '8',
	'14': '9',
	'15': '10',
	'16': '11',
	'17': '12',
	'18': '13',
	'19': '12',
	'20': '13',
	'21': '14',
	'22': '15',
	'23': '16',
	'24': '17',
	'25': '16',
	'26': '17',
	'27': '18',
	'28': '19',
	'29': '20',
	'30': '21',
	'31': '20',
	'32': '21',
	'33': '22',
	'34': '23',
	'35': '24',
	'36': '25',
	'37': '24',
	'38': '25',
	'39': '26',
	'40': '27',
	'41': '28',
	'42': '29',
	'43': '28',
	'44': '29',
	'45': '30',
	'46': '31',
	'47': '32',
	'48': '1'

	}
	new_R0 = '' 
	for x in range(1, 49):
		new_R0 += r0[int(expanison.get(str(x)))-1]

	return new_R0

def XOR_output(k, r0):
	output = ''
	for x in rnage(0, len(k)):
		if(k[x] == r0[x]):
			output+= '0'

		else:
			output+= '1'

	return output          # output 48 bits key


#takes 48 bits key and output 32 bit key by using very strange S boxes
count = 0
def S_box(xored_output):
	count += 1
	s1 = [[14, 4, 13, 1, 2, 15, 11, 6, 3,10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 9],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

	s2 = [[15, 1, 6, 14, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

	s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

	s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

	s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

	s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

	s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

	s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

	piece = []
	piece.append(xored_output[0:6])
	piece.append(xored_output[6:12])
	piece.append(xored_output[12:18])
	piece.append(xored_output[18:24])
	piece.append(xored_output[24:30])
	piece.append(xored_output[30:36])
	piece.append(xored_output[36:42])
	piece.append(xored_output[42:48])
	
	count = 0
	for items in piece:
		row = '0b' + items[0] + items[len(items)-1]
		col = '0b' + items[1:len(items)]
		row_num = int(row, 0)
		col_num = int(col, 0)
            if(count == 1):
                temp_list = s1[row_num]
                temp_num = temp_list[col_num]

            elif(count == 2):
                temp_list = s2[row_num]
                temp_num = temp_list[col_num]

            elif(count == 3):
                temp_list = s3[row_num]
                temp_num = temp_list[col_num]

            elif(count ==4):
            	temp_list = s4[row_num]
                temp_num = temp_list[col_num]

            elif(count == 5):
            	temp_list = s5[row_num]
                temp_num = temp_list[col_num]

            elif(count == 6):
            	temp_list = s6[row_num] 
                temp_num = temp_list[col_num]

            elif(count ==7):
            	temp_list = s7[row_num] 
                temp_num = temp_list[col_num]

            elif(count == 8):
            	temp_list = s8[row_num]
                temp_num = temp_list[col_num]

        count = count + 1


    p = {}
    p{
    	'1':'16',
    	'2':'7',
    	'3':'20',
    	'4':'21',
    	'5':'29',
    	'6':'12',
    	'7':'28',
    	'8':'17',
    	'9':'1',
    	'10':'15',
    	'11':'23',
    	'12':'26',
    	'13':'5',
    	'14':'18',
    	'15':'31',
    	'16':'10',
    	'17':'2',
    	'18':'8',
    	'19':'24',
    	'20':'14',
    	'21':'32',
    	'22','27',
    	'23':'3',
    	'24':'9',
    	'25':'19',
    	'26':'13'
    	'27':'30',
    	'28':'6',
    	'29':'22',
    	'30':'11',
    	'31':'4',
    	'32':'25'
    }


def f_fucntion():
	
                




		


























