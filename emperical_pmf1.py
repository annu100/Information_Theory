from collections import Counter
import os
def find_frequency(file_path):
    file = open(file_path,'r')
    m=file.read()
    length=len(m)
    print("Length without compression is \n",length)
    with open(file_path) as file:
      emp_freq = Counter()
      for line in file:
           emp_freq += Counter(line)
    frequency=dict(emp_freq)
    return frequency

frequency=find_frequency('inputfile_16.txt')
emp_freq_prob=frequency
file = open('inputfile_16.txt','r')
m=file.read()
length=len(m)
for item,count in frequency.items():
    emp_freq_prob[item]/=length

emp_freq_prob=dict(emp_freq_prob)

print("Emperical pmf frequency of each symbol in given text file is:",emp_freq_prob)
keys_codes=['w','f','o','t','q']
values_codes=['000','001','010','011','1']
codes=dict(zip(keys_codes,values_codes))
reverse_mapping=dict(zip(values_codes,keys_codes))
# functions for compression
def make_frequency_dict(text):
		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency





def get_encoded_text(text):
		encoded_text = ""
		for character in text:
			encoded_text += codes[character]
		return encoded_text


def pad_encoded_text(encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


def get_byte_array(padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b

def compress_for_now():
		filename, file_extension = os.path.splitext('inputfile_16.txt')
		output_path = filename + ".bin"

		with open('inputfile_16.txt', 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			#frequency = make_frequency_dict(text)
			frequency=find_frequency('inputfile_16.txt')

			encoded_text = get_encoded_text(text)
			padded_encoded_text =pad_encoded_text(encoded_text)

			b = get_byte_array(padded_encoded_text)
			output.write(bytes(b))
                
		print("Compressed")
		return output_path
def compress():
		filename, file_extension = os.path.splitext(path)
		output_path = filename + ".bin"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			frequency = make_frequency_dict(text)
			

			encoded_text = get_encoded_text(text)
			padded_encoded_text =pad_encoded_text(encoded_text)

			b = get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("Compressed")
		return output_path


""" functions for decompression: """


def remove_padding(padded_encoded_text):
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:] 
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

def decode_text(encoded_text):
		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			if(current_code in reverse_mapping):
				character = reverse_mapping[current_code]
				decoded_text += character
				current_code = ""

		return decoded_text


def decompress(input_path):
		filename, file_extension = os.path.splitext(input_path)
		output_path = filename + "_decompressed" + ".txt"

		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
			bit_string = ""

			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_text = remove_padding(bit_string)

			decompressed_text = decode_text(encoded_text)
			
			output.write(decompressed_text)

		print("Decompressed")
		return output_path
   


compress_for_now()
print(compress_for_now())

file = open('inputfile_16.bin','rb')
k=file.read()
length_comp=len(k)
print("length of compressed file is",length_comp)
print(decompress('inputfile_16.txt'))

