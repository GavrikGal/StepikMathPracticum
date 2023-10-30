import numpy

print(numpy.nan in set([numpy.nan]))

n = numpy.nan
m = numpy.nan
print(id(n), id(m), sep='\n')
print(id(n) == id(m))
print(n == m)