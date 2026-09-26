# 风力发电场运维管理平台

面向风电场风机巡检、叶片维修、发电量监测、升压站管理、备件调配与运维调度的一体化风电场运维管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 风机台账 | `windmill` | 风机 | 风机编号、机型型号、额定功率 |
| 巡检任务 | `patrol` | 巡检任务 | 任务编号、巡检类型、指派班组 |
| 叶片维修 | `blade` | 叶片维修单 | 维修单号、风机编号、损伤类型 |
| 齿轮箱养护 | `gearbox` | 齿轮箱养护单 | 养护编号、风机编号、养护级别 |
| 发电记录 | `generation` | 发电记录 | 记录编号、风机编号、当日发电量 |
| 升压站管理 | `substation` | 升压站设备 | 设备编号、设备名称、电压等级 |
| 备件调配 | `sparepart` | 备件 | 备件编号、备件名称、适用机型 |
| 箱变监测 | `transformer` | 箱变 | 箱变编号、所属风机、油温上限 |
| 塔筒检测 | `tower` | 塔筒检测单 | 检测编号、风机编号、检测项目 |
| 集电线路 | `cable` | 集电线路 | 线路编号、线路名称、电压等级 |
| 基础沉降 | `foundation` | 基础监测点 | 监测编号、风机编号、基准点高程 |
| 防雷检测 | `lightning` | 防雷检测单 | 检测编号、检测对象、接地电阻值 |
| 气象测风 | `meteorology` | 测风塔 | 测风塔编号、风速瞬时、风向角度 |
| 调度指令 | `dispatching` | 调度指令 | 指令编号、指令类型、下发单位 |
| 场区管理 | `site` | 场区 | 场区编号、场区名称、占地面积 |
| 运维合同 | `contract` | 运维合同 | 合同编号、供应商名称、服务范围 |
| 安全工器具 | `safety` | 安全工器具 | 器具编号、器具名称、规格型号 |
| 环境监测 | `envmonitor` | 环境监测点 | 监测点编号、噪声分贝、振动加速度 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
