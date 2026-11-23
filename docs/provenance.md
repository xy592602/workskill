# 来源与改动

前三项由用户上传的 Codex skills.zip 中对应规则提炼。公开版重新组织为通用流程，未直接发布原始业务需求表、客户反馈图片、人像、旧电脑绝对路径或历史业务数量。

- a2-direct-image → poster-layout：保留文案权威来源、视觉分支、母版与变体边界、逐张校验；去掉特定品牌规则。
- image-copy-batch → image-variants：保留组合规划、样式锁定、逐项追踪与检查；本版重写通用清单脚本。未移植原有强绑定头像的合成脚本，也未复用自动读取特定服务商登录配置的脚本。
- flower-material-library → flower-materials：保留停产优先、真实透明、实拍叠加验收、审核与送审计数；去掉客户特定历史状态。
- flower-material-handoff 为原业务交接入口，不作为独立公开能力。
- job-resume-tailor 原样收录自 https://github.com/liheyuting/job-resume-tailor ，版本 156afea541117ab53128eecf36cabc90d4936056。其原作者版权与MIT许可证位于 skills/job-resume-tailor/LICENSE。此部分不属于原创技能。

通用化整理、新脚本和示例是本次新增工作，不声称是历史生产版本。前三项的原始权属未在压缩包中得到独立验证，因此暂未为整个仓库统一授予开源许可证；第三方skill遵循其自带许可证。

## 新增求职工作流

`interview-workbench` 是基于本项目需求新增编写的工作流、证据模板与虚构示例，重点是工程实现核实、中文招聘者回复和技术追问。它与原版 `job-resume-tailor` 独立存放；新增内容不改变原版的来源或许可。
