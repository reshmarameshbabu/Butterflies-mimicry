import argparse
import os
import utils


ap = argparse.ArgumentParser()
ap.add_argument('-i','--input-dir', type=str, default='images', help="input directory containing image files (default = images)", metavar='')
ap.add_argument('-c','--csv-file', type=str, default=None, help="(optional) XY coordinate file in csv format", metavar='')
ap.add_argument('-t','--tps-file', type=str, default=None, help="(optional) tps coordinate file", metavar='')


    
args = vars(ap.parse_args())

assert os.path.isdir(args['input_dir']), "Could not find the folder {}".format(args['input_dir'])
    
file_sizes=utils.split_train_test(args['input_dir'])

if args['csv_file'] is not None:
    dict_csv=utils.read_csv(args['csv_file'])
    utils.generate_dlib_xml(dict_csv,file_sizes['train'],folder='train',out_file='train.xml')
    utils.generate_dlib_xml(dict_csv,file_sizes['test'],folder='test',out_file='test.xml')
    utils.dlib_xml_to_tps('train.xml')
    utils.dlib_xml_to_tps('test.xml')
    
    
    
if args['tps_file'] is not None:
    dict_tps=utils.read_tps(args['tps_file'])
    utils.generate_dlib_xml(dict_tps,file_sizes['train_hindwings'],folder='train_hindwings',out_file='train-hindwings.xml')
    utils.generate_dlib_xml(dict_tps,file_sizes['val_hindwings'],folder='val_hindwings',out_file='val-hindwings.xml')
    utils.dlib_xml_to_tps('train-hindwings.xml')
    utils.dlib_xml_to_tps('val-hindwings.xml')
  
