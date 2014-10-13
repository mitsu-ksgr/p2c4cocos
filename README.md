p2c4cocos
=========
### Particle-System.plist to Code for cocos2d-x (ver 3.x)


# Description
Convert the ParticleSystem.plist to source codes for cocos2d-x v3.x!

パーティクル設定ファイル(.plist)をcocos2d-x v3.x用のコードに変換します。<br>
実行時のファイル読み込み処理を無くせるため、その部分に関して高速化が期待できます。<br>
対応している.plistは、cocos2d-xで読み込めるモノでしたら大丈夫なハズです（大して試してない）。

スクリプトの作成には、cocos2d-xの__"ParticleSystem::initWithDictionary"__のコードを参考にしました。
[ParticleSystem::initWithDictionary](https://github.com/cocos2d/cocos2d-x/blob/v3/cocos/2d/CCParticleSystem.cpp)


# Support
- [C++] cocos2d-x v3.0 or later


# Installation
```sh
$ git clone git@github.com:mitsuaki-n/p2c4cocos.git
```

# How to use
### Basic usage
```sh
Minimum.
$./p2c4cocos ./path/to/Particle.plist

Specify an output-path
$./p2c4cocos ./path/to/Particle.plist -o ./path/to/output/dir

Specify C++ Namespace
$./p2c4cocos ./path/to/Particle.plist -l cpp -n Sample::Effect
>>> generate Sample::Effect::Particle class.
```

### Example to use sample files.
in shell.
```sh
$ cd /path/to/project
$ ./p2c4cocos ./sample/SampleParticle.plist -o ./sample -l cpp -n Sample::Effect
>>> ./sample/SampleParticle.hpp
>>> ./sample/SampleParticle.cpp

$ mv ./sample/SampleParticle.hpp ./path/to/your/cocos2dx/proj/Classes/
$ mv ./sample/SampleParticle.cpp ./path/to/your/cocos2dx/proj/Classes/
```

in C++.
```cpp
#include "SampleParticle.hpp"

void func(Scene *scene) {
  auto particle = Sample::Effects::SampleParticle::create();
  particle->setPosition(Point(320, 640));
  particle->resetSystem();
  scene->addChild(particle);
}

```


# Project Configuration
<dl>
  <dt>./p2c4cocos</dt>
  <dd>
    Execution script.
    (this is alias to "./src/particle_to_code.py".)
  </dd>

  <dt>./src/particle_to_code.py</dt>
  <dd>main code of the p2c4cocos</dd>

  <dt>./src/cpp</dt>
  <dd>Scripts for C++ code generation.</dd>

</dl>
