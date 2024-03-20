<script setup>
import { RouterView } from 'vue-router';
import AppSidebar from '@/components/AppSidebar.vue';
</script>

<template>
  <div class="lg:flex bg-plain-medium shadow">
    <div class="lg:w-1/4">
      <AppSidebar />
    </div>
    <RouterView />
  </div>
</template>

<style scoped></style>
