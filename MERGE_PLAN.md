# AI-policy-Agent 合并计划

## 1. 当前主项目

主目录：

- app/
- frontend/
- data/
- scripts/
- application_workflows/
- policy_schemas/
- tests/

## 2. Incoming 来源

### _incoming/AI-policy-Agent-from-projects

来源：/Users/shajindi/projects/AI-policy-Agent

初步判断：
- 包含 app/ 后端结构
- 包含 frontend/
- 包含 policy_schemas/
- 包含 application_workflows/
- 包含 docker-compose.yml、package.json、requirements.txt
- 更像早期完整产品原型

### _incoming/ai-policy-platform

来源：workspace 中已有 ai-policy-platform

初步判断：
- 包含 backend/
- 包含 frontend/
- 包含 docs/
- 包含 sample policies / sample companies / sample parks
- 更像政策平台 Demo

### _incoming/ai-policy-platform-from-projects

来源：/Users/shajindi/projects/ai-policy-platform

初步判断：
- 与 _incoming/ai-policy-platform 高度相似
- 需要比较是否完全重复

## 3. 合并目标结构

```text
AI-policy-Agent/
├── apps/
│   ├── api/
│   └── web/
├── packages/
│   ├── rag/
│   ├── agents/
│   ├── policy_db/
│   └── reporting/
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── docs/
├── scripts/
├── tests/
├── archive/
└── _incoming/
