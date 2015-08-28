#!/usr/bin/python

import sys, os, time
from mod_pbxproj import XcodeProject

project = "__PROJECT_NAME__" # Only used in the file comment
files_group = "__FILES_GROUP__" # The Xcode group where you want the new files to be created
files_path = "__XCODE_FILES_PATH__" # The file system path where the new files will be created
xcode_proj_path = "__XCODE_PROJECT_PATH__"
super_class = "__SUPERCLASS__" # NSObject, UIViewController...
framework = "__FRAMEWORK__" ## Foundation, UIKit...
author = "__AUTHOR__"
class_name = sys.argv[1] # The class name will be the first argument of the script
header_file = "{0}.h".format(class_name)
implementation_file = "{0}.m".format(class_name)
header_full_file = "{0}/{1}".format(files_path, header_file)
implementation_full_file = "{0}/{1}".format(files_path, implementation_file)

def check_file(file):
    if os.path.exists(file):
        sys.exit()

def check_files_existence():
    check_file(header_full_file)
    check_file(implementation_full_file)

def create_files():
    try:
        date = time.strftime("%d/%m/%Y")
        copyright = "//\n//  {0}\n//  {1}\n//\n//  Created by {2} on {3}.\n//  Copyright (c) 2015, {1}. All rights reserved.\n//"
        header_copyright = copyright.format(header_file, project, author, date)
        implementation_copyright = copyright.format(implementation_file, project, author, date)

        # header file
        file = open(header_full_file,'w')
        file.write("{0}\n\n#import <{1}/{1}.h>\n\n@interface {2} : {3}\n\n@end\n".format(header_copyright, framework, class_name, super_class))
        file.close()

        # implementation file
        file2 = open(implementation_full_file,'w')
        file2.write("{0}\n\n#import \"{1}\"\n\n@implementation {2}\n\n@end\n".format(implementation_copyright, header_file, class_name))
        file2.close()

    except:
        print('Something went wrong')

def add_files_to_project():
    project = XcodeProject.Load('{0}/project.pbxproj'.format(xcode_proj_path))
    group = project.get_or_create_group(files_group)
    project.add_file_if_doesnt_exist(header_full_file, group)
    project.add_file_if_doesnt_exist(implementation_full_file, group)
    project.save()

check_files_existence()
create_files()
add_files_to_project()
