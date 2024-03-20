<script setup>
const props = defineProps({
  showHeader: {
    default: true,
    required: false,
    type: Boolean,
  },
});
</script>

<template>
  <div class="bg-plain-lighter w-full rounded shadow-lg">
    <div
      class="bg-secondary px-8 py-4 rounded-t text-white font-semibold"
      v-if="props.showHeader"
    >
      <slot name="header"></slot>
    </div>
    <div class="p-4"><slot></slot></div>
  </div>
</template>
