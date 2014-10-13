#!/usr/bin/python
# coding: utf-8

import os

################################################################################
#   Constants.
kBaseDirName            = os.path.dirname(os.path.abspath(__file__))
kBaseFilePath_Header    = os.path.normpath(os.path.join(kBaseDirName, './base.hpp'))
kBaseFilePath_CPP       = os.path.normpath(os.path.join(kBaseDirName, './base.cpp'))
kExtensionForHeader     = '.hpp'
kExtensionForCPP        = '.cpp'
kTextureDirectoryPath   = ''

kGravityModeCodeBase = '''
    //-------------------------------------------
    // Emitter Mode
    this->_emitterMode              = {EmitterType};
    this->modeA.gravity.x           = {GravityX};
    this->modeA.gravity.y           = {GravityY};
    this->modeA.speed               = {Speed};
    this->modeA.speedVar            = {SpeedVariance};
    this->modeA.radialAccel         = {RadialAcceleration};
    this->modeA.radialAccelVar      = {RadialAccelVariance};
    this->modeA.tangentialAccel     = {TangentialAcceleration};
    this->modeA.tangentialAccelVar  = {TangentialAccelVariance};
    this->modeA.rotationIsDir       = {RotationIsDir};
'''

kRadiusModeCodeBase = '''
    //-------------------------------------------
    // Emitter Mode
    this->_emitterMode              = {EmitterType};
    this->modeB.startRadius         = {MaxRadius};
    this->modeB.startRadiusVar      = {MaxRadiusVariance};
    this->modeB.endRadius           = {MinRadius};
    this->modeB.endRadiusVar        = {MinRadiusVariance};
    this->modeB.rotatePerSecond     = {RotatePerSecond};
    this->modeB.rotatePerSecondVar  = {RotatePerSecondVariance};
'''

def _safeget(dic, key, default) :
    return dic[key] if key in dic else default


################################################################################
#   Generate Header.
def _gen_hpp_include_guard(namespace, file_name) :
    ns = [] if namespace is None else namespace.split('::')
    ig = '__'
    for n in ns:
        if n is not '':
            ig += n.upper() + '_'
    ig += file_name.upper() + '_H__'
    return ig

def _gen_hpp_namespace_codes(namespace) :
    ns = [] if namespace is None else namespace.split('::')
    begin, end = '', ''
    if len(ns) == 0 :
        return begin, end
    for n in ns :
        if n is not '':
            begin += 'namespace {0} {{{1}'.format(n, os.linesep)
            end = '}}  // namespace {0}{1}'.format(n, os.linesep) + end
    return begin, end

def _generate_header(plist, options) :
    # gen code parts.
    base = open(kBaseFilePath_Header, 'r').read()
    fname = options['output_file_name'] + kExtensionForHeader
    inc_guard = _gen_hpp_include_guard(
            options['namespace'], options['output_file_name'])
    ns_begin, ns_end = _gen_hpp_namespace_codes(options['namespace'])

    # generate header.
    return base.format(
        FileName        = fname,
        GenerateTime    = options['date'],
        ScriptName      = options['script_name'],
        IncludeGuard    = inc_guard,
        ClassName       = options['output_file_name'],
        NamespaceBegin  = ns_begin,
        NamespaceEnd    = ns_end,
        TotalParticles  = _safeget(plist, 'maxParticles', 100),
    )


################################################################################
#   Generate C++ implements.
def _gen_cpp_emitter_code(plist) :
    # Gravity Mode.
    if int(plist['emitterType']) == 0 :
        rotation_is_dir = _safeget(plist, 'rotationIsDir', False)
        code = kGravityModeCodeBase.format(
            EmitterType             = 'cocos2d::ParticleSystem::Mode::GRAVITY',
            GravityX                = _safeget(plist, 'gravityx', 0.0),
            GravityY                = _safeget(plist, 'gravityy', 0.0),
            Speed                   = _safeget(plist, 'speed', 0.0),
            SpeedVariance           = _safeget(plist, 'speedVariance', 0.0),
            RadialAcceleration      = _safeget(plist, 'radialAcceleration', 0.0),
            RadialAccelVariance     = _safeget(plist, 'radialAccelVariance', 0.0),
            TangentialAcceleration  = _safeget(plist, 'tangentialAcceleration', 0.0),
            TangentialAccelVariance = _safeget(plist, 'tangentialAccelVariance', 0.0),
            RotationIsDir           = ('true' if rotation_is_dir else 'false'),
        )

    # Radius Mode.
    else:
        code = kRadiusModeCodeBase.format(
            EmitterType             = 'cocos2d::ParticleSystem::Mode::RADIUS',
            MaxRadius               = _safeget(plist, 'maxRadius', 0.0),
            MaxRadiusVariance       = _safeget(plist, 'maxRadiusVariance', 0.0),
            MinRadius               = _safeget(plist, 'minRadius', 0.0),
            MinRadiusVariance       = _safeget(plist, 'minRadiusVariance', 0.0),
            RotatePerSecond         = _safeget(plist, 'rotatePerSecond', 0.0),
            RotatePerSecondVariance = _safeget(plist, 'rotatePerSecondVariance', 0.0),
        )
    return code

def _generate_cpp(plist, options) :
    # gen code parts.
    base = open(kBaseFilePath_CPP, 'r').read()
    fname = options['output_file_name'] + kExtensionForCPP
    header_fname = options['output_file_name'] + kExtensionForHeader

    # generate cpp.
    return base.format(
        # File properties.
        FileName        = fname,
        GenerateTime    = options['date'],
        ScriptName      = options['script_name'],
        ClassName       = options['output_file_name'],
        IncludeHeader   = './' + header_fname,

        # Particle properties.
        TotalParticles              = _safeget(plist, 'maxParticles', 100),
        ConfigName                  = _safeget(plist, 'configName', ''),
        Angle                       = _safeget(plist, 'angle', 0.0),
        AngleVariance               = _safeget(plist, 'angleVariance', 0.0),
        Duration                    = _safeget(plist, 'duration', -1.0),
        BlendFuncSource             = _safeget(plist, 'blendFuncSource', 0.0),
        BlendFuncDestination        = _safeget(plist, 'blendFuncDestination', 0.0),
        StartColorRed               = _safeget(plist, 'startColorRed', 0.0),
        StartColorGreen             = _safeget(plist, 'startColorGreen', 0.0),
        StartColorBlue              = _safeget(plist, 'startColorBlue', 0.0),
        StartColorAlpha             = _safeget(plist, 'startColorAlpha', 0.0),
        StartColorVarianceRed       = _safeget(plist, 'startColorVarianceRed', 0.0),
        StartColorVarianceGreen     = _safeget(plist, 'startColorVarianceGreen', 0.0),
        StartColorVarianceBlue      = _safeget(plist, 'startColorVarianceBlue', 0.0),
        StartColorVarianceAlpha     = _safeget(plist, 'startColorVarianceAlpha', 0.0),
        FinishColorRed              = _safeget(plist, 'finishColorRed', 0.0),
        FinishColorGreen            = _safeget(plist, 'finishColorGreen', 0.0),
        FinishColorBlue             = _safeget(plist, 'finishColorBlue', 0.0),
        FinishColorAlpha            = _safeget(plist, 'finishColorAlpha', 0.0),
        FinishColorVarianceRed      = _safeget(plist, 'finishColorVarianceRed', 0.0),
        FinishColorVarianceGreen    = _safeget(plist, 'finishColorVarianceGreen', 0.0),
        FinishColorVarianceBlue     = _safeget(plist, 'finishColorVarianceBlue', 0.0),
        FinishColorVarianceAlpha    = _safeget(plist, 'finishColorVarianceAlpha', 0.0),
        StartParticleSize           = _safeget(plist, 'startParticleSize', 0.0),
        StartParticleSizeVariance   = _safeget(plist, 'startParticleSizeVariance', 0.0),
        FinishParticleSize          = _safeget(plist, 'finishParticleSize', 0.0),
        FinishParticleSizeVariance  = _safeget(plist, 'finishParticleSizeVariance', 0.0),
        SourcePositionX             = _safeget(plist, 'sourcePositionx', 0.0),
        SourcePositionY             = _safeget(plist, 'sourcePositiony', 0.0),
        SourcePositionVarianceX     = _safeget(plist, 'sourcePositionVariancex', 0.0),
        SourcePositionVarianceY     = _safeget(plist, 'sourcePositionVariancey', 0.0),
        RotationStart               = _safeget(plist, 'rotationStart', 0.0),
        RotationStartVariance       = _safeget(plist, 'rotationStartVariance', 0.0),
        RotationEnd                 = _safeget(plist, 'rotationEnd', 0.0),
        RotationEndVariance         = _safeget(plist, 'rotationEndVariance', 0.0),
        EmitterConfigCodes          = _gen_cpp_emitter_code(plist),
        ParticleLifespan            = _safeget(plist, 'particleLifespan', 0.0),
        ParticleLifespanVariance    = _safeget(plist, 'particleLifespanVariance', 0.0),

        # Texture
        TextureDirectoryPath        = kTextureDirectoryPath,
        TextureFileName             = _safeget(plist, 'textureFileName', ''),
        TextureData                 = _safeget(plist, 'textureImageData', ''),
        YCoordFlipped               = _safeget(plist, 'yCoordFlipped', 1),
    )


################################################################################
#   main.
def generate(plist, options) :
    print 'C++: generate start...'
    output_path = options['output_path']
    path_header = output_path + options['output_file_name'] + kExtensionForHeader
    path_cpp    = output_path + options['output_file_name'] + kExtensionForCPP

    # Generate header.
    header = _generate_header(plist, options)
    print 'C++: succeeded to converted for header.'

    header_file = open(path_header, 'w')
    header_file.write(header)
    header_file.close()
    print 'C++: succeeded to generated header: {0}'.format(path_header)

    # Generate cpp.
    cpp = _generate_cpp(plist, options)
    print 'C++: succeeded to converted for C++ implements.'

    cpp_file = open(path_cpp, 'w')
    cpp_file.write(cpp)
    cpp_file.close()
    print 'C++: succeeded to generated C++ implements: {0}'.format(path_header)

    return True

