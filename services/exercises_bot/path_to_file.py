import os

project = 'services/exercises_bot'

# path = os.path.abspath(os.path.join('..', '..', project))


def list_dir(project):
    print(f'Содержимое директории {project}')
    for i in os.listdir(project):
        path = os.path.join(project, i)
        print('__', path)

d = 'data_files'
list_dir(project)
print(f'\n{os.listdir(project)}\n')
print(f'\n    {(os.path.join(os.path.dirname("garbagnya")))}')
