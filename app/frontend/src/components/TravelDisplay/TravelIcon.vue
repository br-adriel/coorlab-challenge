<script setup>
import { PhClock, PhHandCoins } from '@phosphor-icons/vue';

const props = defineProps({
  cheapestOption: Boolean,
});
</script>

<template>
  <div
    class="bg-primary px-4 py-6 rounded-l text-white h-full flex items-center"
  >
    <PhClock size="32px" v-if="props.cheapestOption" />
    <PhHandCoins size="32px" v-else />
  </div>
</template>
