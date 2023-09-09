import dill

counter = 0

for i in range(100):
    counter += 1
    if i == 25:
        dill.dump_session('mysession.pkl')

dill.load_session('mysession.pkl')

print(i)
