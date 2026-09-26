"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import windmill as router_windmill
from app.routers import patrol as router_patrol
from app.routers import blade as router_blade
from app.routers import gearbox as router_gearbox
from app.routers import generation as router_generation
from app.routers import substation as router_substation
from app.routers import sparepart as router_sparepart
from app.routers import transformer as router_transformer
from app.routers import tower as router_tower
from app.routers import cable as router_cable
from app.routers import foundation as router_foundation
from app.routers import lightning as router_lightning
from app.routers import meteorology as router_meteorology
from app.routers import dispatching as router_dispatching
from app.routers import site as router_site
from app.routers import contract as router_contract
from app.routers import safety as router_safety
from app.routers import envmonitor as router_envmonitor

ROUTERS = [router_windmill, router_patrol, router_blade, router_gearbox, router_generation, router_substation, router_sparepart, router_transformer, router_tower, router_cable, router_foundation, router_lightning, router_meteorology, router_dispatching, router_site, router_contract, router_safety, router_envmonitor]
