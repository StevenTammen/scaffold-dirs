#!/usr/bin/env python3

import importlib
import os
import sys
import shutil

def copy_and_rename(src_path, dest_dir, new_file_name):
    dest_path = dest_dir + '/' + new_file_name
    shutil.copy(src_path, dest_path)

def read_in_file(file_path):
    with open(file_path, "r", encoding="utf8") as f:
      return f.read()

def safe_open_w(path):
  '''
  Open "path" for writing, creating any parent directories as needed.

  https://stackoverflow.com/a/23794010
  '''
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w', encoding="utf8")

def copy_over_template_file_and_name_it_properly(template_path, dir_path, file_name):
    copy_and_rename(template_path, dir_path, file_name)

def fill_in_study_template(file_path, title, id):
    file_contents = read_in_file(file_path)
    file_contents = file_contents.replace('[title]', title)
    file_contents = file_contents.replace('[id]', id.upper())
    with safe_open_w(file_path) as f:
        f.writelines(file_contents)

def fill_in_chapter_notes_template(file_path, title, id):
    file_contents = read_in_file(file_path)
    file_contents = file_contents.replace('[title]', title)
    file_contents = file_contents.replace('[id]', id)
    with safe_open_w(file_path) as f:
        f.writelines(file_contents)

def fill_in_template(file_path, title, id, template):
    if(template == "study"):
        fill_in_study_template(file_path, title, id)
    elif (template == "chapter-notes"):
        fill_in_chapter_notes_template(file_path, title, id)

def build_dir_tree_node(scaffold_dirs_project_path, absolute_path_preceding_node, dir_tree_node):
    dir_path = absolute_path_preceding_node + '/' + dir_tree_node.name
    os.makedirs(dir_path, exist_ok=True)
    for leaf in dir_tree_node.leaves:
        copy_over_template_file_and_name_it_properly(scaffold_dirs_project_path + '/templates/' + leaf.template + '.md', dir_path, leaf.name + '.md')
        fill_in_template(dir_path + '/' + leaf.name + '.md', leaf.title, leaf.id, leaf.template)
    for subdir in dir_tree_node.subdirs:
        build_dir_tree_node(scaffold_dirs_project_path, dir_path, subdir)


scaffold_dirs_project_path = os.path.dirname(sys.argv[0])
dir_script_executing_from = os.getcwd()
config_to_use = 'ichthys_study_notes'
#config_to_use = 'bible_study_personal_notes'
#config_to_use = 'bible_study_study_notes'
config = importlib.import_module(f'config.{config_to_use}')
root_dir_tree_node = config.base_dir

#print(scaffold_dirs_project_path)

build_dir_tree_node(scaffold_dirs_project_path, dir_script_executing_from, root_dir_tree_node)
