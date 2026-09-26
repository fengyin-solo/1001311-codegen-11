"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class WindmillEntry(BaseModel):
    """风机明细结构。"""

    field_0: str | None = None  # 风机编号
    field_1: str | None = None  # 机型型号
    field_2: str | None = None  # 额定功率
    field_3: str | None = None  # 安装日期
    field_4: str | None = None  # 所属场区
    field_5: str | None = None  # 轮毂高度
    field_6: str | None = None  # 叶轮直径
    field_7: str | None = None  # 运行状态

class PatrolEntry(BaseModel):
    """巡检任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡检类型
    field_2: str | None = None  # 指派班组
    field_3: str | None = None  # 巡检日期
    field_4: str | None = None  # 覆盖区域
    field_5: str | None = None  # 风机数量
    field_6: str | None = None  # 完成情况
    field_7: str | None = None  # 巡检结论

class BladeEntry(BaseModel):
    """叶片维修单明细结构。"""

    field_0: str | None = None  # 维修单号
    field_1: str | None = None  # 风机编号
    field_2: str | None = None  # 损伤类型
    field_3: str | None = None  # 损伤位置
    field_4: str | None = None  # 维修方案
    field_5: str | None = None  # 维修人员
    field_6: str | None = None  # 预计工时
    field_7: str | None = None  # 实际工期

class GearboxEntry(BaseModel):
    """齿轮箱养护单明细结构。"""

    field_0: str | None = None  # 养护编号
    field_1: str | None = None  # 风机编号
    field_2: str | None = None  # 养护级别
    field_3: str | None = None  # 润滑油型号
    field_4: str | None = None  # 更换滤芯
    field_5: str | None = None  # 养护班组
    field_6: str | None = None  # 计划日期
    field_7: str | None = None  # 完工日期

class GenerationEntry(BaseModel):
    """发电记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 风机编号
    field_2: str | None = None  # 当日发电量
    field_3: str | None = None  # 平均风速
    field_4: str | None = None  # 并网时长
    field_5: str | None = None  # 记录日期
    field_6: str | None = None  # 限电损失
    field_7: str | None = None  # 审核人

class SubstationEntry(BaseModel):
    """升压站设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 电压等级
    field_3: str | None = None  # 所属升压站
    field_4: str | None = None  # 上次检修日
    field_5: str | None = None  # 运行参数
    field_6: str | None = None  # 继保装置
    field_7: str | None = None  # 设备状态

class SparepartEntry(BaseModel):
    """备件明细结构。"""

    field_0: str | None = None  # 备件编号
    field_1: str | None = None  # 备件名称
    field_2: str | None = None  # 适用机型
    field_3: str | None = None  # 保有数量
    field_4: str | None = None  # 存放库位
    field_5: str | None = None  # 补货阈值
    field_6: str | None = None  # 上次调配日
    field_7: str | None = None  # 备件状态

class TransformerEntry(BaseModel):
    """箱变明细结构。"""

    field_0: str | None = None  # 箱变编号
    field_1: str | None = None  # 所属风机
    field_2: str | None = None  # 油温上限
    field_3: str | None = None  # 绕组温度
    field_4: str | None = None  # 负载率
    field_5: str | None = None  # 环境温度
    field_6: str | None = None  # 采样时间
    field_7: str | None = None  # 运行状态

class TowerEntry(BaseModel):
    """塔筒检测单明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 风机编号
    field_2: str | None = None  # 检测项目
    field_3: str | None = None  # 检测方法
    field_4: str | None = None  # 检测人员
    field_5: str | None = None  # 检测日期
    field_6: str | None = None  # 焊缝等级
    field_7: str | None = None  # 检测结论

class CableEntry(BaseModel):
    """集电线路明细结构。"""

    field_0: str | None = None  # 线路编号
    field_1: str | None = None  # 线路名称
    field_2: str | None = None  # 电压等级
    field_3: str | None = None  # 起止端点
    field_4: str | None = None  # 敷设方式
    field_5: str | None = None  # 线路长度
    field_6: str | None = None  # 投运日期
    field_7: str | None = None  # 线路状态

class FoundationEntry(BaseModel):
    """基础监测点明细结构。"""

    field_0: str | None = None  # 监测编号
    field_1: str | None = None  # 风机编号
    field_2: str | None = None  # 基准点高程
    field_3: str | None = None  # 本次高程
    field_4: str | None = None  # 沉降量
    field_5: str | None = None  # 累计沉降
    field_6: str | None = None  # 监测日期
    field_7: str | None = None  # 监测结论

class LightningEntry(BaseModel):
    """防雷检测单明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 检测对象
    field_2: str | None = None  # 接地电阻值
    field_3: str | None = None  # 防雷等级
    field_4: str | None = None  # 检测人员
    field_5: str | None = None  # 检测日期
    field_6: str | None = None  # 上次检测日
    field_7: str | None = None  # 结论判定

class MeteorologyEntry(BaseModel):
    """测风塔明细结构。"""

    field_0: str | None = None  # 测风塔编号
    field_1: str | None = None  # 风速瞬时
    field_2: str | None = None  # 风向角度
    field_3: str | None = None  # 大气温度
    field_4: str | None = None  # 大气气压
    field_5: str | None = None  # 空气密度
    field_6: str | None = None  # 采集时间
    field_7: str | None = None  # 数据状态

class DispatchingEntry(BaseModel):
    """调度指令明细结构。"""

    field_0: str | None = None  # 指令编号
    field_1: str | None = None  # 指令类型
    field_2: str | None = None  # 下发单位
    field_3: str | None = None  # 执行对象
    field_4: str | None = None  # 下发时间
    field_5: str | None = None  # 执行期限
    field_6: str | None = None  # 功率目标
    field_7: str | None = None  # 执行状态

class SiteEntry(BaseModel):
    """场区明细结构。"""

    field_0: str | None = None  # 场区编号
    field_1: str | None = None  # 场区名称
    field_2: str | None = None  # 占地面积
    field_3: str | None = None  # 风机数量
    field_4: str | None = None  # 装机容量
    field_5: str | None = None  # 并网日期
    field_6: str | None = None  # 责任人
    field_7: str | None = None  # 运营状态

class ContractEntry(BaseModel):
    """运维合同明细结构。"""

    field_0: str | None = None  # 合同编号
    field_1: str | None = None  # 供应商名称
    field_2: str | None = None  # 服务范围
    field_3: str | None = None  # 合同金额
    field_4: str | None = None  # 起止日期
    field_5: str | None = None  # 付款节点
    field_6: str | None = None  # 履约保证
    field_7: str | None = None  # 履约进度

class SafetyEntry(BaseModel):
    """安全工器具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具名称
    field_2: str | None = None  # 规格型号
    field_3: str | None = None  # 上次校验日
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 保管人
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 器具状态

class EnvmonitorEntry(BaseModel):
    """环境监测点明细结构。"""

    field_0: str | None = None  # 监测点编号
    field_1: str | None = None  # 噪声分贝
    field_2: str | None = None  # 振动加速度
    field_3: str | None = None  # 环境温度
    field_4: str | None = None  # 环境湿度
    field_5: str | None = None  # 采集时间
    field_6: str | None = None  # 排放指标
    field_7: str | None = None  # 处置状态
