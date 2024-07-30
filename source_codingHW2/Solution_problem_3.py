
import numpy as np
 

input_array=np.array([6.821506986225128, 6.80374122237135, -0.5676770607392423, 7.295043638901012, -1.9133586349994811, -1.542086374352342, -2.3848996331593213, -0.47448115402090707, 4.564972334540128, 3.1646560423266856, 7.447984928669229, 1.2865054202917814, 3.534673952554946, 4.242464823689296, -2.3356570749196814, -1.1554978093178632, -0.3974129998209026, 1.595214448909179, -1.108467438027814, 2.463692802574833, 7.283284250718335, 0.8133816653828578, -2.1813591617523147, 3.6097403419072323, 7.147945106176598, -2.3136198548666935, 2.79005154948114, 4.860647664838572, 5.384391538958587, 4.171590577462968, -2.9194838203016285, 1.266103999397696, 2.1856613195588577, 3.112505118969279, 4.480272844801899, 3.3905973023892977, 5.000154868498361, 2.539428346208575, 4.966615921694002, 7.570855516182867, 4.280651166277716, -1.3402191841982933, 5.810481080814, -1.7794511712813854, -0.6230969278352934, 6.488451623302382, 2.8977856598146885, 7.097555071490881, 2.9468703344741, 5.463844750140563, -0.18442233841209532, 5.26371043659093, 7.502227757670955, 3.1001234230871497, -2.0942006456126427, 2.398313344462434, -0.9572103170497863, 4.018297371070643, 4.383236573672985, 0.5255059665819024, 4.9862722563321515, -1.9232499907364804, 3.6084466909165056, 0.5103587625234502, -2.593920904915375, 6.079495867873858, 7.263970486594658, 0.6820556821403874, 0.92405032166304, -1.2603629075830451, -2.447719646125348, 0.39778427199589617, 3.9906551883373695, 7.21822514611625, 4.418455610515368, 0.4903554976727089, 3.0782792173063123, 2.6041027185389294, 4.370294179090541, -2.20614817017864, 4.727137840621014, -0.7567082872229025, 4.605374274511535, 0.5555448191271126, -1.5499734614863023, 6.845756616642918, 5.124364684785698, 3.4915497019467767, 2.824274826563084, -0.8061099875457103, 7.548053698990376, -2.805317132939281, 7.544691725467535, 4.940245886843597, 4.802796810915865, 7.562868099417884, 6.151485998787868, 3.2019494478008856, 1.288459071724755, 2.8068144852839247])

#for uniform distribution 
mean=sum(input_array)/len(input_array)
variance=sum((input_array-mean)**2)/len(input_array)
#mean=(alpha+beta)/2
#variance=(beta-alpha)**2/12
print("mean of uniformly distributed data is :",mean)
print("variance of uniformly distributed data is :",variance)

alpha=mean-np.sqrt(12*variance)/2
beta=(2*mean-alpha)
print("using mean and variance alpha is:",alpha,"beta is :",beta)
#using theoritical results:-
alpha =np.max(input_array)
beta =np.min(input_array)
t = (alpha +beta)/2
print('highest value of interval of our array is given by beta is ',np.max(input_array), 'smallest value of interval of our array is given by alpha is', np.min(input_array))
print("thresold is:",t)
# defining the quantisation 
def find_quantisation(input_array,alpha,beta):
    Q = []
    a = (3*alpha + beta)/4
    b = (alpha + 3*beta)/4

    for i in range(len(input_array)) :
       if input_array[i] >= t :
          Q.append(a)
       else :
          Q.append(b)
    return Q

#pmf of uniform distribution
def pmf_uniform(input_array,alpha,beta):
    mag=1/(alpha-beta)
    #pmf=[mag for i in range(input_array)]
    return mag

quantisation= find_quantisation(input_array,alpha,beta)

#statistical mse
def statistical_mse(input_array):
    mse=[]
    quantisation=find_quantisation(input_array,alpha,beta)
    mse=(np.sum((input_array-quantisation)**2))/len(input_array)
    return mse

#Using expectation mse calculation
def expectation_mse(input_array):
    mse=[]
    quantisation=find_quantisation(input_array,alpha,beta)
    pmf=pmf_uniform(input_array,alpha,beta)
    mse=(np.sum(pmf*((input_array-quantisation)**2)))/len(input_array)
    return mse
    
print("Quantisation array is given by:",quantisation)
E = ((alpha - beta)/4)**2
print('The value of MSE error for optimal case is',E)
print('Mean square error using expectation :',expectation_mse(input_array))
print('Mean square error using statistical method',statistical_mse(input_array))
