import json
import sys

def limpiar_recursivo(obj):
    keys_a_borrar = {
        'colab', 'executionInfo', 'user', 'userId', 'displayName',
        'auth_signature', 'authorship_tag', 'outputId', 'id'
    }

    if isinstance(obj, dict):
        for k in list(obj.keys()):
            if k in keys_a_borrar:
                del obj[k]
            else:
                limpiar_recursivo(obj[k])
    elif isinstance(obj, list):
        for item in obj:
            limpiar_recursivo(item)

def limpiar_total_ipynb(input_path, output_path):

    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    kernelspec = nb.get('metadata', {}).get('kernelspec', {})
    language_info = nb.get('metadata', {}).get('language_info', {})

    nb['metadata'] = {}
    if kernelspec:
        nb['metadata']['kernelspec'] = kernelspec
    if language_info:
        nb['metadata']['language_info'] = language_info

    for cell in nb.get('cells', []):
        cell['metadata'] = {}

        if 'execution_count' in cell:
            cell['execution_count'] = None

        if 'outputs' in cell:
            for output in cell['outputs']:
                if 'metadata' in output:
                    output['metadata'] = {}
                limpiar_recursivo(output)

    limpiar_recursivo(nb)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)

    print(f"D0ne!: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        limpiar_total_ipynb(sys.argv[1], sys.argv[1].replace('.ipynb', '_clean.ipynb'))
    else:
        print("Usage: python 00_meta_notebook.py file.ipynb")
