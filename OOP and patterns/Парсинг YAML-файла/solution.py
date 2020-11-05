import yaml


Levels = yaml.load(
'''
levels:
    - easy_level: {}
    - medium_level:
         enemy: ['rat']
    - hard_level:
        enemy:
            - rat
            - snake
            - dragon
        enemy_count: 10
''')


def create(loader, node):
    data = loader.construct_mapping(node)
    print(data)
# - !medium_level
#     enemy: ['rat']
# - !hard_level
#     enemy:
#         - rat
#         - snake
#         - dragon
#     enemy_count: 10

print(Levels)


class Lvl(yaml.YAMLObject):
    yaml_tag = 'levels'

    