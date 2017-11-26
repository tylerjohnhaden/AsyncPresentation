def k_g_coroutine():
    print(' + inside coroutine 1')

    k = yield 'no values initialized yet'
    print(' + inside coroutine 2')

    g = yield 'thanks for k={}'.format(k)
    print(' + inside coroutine 3')

    yield 'thanks for g={}, now that I have k and g, k * g = {}'.format(g, k * g)
    print(' + inside coroutine 4')


kg_co = k_g_coroutine()

print(' - before')
print(next(kg_co))  # run up until first yield

print('\n - sending k = 7')
print(kg_co.send(7))

print('\n - sending g = 6')
print(kg_co.send(6))
