
def k_g_coroutine():
    k = yield 'no values initialized yet'
    g = yield 'thanks for k={}'.format(k)
    yield 'thanks for g={}, now that I have k and g, k * g = {}'.format(g, k * g)


kg_co = k_g_coroutine()

print(' - before')
print(next(kg_co))  # run up until first yield

print('\n - sending k = 7')
print(kg_co.send(7))

print('\n - sending g = 6')
print(kg_co.send(6))



