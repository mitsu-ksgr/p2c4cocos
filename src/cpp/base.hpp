/***************************************************************************//**
 *  @file   {FileName}
 *  @brief  Definition for the {ClassName} class.
 *
 *  @date   {GenerateTime}
 *  @autor  generated by {ScriptName} script.
 *          {ScriptName} written by Mitsu(https://github.com/mitsuaki-n).
 ******************************************************************************/
#ifndef {IncludeGuard}
#define {IncludeGuard}

#include "cocos2d.h"

{NamespaceBegin}

/**
 *  @brief  {ClassName} class is particle-system of
 *          generated by {ScriptName}.
 */
class {ClassName} : public cocos2d::ParticleSystemQuad
{{
public:
    static {ClassName}* create() {{
        {ClassName}* ret = new {ClassName}();
        if(ret && ret->init()) {{
            ret->autorelease();
        }} else {{
            CC_SAFE_DELETE(ret);
        }}
        return ret;
    }}

protected:
    {ClassName}(){{}}
    virtual ~{ClassName}(){{}}

    bool init() {{
        return initWithTotalParticles({TotalParticles});
    }}
    virtual bool initWithTotalParticles(int number_of_particles);

private:
    {ClassName}(const {ClassName} &) = delete;
    {ClassName} &operator = (const {ClassName} &) = delete;

}};

{NamespaceEnd}

#endif  // {IncludeGuard}
