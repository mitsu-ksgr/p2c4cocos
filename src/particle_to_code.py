#!/usr/bin/python
# coding: utf-8

import argparse
import datetime
import locale
import plistlib
import sys


################################################################################
#   Constatns.
kScriptName     = 'ParticleToCode'
kGenLang_CPP    = 'cpp'
kGenLang_JS     = 'js'
kGenLang_Lua    = 'lua'

kSupportLangs = [kGenLang_CPP]

################################################################################
#   Arguments Parser
def parseArgs():
    parser = argparse.ArgumentParser(
        prog = kScriptName,
        description = 'Convert the ParticleSystem.plist to source codes for cocos2d-x v3.x!',
        version = '1.0.0')
    parser.add_argument('plist_path',
            help='Path to plist-file of the Particle System.')
    parser.add_argument('-o', '--output', nargs=1, default=None,
            help='Output directory.')
    parser.add_argument('-l', '--language', nargs=1, default=None,
            help='Language of output file.\nSelect from {0}. Default is "{1}".'.format(
                kSupportLangs, kGenLang_CPP))
    parser.add_argument('-n', '--namespace', nargs=1, default=None,
            help='[C++] Specify the namespace that generated code belongs.')
    return parser.parse_args()


################################################################################
#   Generator main.
def main() :
    args = parseArgs()
    base = plistlib.readPlist(args.plist_path)

    #############################################
    # Get options
    opt_plist = args.plist_path # if this is None, then it is 'Argument error'
    opt_output = './' if args.output is None else args.output[0]
    opt_lang = kGenLang_CPP if args.language is None else args.language[0]
    opt_lang = opt_lang.lower()

    # output dir
    opt_output += ('' if opt_output[-1] == '/' else '/')

    # output file name.
    opt_output_fname = args.plist_path[args.plist_path.rfind('/') + 1:]
    if opt_output_fname.rfind('.') > 0 :
        opt_output_fname = opt_output_fname[:opt_output_fname.rfind('.')]

    options = {
        'date' : datetime.datetime.today().strftime('%Y-%m-%dT%H:%M:%S'),
        'script_name' : kScriptName,
        'output_path' : opt_output[:opt_output.rfind('/') + 1],
        'output_file_name' : opt_output_fname,
    }

    #############################################
    # Generate
    result = False

    # C++ Mode.
    if opt_lang == kGenLang_CPP:
        import cpp.generator
        options['namespace'] = '' if args.namespace is None else args.namespace[0]
        result = cpp.generator.generate(base, options)

    # JS Mode.
    elif opt_lang == kGenLang_JS:
        print 'Sorry, JS is not yet implemented.'

    # Lua Mode.
    elif opt_lang == kGenLang_Lua:
        print 'Sorry, Lua is not yet implemented.'

    # Invalid Language
    else :
        print 'ERR: Invalid language. lang = {0}'.format(opt_lang)

    return result


if __name__ == '__main__':
    main()
