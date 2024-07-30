from collections import Counter
import os
import numpy as np
import binascii

file = open('inputfile_problem2_51.txt','r+')
m=file.read()
length=len(m)
print("Length without compression is \n",length,"bytes")

# Question2 part1

def entropy_calculation(P_x): #Functions for entropy calculations
  length=len(P_x)
  entropy=0
  for i in range(length):
    entropy+=-P_x[i]*np.log2(P_x[i])
  return entropy

#Functions for frequency calculations of each symbol of file
def find_frequency(file_path): 
    with open(file_path) as file:
      emp_freq = Counter()
      for line in file:
           emp_freq += Counter(line)
    frequency=dict(emp_freq)
    return frequency

  
#Emperical pmf of each symbol is calculated using this function
def find_emperical_probability(file_path): #Functions for frequency calculations
    with open(file_path) as file:
      emp_freq = Counter()
      for line in file:
           emp_freq += Counter(line)
    frequency=dict(emp_freq)
    emp_freq_prob=frequency
    for item,count in frequency.items():
      emp_freq_prob[item]/=length
    emp_freq_prob=dict(emp_freq_prob)
    return emp_freq_prob

emp_freq_prob=find_emperical_probability('inputfile_problem2_51.txt')

print("Emperical pmf  of each symbol in given text file is:",emp_freq_prob)
print("frequency  of each symbol in given text file is:",find_frequency('inputfile_problem2_51.txt'))
probability=list(find_emperical_probability('inputfile_problem2_51.txt').values())
print(probability)


entropy=entropy_calculation(probability)
print("entropy of given file is",entropy,"bits")

#Question 2 part 2,pen and paper solution is attached
#Inputs for our file
keys_codes=['c','a','b','d','e']

values_codes_huffman=['1','01','001','0000','0001'] #Huffman codes
values_codes_shannon=['0','100','1010','1011','11000']#Shannon codes
values_codes_shannon_alias=['01','1011','11011','11101','111110']#Shannon fano alias code
codes_huff=dict(zip(keys_codes,values_codes_huffman))
codes_shan=dict(zip(keys_codes,values_codes_shannon))
codes_shan_alias=dict(zip(keys_codes,values_codes_shannon_alias))
reverse_mapping_huff=dict(zip(values_codes_huffman,keys_codes))
reverse_mapping_shan=dict(zip(values_codes_shannon,keys_codes))
reverse_mapping_shan_alias=dict(zip(values_codes_shannon_alias,keys_codes))


#Compression algorith works by replacing actual ascii coded values to our codes which is calculated by
#Huffman,shannon and shannon alias coding
# example aaaabbbbcc=a4b4c2,which definitely reduces the size of file

def optimal_compressed_Size_using_entropy(file_path):
  probability=list(find_emperical_probability('inputfile_problem2_51.txt').values())
  entropy=entropy_calculation(probability)
  file = open(file_path,'r+')
  m=file.read()
  total_char=len(m)
  compressed_size_using_entropy=(total_char*entropy)/8
  return compressed_size_using_entropy 
#Question2 part 3-Compression-Encoding,zero padding and storing as byte string

# functions for compression


#Encoding function here replaces with old ascii value codes(which is stored in our computer)
#calculated codes


def encoding(text,codes):
                encoded = ""
                for char in text:
                        encoded += codes[char]
                return encoded

#function padding and byte conversion does the job of adding extra padding which is stored as header
#And byte conversion in order to store in computer memory
#File size is calculated in bytes
def padding_and_byteconversion_encoder(encoded_text,codes):
                extra_padding_bits = 8 - len(encoded_text) % 8 #For making it multiple of 8,as in memory,data will be stored as bytes
                for i in range(extra_padding_bits): #Making 0 as extra padded bits
                        encoded_text += "0"
                padded_info = "{0:08b}".format(extra_padding_bits)
                #print("extra added bits information is",padded_info)
                encoded_text = padded_info + encoded_text
                padded_encoded_text=encoded_text
                byte_array = bytearray() #Forming a byte array
                for i in range(0, len(padded_encoded_text), 8):
                        byte = padded_encoded_text[i:i+8]
                        byte_array.append(int(byte, 2))
                return byte_array


def read_binary_string(file_path):

                binary_string1=[]
                with open(file_path, 'r+') as file: 
                        text = file.read()
                        text = text.rstrip() #Removes any trailing character
                        #Writing into binary string
                for char in text:
                           ascii_value=ord(char)
                           binary_value=bin(ascii_value)
                           binary_string1.append(binary_value[2:])
                print(" input binary sequence in binary form is:",(''.join(binary_string1)))
                print("length of input file binary sequence is",len(binary_string1),"bytes")
                
              

read_binary_string('0101010')
#Here finally compression algorith does it's job using above mentioned functions           
def compression_algo(file_path,codes):
                #Input file is text file and we are writing in output binary file
                inputfilename, file_extension = os.path.splitext(file_path)
                output_file_path = inputfilename +"_compressed"+".bin"
                binary_string=[]
                with open(file_path, 'r+') as file, open(output_file_path, 'wb') as output:
                        text = file.read()
                        text = text.rstrip() #Removes any trailing character
                        frequency = find_frequency(file_path)
                        encoded_text = encoding(text,codes)
                        bytes_formed = padding_and_byteconversion_encoder(encoded_text,codes)
                        output.write(bytes(bytes_formed))
                        
                #"Compressed File is"
                return output_file_path



""" functions for decompression: """
#Decompression basically done by reading bit by bit codes,at one time,one bit is read
#If any codes of any symbol matches,it does the job of reverse mapping and performs decompression


#function padding_removal_and_decoding does the job of removing extra padding which is stored as header
#And byte conversion in order to store in computer memory and thus decoding is done
#File size is calculated in bytes
def padding_removal_and_decoding(padded_encoded_text,reverse_mapping):
                padded_info = padded_encoded_text[:8] #first 8 bits checking as header
                extra_padding = int(padded_info, 2) #Returning base of string padded_info

                padded_encoded_text = padded_encoded_text[8:] 
                encoded_text = padded_encoded_text[:-1*extra_padding]

                removed_padded=encoded_text
                current_code = ""
                final_decoding = ""

                for bit in removed_padded:
                        current_code += bit
                        if(current_code in reverse_mapping):
                                character = reverse_mapping[current_code]
                                final_decoding += character
                                current_code = ""

                return final_decoding

              
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])



#Question2 part 4-Compression-decoding,zero padding removal(header removal) and storing as byte string

#Decompression basically done by reading bit by bit codes,at one time,one bit is read
#If any codes of any symbol matches,it does the job of reverse mapping and performs decompression
#This function executes the decompression algorithm
def decompression_algo(input_file_path,reverse_mapping):
          #Using os ,we get final name with it's available extension
          #compressed sequence is binary file which is input here and output is text file for decompression algo
                filename, file_extension = os.path.splitext(input_file_path)
                output_file_path = filename + "_decompressed" + ".txt"

                with open(input_file_path, 'rb') as file, open(output_file_path, 'w+') as output:
                        bit_string = ""

                        byte = file.read(1)
                      
                        while (len(byte)):
                                byte = ord(byte) #RETURNS ASCII VALUE OF EACH BYTE
                                #bits=format(byte,"08b")
                                bits = bin(byte)[2:].rjust(8, '0')#Provides right justified version

                                bit_string += bits
                                byte = file.read(1) #reading each character
                                if (len(byte)<0):
                                   break

                        

                        content_decomp = padding_removal_and_decoding(bit_string,reverse_mapping)
                        
                        output.write(content_decomp)

                #"Decompressed File is" output_file_path
                return output_file_path
   

#Question2 part 5,displaying all results using
#1.Huffman coding
#2.Shannon coding
#3.Shannon-Fano-aliasing
#We will check with each coding scheme and compare file sizes
# we will also compare file size with entropy
#Optimal compressed file calculated using entropy
comp_size_entropy=optimal_compressed_Size_using_entropy('inputfile_problem2_51.txt')
print("Optimal Compressed file size calculated using entropy is:",comp_size_entropy,"bytes")
print("\n")
print("\n")
#With Huffman_coding
print("With Huffman coding\n")

print("Compressed file with huffman code is:")
print(compression_algo('inputfile_problem2_51.txt',codes_huff))
compressed_file=compression_algo('inputfile_problem2_51.txt',codes_huff)



file1 = open(compression_algo('inputfile_problem2_51.txt',codes_huff),'rb')
k_comp=file1.read()
length_comp=len(k_comp)
binary_string1=[]
with open(compressed_file, 'rb') as output:
                          text1=output.read()
output.close()                      #map(bin,bytearray(text1))
print("bytearray output compressed sequence is:",bytearray(text1),"and it's length is",len(text1),"bytes")

print("length of compressed file with huffman  is",length_comp,"bytes")
print("Decompression with huffman of Compressed file is:")
print(decompression_algo(compressed_file,reverse_mapping_huff))
file2 = open(decompression_algo(compressed_file,reverse_mapping_huff),'r+')
k_decomp=file2.read()
length_decomp=len(k_decomp)
print("length of decompressed file of compressed file with huffman  is",length_decomp,"bytes")
print("does decompressed file of compressed file is same as original file with huffman coding???:")
print(k_decomp==m)
print("\n")
print("\n")
#With shannon_coding
print("With shannon coding\n")
print("Compressed file with shannon coding is:")
print(compression_algo('inputfile_problem2_51.txt',codes_shan))
compressed_file=compression_algo('inputfile_problem2_51.txt',codes_shan)
file1 = open(compression_algo('inputfile_problem2_51.txt',codes_shan),'rb')
k_comp=file1.read()
length_comp=len(k_comp)
binary_string1=[]
with open(compressed_file, 'rb') as output:
                          text1=output.read()
output.close()                      
print("bytearray output compressed sequence is:",bytearray(text1),"and it's length is",len(text1))

print("length of compressed file with shannon coding is",length_comp,"bytes")
print("Decompression with sahnnon coding of Compressed file is:")
print(decompression_algo(compressed_file,reverse_mapping_shan))
file2 = open(decompression_algo(compressed_file,reverse_mapping_shan),'r+')
k_decomp=file2.read()
length_decomp=len(k_decomp)
print("length of decompressed file of compressed file is",length_decomp,"bytes")
print("does decompressed file of compressed file is same as original file with shannon coding???:")
print(k_decomp==m)

print("\n")
print("\n")
#With shannon alias coding
print("With shannon-fanno alias coding\n")
print("Compressed file with shannon alias coding is:")
print(compression_algo('inputfile_problem2_51.txt',codes_shan_alias))
compressed_file=compression_algo('inputfile_problem2_51.txt',codes_shan_alias)
file1 = open(compression_algo('inputfile_problem2_51.txt',codes_shan_alias),'rb')
k_comp=file1.read()
length_comp=len(k_comp)
binary_string1=[]
with open(compressed_file, 'rb') as output:
                          text1=output.read()
output.close()                      
print("bytearray output compressed sequence with shannon alias coding is:",bytearray(text1),"and it's length is",len(text1))

print("length of compressed file with shannon alias coding is",length_comp,"bytes")
print("Decompression with shannon alias coding of Compressed file is:")
print(decompression_algo(compressed_file,reverse_mapping_shan_alias))
file2 = open(decompression_algo(compressed_file,reverse_mapping_shan_alias),'r+')
k_decomp=file2.read()
length_decomp=len(k_decomp)
print("length of decompressed file of compressed  with shannon alias coding file is",length_decomp,"bytes")
print("does decompressed file of compressed file is same as original file with shannon alias coding???:")
print(k_decomp==m)
print("\n")
print("\n")
print("We can see the optimal compressed file size calculated using entropy is the lower bound for all coding scheme i.e huffman,shannon and shannon-alias coding compressed file size")
print("We can see the optimal compressed file size using huffman coding is the lowest among  all other coding scheme i.e shannon and shannon-alias coding compressed file size")


