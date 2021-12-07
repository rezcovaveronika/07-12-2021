#Sastādīt programmu, kura lietotāja ievadīto vārdu izdrukā apgrieztā secībā.
def my_function(x):
  return x[::-1]
mytext = my_function("Man patīk programmēšana.")
print(mytext)