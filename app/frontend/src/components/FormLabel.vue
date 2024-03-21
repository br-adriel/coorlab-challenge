<script setup>
const props = defineProps({
  label: String,
  for: String,
});
</script>

<template>
  <label :for="props.for" class="font-bold text-sm">{{ props.label }}</label>
</template>
