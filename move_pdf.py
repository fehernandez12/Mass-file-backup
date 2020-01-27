import sys
import os
import shutil
import pathlib

def _menu():
    print('-----------------------------')
    print('------ PDF Transporter ------')
    print('-----------------------------')
    print('Selecciona una opción: ')
    print('[M]over archivos')
    print('[S]alir')
    opcion = input().upper()
    _switch_case(opcion)

def _solicitar_ruta_entrada():
    try:
        ruta_entrada = input('Ingresa la lista de archivos a transportar:\n')
        return ruta_entrada
    except Exception:
        print('Error: ' + str(Exception.with_traceback))
    finally:
        return ruta_entrada

def _convertir_archivo_en_lista(r):
    try:
        with open(r) as archivo:
            arr = [line.rstrip('\n') for line in archivo]
        return arr
    except IOError:
        print('Error: Ruta de archivo no válida.')
    except Exception:
        print('Error: ' + str(Exception.with_traceback))

def _solicitar_path():
    path = input('Ingresa el path en el que deseas replicar la estructura de carpetas:\n')
    return path

def _rutas_digester(x, y):
    y = y[:-1]
    for i in range(len(x)):
        x[i] = x[i][2::]
    for i in range(len(x)):
        x[i] = y + x[i]
    return x

def _crear_directorios(arr):
    arreglo_dir = []
    try:
        for item in arr:
            arr_item = item.split('/')
            arr_item.pop(-1)
            nuevo_directorio = ''
            for i in arr_item:
                nuevo_directorio += i
                nuevo_directorio += '/'
            arreglo_dir.append(nuevo_directorio)
        return arreglo_dir
    except IOError as e:
        print('Error de directorios.\n' + str(e.with_traceback))
    except Exception:
        print('Error: ' + str(Exception.with_traceback))

def _crear_carpetas(arr):
    try:
        for item in arr:
            if not os.path.exists(item):
	            pathlib.Path(item).mkdir(parents=True, exist_ok=True)
    except IOError as e:
        print('Error de directorior.\n' + str(e.with_traceback))
    except Exception:
        print('Error: ' + str(Exception.with_traceback))

def _mover_archivos(x, y):
    arr_log = []
    try: 
        count = 0
        for i in range(len(x)):
            shutil.copyfile(x[i], y[i])
            count +=1
            log = 'El archivo {} fue copiado.\n'.format(x[i])
            arr_log.append(log)
        with open('log.txt', 'w') as f:
            for i in arr_log:
                f.write(i)
        return count
    except IOError as e:
        print('Error de directorios.\n' + str(e.with_traceback))
        log = 'Error de directorios: ' + str(e)
        arr_log.append(log)
    except Exception:
        print('Error: ' + str(Exception.with_traceback))
        log = 'Error: ' + str(Exception)
        arr_log.append(log)
    finally:
        continue

def _switch_case(o):
    if o == 'M':
        ruta = _solicitar_ruta_entrada()
        lista_rutas = _convertir_archivo_en_lista(ruta)
        lista_rutas_salida = list(lista_rutas)
        path = _solicitar_path()
        lista_rutas_salida = _rutas_digester(lista_rutas_salida, path)
        lista_directorios = _crear_directorios(lista_rutas_salida)
        _crear_carpetas(lista_directorios)
        count = _mover_archivos(lista_rutas, lista_rutas_salida)
        print('Tarea finalizada. Se han copiado {} archivos.'.format(str(count)))
    elif o == 'S':
        sys.exit()
    else:
        print('Opción incorrecta.')

if __name__ == '__main__':
    while True:
        _menu()
    sys.exit()