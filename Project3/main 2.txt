# Write a program that will iteratively predict and
# correct based on the location measurements
# and inferred motions shown below.


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

def correct(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [0., 1., 1., 2., 1.]
measurement_var = 4.
motion_var = 2.
mean = 4
var = 10000

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].

# Insert code here

for i in range(len(motion)):
    result = predict(mean, var, motion[i], motion_var)
    print ("predict", predict(mean, var, motion[i], motion_var))
    ALTresult = correct(result[0], result[1], measurements[i], measurement_var)
    print ("correct", correct(result[0], result[1], measurements[i], measurement_var))
    mean = ALTresult[0]
    var = ALTresult[1]
print (ALTresult)
