<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">风力发电场运维管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向风电场风机巡检、叶片维修、发电量监测、升压站管理、备件调配与运维调度的一体化风电场运维管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "风机台账", path: "/windmill" }, { label: "巡检任务", path: "/patrol" }, { label: "叶片维修", path: "/blade" }, { label: "齿轮箱养护", path: "/gearbox" }, { label: "发电记录", path: "/generation" }, { label: "升压站管理", path: "/substation" }, { label: "备件调配", path: "/sparepart" }, { label: "箱变监测", path: "/transformer" }, { label: "塔筒检测", path: "/tower" }, { label: "集电线路", path: "/cable" }, { label: "基础沉降", path: "/foundation" }, { label: "防雷检测", path: "/lightning" }, { label: "气象测风", path: "/meteorology" }, { label: "调度指令", path: "/dispatching" }, { label: "场区管理", path: "/site" }, { label: "运维合同", path: "/contract" }, { label: "安全工器具", path: "/safety" }, { label: "环境监测", path: "/envmonitor" }]
</script>
