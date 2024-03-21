<script setup>
import TravelOptions from './TravelOptions.vue';

const props = defineProps({
  best: Object,
  cheapest: Object,
});
</script>

<template>
  <div class="min-h-[300px] h-full w-full flex-grow flex items-center">
    <p v-if="!props.best && !props.cheapest" class="text-center w-full">
      {{
        props.best === undefined
          ? 'Nenhum dado selecionado.'
          : 'Nenhuma opção encontrada para a data selecionada.'
      }}
    </p>
    <TravelOptions v-else :best="best" :cheapest="cheapest" />
  </div>
</template>
