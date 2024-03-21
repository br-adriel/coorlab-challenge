<script setup>
import AppCard from '@/components/AppCard.vue';

const emit = defineEmits(['modalClose']);
</script>

<template>
  <div
    class="bg-gray-500 bg-opacity-50 fixed h-full w-full overflow-y-auto overflow-x-hidden top-0 left-0 p-5 z-50"
    @click="$emit('modalClose')"
  >
    <div class="flex items-center justify-center min-h-full">
      <AppCard :show-header="false" class="w-auto rounded-lg">
        <slot></slot>
      </AppCard>
    </div>
  </div>
</template>
