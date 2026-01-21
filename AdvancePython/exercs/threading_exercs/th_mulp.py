import multiprocessing
import threading
import time

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def tarefa_leve(n=None):
    """Uma tarefa muito rápida"""
    return sum(i for i in range(1000))

def tarefa_pesada(n=None):
    """Uma tarefa que realmente usa CPU - CORRIGIDA para aceitar argumento"""
    result = 0
    # Aumentei o range para fazer uma tarefa realmente pesada
    for _ in range(500000):
        result += sum(i*i for i in range(100))
    return result

def tarefa_pesada_sem_arg():
    """Versão alternativa sem argumento - para usar com apply_async"""
    result = 0
    for _ in range(500000):
        result += sum(i*i for i in range(100))
    return result

if __name__ == "__main__":
    print("=== Teste 1: Fatorial de 20 (tarefa muito leve) ===")
    
    n = 20
    num_execucoes = 1000
    
    # Serial (baseline)
    start = time.time()
    for _ in range(num_execucoes):
        fatorial(n)
    serial_time = time.time() - start
    
    # Threading
    start = time.time()
    threads = []
    for _ in range(num_execucoes):
        t = threading.Thread(target=fatorial, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    threading_time = time.time() - start
    
    # Multiprocessing (com Pool para reuso de processos)
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(fatorial, [n] * num_execucoes)
    multiprocessing_time = time.time() - start
    
    print(f"Serial: {serial_time:.4f}s")
    print(f"Threading: {threading_time:.4f}s (overhead: {threading_time/serial_time:.1f}x)")
    print(f"Multiprocessing: {multiprocessing_time:.4f}s (overhead: {multiprocessing_time/serial_time:.1f}x)")
    
    print("\n" + "="*50)
    print("=== Teste 2: Tarefa mais pesada ===")
    print("="*50)
    
    # Serial
    start = time.time()
    for _ in range(4):  # Reduzi para 4 porque a tarefa é pesada
        tarefa_pesada()
    serial_time = time.time() - start
    print(f"Serial: {serial_time:.4f}s")
    
    # Threading (GIL vai atrapalhar - será quase serial)
    start = time.time()
    threads = []
    for _ in range(4):
        t = threading.Thread(target=tarefa_pesada)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    threading_time = time.time() - start
    print(f"Threading: {threading_time:.4f}s (GIL limitation: {threading_time/serial_time:.1f}x)")
    
    # Multiprocessing - VERSÃO 1: com argumento
    print("\n--- Multiprocessing (com argumento) ---")
    start = time.time()
    with multiprocessing.Pool() as pool:
        # Passamos None para cada chamada
        results = pool.map(tarefa_pesada, [None] * 4)
    multiprocessing_time = time.time() - start
    print(f"Multiprocessing: {multiprocessing_time:.4f}s (speedup: {serial_time/multiprocessing_time:.1f}x)")
    
    # Multiprocessing - VERSÃO 2: sem argumento usando apply_async
    print("\n--- Multiprocessing (sem argumento, usando apply_async) ---")
    start = time.time()
    with multiprocessing.Pool() as pool:
        # Cria uma lista de tarefas
        tasks = [pool.apply_async(tarefa_pesada_sem_arg) for _ in range(4)]
        # Coleta os resultados
        results = [task.get() for task in tasks]
    multiprocessing_time2 = time.time() - start
    print(f"Multiprocessing: {multiprocessing_time2:.4f}s (speedup: {serial_time/multiprocessing_time2:.1f}x)")
    
    print("\n" + "="*50)
    print("RESUMO:")
    print("="*50)
    print("Para tarefas CPU-bound pesadas:")
    print(f"- Threading tem overhead do GIL: {threading_time/serial_time:.1f}x mais lento")
    print(f"- Multiprocessing tem speedup: {serial_time/multiprocessing_time:.1f}x mais rápido")
    print(f"- Número de núcleos disponíveis: {multiprocessing.cpu_count()}")