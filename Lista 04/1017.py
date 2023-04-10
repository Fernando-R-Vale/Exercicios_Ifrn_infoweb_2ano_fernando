tmpo_gasto = input()
kmporhora = input()
tmpgasto = int(tmpo_gasto)
Kmh = int(kmporhora)
gasto_decombustivel = Kmh * tmpgasto
combustivelgasto = gasto_decombustivel / 12
print(f'{combustivelgasto:.3f}')
