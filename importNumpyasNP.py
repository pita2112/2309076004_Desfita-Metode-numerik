# Mendefinisikan fungsi f(x) = x + e^x
def f(x):
    return x + np.exp(x)

# Metode Biseksi
def biseksi(f, a, b, toleransi=1e-6, max_iterasi=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar.")
        return None
    
    iterasi_count = 0
    while (b - a) / 2 > toleransi and iterasi_count < max_iterasi:
        c = (a + b) / 2
        if f(c) == 0:  # Jika nilai tengah adalah akar
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi_count += 1
    return (a + b) / 2
    a, b = -1, 0
