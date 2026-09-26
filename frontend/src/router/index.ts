import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Windmill = () => import('@/views/windmill/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Blade = () => import('@/views/blade/index.vue')
const Gearbox = () => import('@/views/gearbox/index.vue')
const Generation = () => import('@/views/generation/index.vue')
const Substation = () => import('@/views/substation/index.vue')
const Sparepart = () => import('@/views/sparepart/index.vue')
const Transformer = () => import('@/views/transformer/index.vue')
const Tower = () => import('@/views/tower/index.vue')
const Cable = () => import('@/views/cable/index.vue')
const Foundation = () => import('@/views/foundation/index.vue')
const Lightning = () => import('@/views/lightning/index.vue')
const Meteorology = () => import('@/views/meteorology/index.vue')
const Dispatching = () => import('@/views/dispatching/index.vue')
const Site = () => import('@/views/site/index.vue')
const Contract = () => import('@/views/contract/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Envmonitor = () => import('@/views/envmonitor/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/windmill', name: 'windmill', component: Windmill },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/blade', name: 'blade', component: Blade },
    { path: '/gearbox', name: 'gearbox', component: Gearbox },
    { path: '/generation', name: 'generation', component: Generation },
    { path: '/substation', name: 'substation', component: Substation },
    { path: '/sparepart', name: 'sparepart', component: Sparepart },
    { path: '/transformer', name: 'transformer', component: Transformer },
    { path: '/tower', name: 'tower', component: Tower },
    { path: '/cable', name: 'cable', component: Cable },
    { path: '/foundation', name: 'foundation', component: Foundation },
    { path: '/lightning', name: 'lightning', component: Lightning },
    { path: '/meteorology', name: 'meteorology', component: Meteorology },
    { path: '/dispatching', name: 'dispatching', component: Dispatching },
    { path: '/site', name: 'site', component: Site },
    { path: '/contract', name: 'contract', component: Contract },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/envmonitor', name: 'envmonitor', component: Envmonitor },
  ],
})

export default router
