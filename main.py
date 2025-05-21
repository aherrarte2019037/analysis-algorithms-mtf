def mtf(initial_config, requests):
    """
    Implementación del algoritmo Move to Front (MTF)
    
    Args:
        initial_config: Lista inicial de configuración
        requests: Secuencia de solicitudes
        
    Returns:
        total_cost: Costo total de acceso
        steps: Lista de pasos con la configuración, solicitud, costo y nueva configuración
    """
    config = initial_config.copy()  # Copia para no modificar la original
    total_cost = 0
    steps = []
    
    for request in requests:
        # Encontrar posición del elemento solicitado (índice + 1 para el costo)
        position = config.index(request)
        cost = position + 1
        
        # Actualizar costo total
        total_cost += cost
        
        # Crear una copia de la configuración actual antes de modificarla
        old_config = config.copy()
        
        # Mover el elemento al frente (aplicar MTF)
        config.pop(position)
        config.insert(0, request)
        
        # Guardar este paso
        steps.append({
            'old_config': old_config,
            'request': request,
            'cost': cost,
            'new_config': config.copy()
        })
    
    return total_cost, steps

def imtf(initial_config, requests):
    """
    Implementación del algoritmo Improved Move to Front (IMTF)
    
    Args:
        initial_config: Lista inicial de configuración
        requests: Secuencia de solicitudes
        
    Returns:
        total_cost: Costo total de acceso
        steps: Lista de pasos con la configuración, solicitud, costo y nueva configuración
    """
    config = initial_config.copy()
    total_cost = 0
    steps = []
    
    for idx, request in enumerate(requests):
        # Encontrar posición del elemento solicitado
        position = config.index(request)
        cost = position + 1
        
        # Actualizar costo total
        total_cost += cost
        
        # Crear una copia de la configuración actual
        old_config = config.copy()
        
        # Verificar si debemos mover el elemento al frente
        should_move = False
        if idx < len(requests) - 1 and position > 0:  # Solo si no es ya el primero
            # Mirar los próximos position elementos en la secuencia
            look_ahead_count = position
            if idx + look_ahead_count < len(requests):
                next_requests = requests[idx+1:idx+1+look_ahead_count]
                should_move = request in next_requests
        
        # Mover el elemento al frente solo si cumple la condición
        if should_move:
            config.pop(position)
            config.insert(0, request)
        
        # Guardar este paso
        steps.append({
            'old_config': old_config,
            'request': request,
            'cost': cost,
            'new_config': config.copy(),
            'moved': should_move
        })
    
    return total_cost, steps

def print_mtf_results(initial_config, requests, total_cost, steps):
    """
    Imprime los resultados del algoritmo MTF de forma detallada
    """
    print(f"Configuración inicial: {initial_config}")
    print(f"Secuencia de solicitudes: {requests}")
    print("\nPasos:")
    
    for i, step in enumerate(steps):
        print(f"Paso {i+1}:")
        print(f"  Configuración: {step['old_config']}")
        print(f"  Solicitud: {step['request']}")
        print(f"  Costo: {step['cost']}")
        print(f"  Nueva configuración: {step['new_config']}")
    
    print(f"\nCosto total: {total_cost}")
    print("\n" + "="*50 + "\n")

def print_imtf_results(initial_config, requests, total_cost, steps):
    """
    Imprime los resultados del algoritmo IMTF de forma detallada
    """
    print(f"Configuración inicial: {initial_config}")
    print(f"Secuencia de solicitudes: {requests}")
    print("\nPasos:")
    
    for i, step in enumerate(steps):
        print(f"Paso {i+1}:")
        print(f"  Configuración: {step['old_config']}")
        print(f"  Solicitud: {step['request']}")
        print(f"  Costo: {step['cost']}")
        moved_text = "Sí" if step['moved'] else "No"
        print(f"  ¿Se movió al frente?: {moved_text}")
        print(f"  Nueva configuración: {step['new_config']}")
    
    print(f"\nCosto total: {total_cost}")
    print("\n" + "="*50 + "\n")

def mtf_best_case(initial_config, length=20):
    """
    Genera la secuencia de solicitudes para el mejor caso del algoritmo MTF
    """
    # En el mejor caso, siempre solicitamos el primer elemento de la lista
    return [initial_config[0]] * length

def mtf_worst_case(initial_config, length=20):
    """
    Genera la secuencia de solicitudes para el peor caso del algoritmo MTF
    """
    n = len(initial_config)
    sequence = []
    
    # Crear un patrón cíclico que va de mayor a menor índice
    for i in range(length):
        index = n - 1 - (i % n)
        sequence.append(initial_config[index])
    
    return sequence

def main():
    # Configuración inicial para todos los ejercicios
    initial_config = [0, 1, 2, 3, 4]
    
    # Ejercicio 1
    print("EJERCICIO 1:")
    requests_1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    total_cost_1, steps_1 = mtf(initial_config, requests_1)
    print_mtf_results(initial_config, requests_1, total_cost_1, steps_1)
    
    # Ejercicio 2
    print("EJERCICIO 2:")
    requests_2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    total_cost_2, steps_2 = mtf(initial_config, requests_2)
    print_mtf_results(initial_config, requests_2, total_cost_2, steps_2)
    
    # Ejercicio 3
    print("EJERCICIO 3:")
    best_requests = mtf_best_case(initial_config, 20)
    best_cost, best_steps = mtf(initial_config, best_requests)
    print(f"La secuencia que produce el mínimo costo total es: {best_requests}")
    print(f"El costo total mínimo es: {best_cost}")
    
    # Ejercicio 4
    print("EJERCICIO 4:")
    worst_requests = mtf_worst_case(initial_config, 20)
    worst_cost, worst_steps = mtf(initial_config, worst_requests)
    print(f"La secuencia que produce el peor caso es: {worst_requests}")
    print(f"El costo total máximo es: {worst_cost}")
    
    # Ejercicio 5
    print("EJERCICIO 5:")
    print("Secuencia de solicitudes con repetición de 2:")
    requests_5a = [2] * 20  # [2, 2, 2, 2, ..., 2] (20 veces)
    total_cost_5a, steps_5a = mtf(initial_config, requests_5a)
    print_mtf_results(initial_config, requests_5a, total_cost_5a, steps_5a)
    
    print("Secuencia de solicitudes con repetición de 3:")
    requests_5b = [3] * 20  # [3, 3, 3, 3, ..., 3] (20 veces)
    total_cost_5b, steps_5b = mtf(initial_config, requests_5b)
    print_mtf_results(initial_config, requests_5b, total_cost_5b, steps_5b)
    
    print("Observación de patrón con repeticiones:")
    print(f"Costo total para secuencia con repetición de 2: {total_cost_5a}")
    print(f"Costo total para secuencia con repetición de 3: {total_cost_5b}")
    print("Cuando hay repetición de un mismo elemento, después del primer acceso,")
    print("el elemento se mueve al frente y todos los accesos posteriores tienen un costo de 1.")
    print("Por lo tanto, el patrón es: costo_inicial + (número_repeticiones - 1)")
    
    # Ejercicio 6
    print("EJERCICIO 6:")
    print("IMTF para el mejor caso de MTF:")
    imtf_best_cost, imtf_best_steps = imtf(initial_config, best_requests)
    print_imtf_results(initial_config, best_requests, imtf_best_cost, imtf_best_steps)
    
    print("IMTF para el peor caso de MTF:")
    imtf_worst_cost, imtf_worst_steps = imtf(initial_config, worst_requests)
    print_imtf_results(initial_config, worst_requests, imtf_worst_cost, imtf_worst_steps)
    
    print("Comparación:")
    print(f"MTF (mejor caso) - Costo total: {best_cost}")
    print(f"IMTF (mejor caso) - Costo total: {imtf_best_cost}")
    print(f"MTF (peor caso) - Costo total: {worst_cost}")
    print(f"IMTF (peor caso) - Costo total: {imtf_worst_cost}")

if __name__ == "__main__":
    main()