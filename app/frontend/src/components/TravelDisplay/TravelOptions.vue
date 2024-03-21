<script setup>
import TravelInfo from './TravelInfo.vue';

const props = defineProps({
  best: Object,
  cheapest: Object,
});
</script>

<template>
  <div class="w-full">
    <p class="w-2/3 mb-3">
      Essas são as melhores alternativas de viagem para a data selecionada
    </p>
    <TravelInfo :travel="best" class="mb-3" />
    <TravelInfo :travel="cheapest" :cheapest-option="true" />
  </div>
</template>
