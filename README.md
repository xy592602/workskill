# My AI Workbench

个人 AI 工作流程合集：图片版式、批量变体、花字素材和求职准备。

## 五个能力

| Skill | 输入 | 输出 | 来源 |
| --- | --- | --- | --- |
| [poster-layout](skills/poster-layout/SKILL.md) | 文案、素材、风格要求 | 母版和质检记录 | 从上传的 a2-direct-image 通用化整理 |
| [image-variants](skills/image-variants/SKILL.md) | 母版、配色、版式、文案 | 组合清单、图片及逐张检查 | 从 image-copy-batch 通用化整理；本版清单脚本新编写 |
| [flower-materials](skills/flower-materials/SKILL.md) | 文案、样式、用途 | 透明底花字、审核台账 | 从 flower-material-library 通用化整理 |
| [interview-workbench](skills/interview-workbench/SKILL.md) | 项目材料、JD、招聘者问题 | 证据核实、沟通回复、技术追问 | 本项目新增的求职工作流 |
| [job-resume-tailor](skills/job-resume-tailor/SKILL.md) | 简历和JD | 匹配分析、简历调整、面试准备 | 第三方开源 skill，保留原文和许可证 |

## 如何使用

将选定 skill 的整个文件夹放入所用 Agent 支持的技能目录，或明确要求 Agent 阅读该文件夹的 SKILL.md 并执行。图片任务需要宿主环境提供生图/编辑工具、文件读写与图片查看能力。求职任务需要简历/JD读取能力；外网调研依赖联网工具。

本仓库是一组执行工作流，不是独立运行的数字人服务，也未实现后台自动监控。没有调用图片工具时不会自行生成图片。

### 无API演示：规划8张变体

在仓库根目录执行（Python 3.10+，标准库，无需密钥）：
```bash
python skills/image-variants/scripts/build_manifest.py skills/image-variants/references/plan.example.json outputs/manifest.json
python -m unittest discover -s tests -v
```

输出8条计划：1母版×2配色×2版式×2文案。输出只是待执行任务，不代表8张图已生成。重复运行不会覆盖已有清单。

### 对话演示

- “用 interview-workbench 核对这段项目描述，再帮我回复招聘者，分清现有实现和方案。”

- “用 poster-layout 根据这份文案生成一张3:4知识卡，逐字核对后给我母版。”
- “用 image-variants 按这份计划生成变体；先规划8张，保留原风格，记录每张结果。”
- “用 flower-materials 生成‘周末去公园’的三款透明底花字，在亮暗背景检查。”
- “用 job-resume-tailor 对照我的简历分析这份JD，区分直接证据、可迁移经验和缺口。”

## 求职工作流

新增 `interview-workbench` 聚焦工程师的项目证据与面试沟通，包含事实表模板和完整虚构示例。它可独立使用，不依赖原版 `job-resume-tailor`。后者继续保留，用于通用岗位匹配、简历调整和面试准备。

新工作流已做格式与引用检查，示例为手工编写；尚未进行独立模型评测或真实投递验证。

## 设计取舍

- 文案与参考图分开管理，防止模型沿用旧字或删减正文。
- 明确每个组合的来源和文件名，防止批量生成漏项、重项。
- 技术质检、人工审核、送审数量分开，避免把生成数量当作交付数量。
- 已确认失败与结果未知分开处理，避免盲目重复提交。
- 原始业务资料留在私有目录，公开仓库只保留通用规则与虚构示例。

## 验证与限制

本次可自动验证的是任务清单的组合、输入校验、命名和覆盖保护。图片生成、文字准确性、透明边缘与模型效果仍需实际执行和逐张验收；本版未运行收费图片生成，也没有把历史业务结果当作本仓库测试结果。

[来源与改动](docs/provenance.md) · [演示流程](docs/demo.md)
