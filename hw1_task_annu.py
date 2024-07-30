
def padding_and_byteconversion_encoder(encoded_text):
                extra_padding_bits = 8 - len(encoded_text) % 8 #For making it multiple of 8,as in memory,data will be stored as bytes
                for i in range(extra_padding_bits): #Making 0 as extra padded bits
                        encoded_text += "0"
                padded_info = "{0:08b}".format(extra_padding_bits)
                print("extra added bits information is",padded_info)
                encoded_text = encoded_text
                padded_encoded_text=encoded_text
                byte_array = bytearray() #Forming a byte array
                for i in range(0, len(padded_encoded_text), 8):
                        byte = padded_encoded_text[i:i+8]
                        byte_array.append(int(byte, 2))
                return byte_array


#Sir please see this function
def read_and_write_binary_string(encoded_text):
  #Input file is text file and we are writing in output binary file
                
                output_file_path = "outputfile" +".bin"
                binary_string=[]
                binary_string1=[]
                
                bytes_formed = padding_and_byteconversion_encoder(encoded_text)
                
                #Writing into binary string
                with open(output_file_path, 'wb') as output:
                   output.write(bytes(bytes_formed))
                file=open(output_file_path,'rb')
                read_bin=file.read()
                read_bin=str(read_bin)
                print("written binary file in bytes is:",read_bin)
                
                
                

                with open(output_file_path, 'r+') as file:
                    text1=file.read()
                    text1 = text1.rstrip()
                
                for char in text1:
                             ascii_value=ord(char)
                             binary_value=bin(ascii_value)
                             binary_string1.append(binary_value[2:])
                binary_string1=str(binary_string1)
                
                #print("binary string:",binary_string1)
            
                print("length of output binary sequence is",len(text1),"bytes")
                print("length of output binary sequence is",len(text1)*8,"bits")
                return output_file_path



encoded_text="0101010000101010111010000000000000000101010100100000"
read_and_write_binary_string(encoded_text)

