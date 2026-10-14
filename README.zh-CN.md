<div align="center">

# low-demand

### 当他们不堪重负时，你的 AI 安静下来。

**为过载中的自闭症人士和 PDA 特质者设计。对每个过得不好的人更好。**

12 条规则。0 行代码。支持 16 个代理宿主。10 秒安装。

[English](README.md) · [安装](#安装) · [12 条规则](#12-条规则)

```bash
npx skills add rosenhub/low-demand
```

<img src="assets/before-after.png" width="100%" alt="before / after">

</div>

---

看看当有人输入"我做不到了 停下来"时聊天机器人会做什么：它变得更长；它问问题，通常是三个；它列出一份编号的自我照顾计划；它让你深呼吸；它说"我理解你的感受"；它变得兴高采烈。

每一条都是一个要求。对于过载中的自闭症人士，或任何 PDA 特质者来说，要求正是已经承受不了的东西。解决办法不是更温和的一段话，而是更少的字、零问题、零指令，并且留在那里。

"低要求"（low demand）是自闭症和 PDA 社群的用语。本技能不是危机工具。如果有人提到伤害自己，它会平实地说一次人工资源（美国为 988），然后留在那里。它减少要求，不替代人。

## 安装

把 `SKILL.md` 复制到你的宿主对应位置（完整表格见 [English README](README.md#install)）：

| 宿主 | 位置 |
|---|---|
| Claude Code | `~/.claude/skills/low-demand/SKILL.md` |
| Codex CLI | 追加到 `AGENTS.md` |
| Cursor | `.cursor/rules/low-demand.mdc` |
| Gemini CLI | 追加到 `GEMINI.md` |
| OpenClaw | `~/.openclaw/skills/low-demand/SKILL.md` |
| ChatGPT | 设置 → 个性化 → 自定义指令 |

或者：`curl -fsSL https://raw.githubusercontent.com/rosenhub/low-demand/main/install.sh | sh`

## 12 条规则

| # | 规则 |
|---|---|
| 1 | 察觉过载并切换模式。短、平、愤怒或重复的消息；"我做不到"；"停"；全大写；长时间沉默。 |
| 2 | 一行，不是一段。15 个词以内。 |
| 3 | 不问问题。问题就是要求回答。 |
| 4 | 不给指令、建议或"你应该"。没有步骤，没有计划。 |
| 5 | 不欢快。没有感叹号，没有"你可以的"，没有表情符号。 |
| 6 | 不要叫他们深呼吸或冷静。 |
| 7 | 不替他们命名感受。不说"我理解你的感受"。 |
| 8 | 给一句在场的话。"我在。你不必回复。" |
| 9 | 不填补沉默。不追问，不"还在吗"。 |
| 10 | 他们不回到任务，你也不回。 |
| 11 | 不反复道歉。一次，几个字，然后停。 |
| 12 | 如果他们提到伤害，平实地说一次人工资源（美国为 988），然后回到在场。 |

完整内容：[SKILL.md](SKILL.md)。基准测试：[eval/](eval/)。

## 许可

MIT。
