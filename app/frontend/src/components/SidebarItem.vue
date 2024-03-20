<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  to: {
    required: true,
    type: String,
  },
});
</script>

<template>
  <RouterLink :to="props.to" class="text-white font-medium text-sm">
    <div class="flex items-baseline gap-2">
      <slot></slot>
    </div>
  </RouterLink>
</template>
