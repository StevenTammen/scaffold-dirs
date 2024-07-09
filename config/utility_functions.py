from slugify import slugify
from .classes import *

def range_count(start, count):
    # range() returns from start to end - 1.
    return range(start, count+1)

def string_list(num_list):
    return map(str, num_list)

def build_parameterized_leaves(id_list, name_template, title_template, template):
    leaves_list = []
    for id in id_list:
        name = name_template.replace("[id]", id)
        title = title_template.replace("[id]", id.upper())
        leaves_list.append(LeafFile(id, name, title, template))
    return leaves_list

def build_parallel_subdirs(subdirs_dict, template, prefix = ''):
    subdirs = []
    slugified_prefix = slugify(prefix)
    if(len(prefix) > 0):
        prefix = prefix + ' - '
        slugified_prefix = slugified_prefix + '-'
    for subdir_name, num_files in subdirs_dict.items():
        slugified_subdir_name = slugify(subdir_name)
        subdir = Dir(slugified_subdir_name)
        subdir.leaves = build_parameterized_leaves(
            string_list(range_count(1, num_files)),
            f'{slugified_prefix}{slugified_subdir_name}-[id]',
            f'{prefix}{subdir_name} [id]',
            template
        )
        subdirs.append(subdir)
    return subdirs

def build_ordered_parallel_subdirs(subdirs_list, template):
    subdirs = []
    slugified_prefix = slugify(prefix)
    if(len(prefix) > 0):
        prefix = prefix + ' - '
        slugified_prefix = slugified_prefix + '-'
    for i in range_count(1, len(subdirs_list)):
        subdir_name = subdirs_list[i][0]
        num_files = subdirs_list[i][1]
        slugified_subdir_name = slugify(subdir_name)
        subdir = Dir(f'{i}-{slugified_subdir_name}')
        subdir.leaves = build_parameterized_leaves(
            string_list(range_count(1, num_files)),
            f'{slugified_prefix}{slugified_subdir_name}-[id]',
            f'{prefix}{subdir_name} [id]',
            template
        )
        subdirs.append(subdir)
    return subdirs
        