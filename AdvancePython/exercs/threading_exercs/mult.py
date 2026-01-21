from multiprocessing import Pool
import multiprocessing

# def processar_imagem(img):
#     return img * 2

# if __name__ == '__main__':
#     images = [1, 2, 3, 4, 5]
#     with Pool(processes=3) as pool:
#         resultados = pool.map(processar_imagem, images)
#     print(resultados)


def calc_quadrado(n, q):
    q.put(n * n)

if __name__ == "__main__":
    n = 2
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_quadrado, args=(n,q))

    p1.start()
    p1.join()
    print(q.get())