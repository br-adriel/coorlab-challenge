<script setup>
import { CalculatorOutlined } from '@ant-design/icons-vue';
import { RouterLink } from 'vue-router';
import SidebarItem from './SidebarItem.vue';
</script>

<template>
  <div
    class="bg-secondary shadow-deep lg:shadow-none w-full lg:min-h-[100dvh] px-5"
  >
    <div class="container mx-auto">
      <RouterLink to="/" class="block py-5">
        <img
          src="@/assets/img/logo.png"
          alt="Logo da CB Viagens"
          width="160px"
          class="max-w-full"
        />
      </RouterLink>

      <nav class="hidden lg:flex flex-col gap-4 mt-6">
        <SidebarItem to="/">
          <CalculatorOutlined class="text-lg" />
          Calculadora de Viagem
        </SidebarItem>
      </nav>
    </div>
  </div>
</template>
