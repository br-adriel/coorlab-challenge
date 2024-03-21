<script setup>
import { timeStringToHours } from '@/utils/time';
import TravelPrice from './TravelPrice.vue';
import TravelIcon from './TravelIcon.vue';
import clsx from 'clsx';

const props = defineProps({
  travel: Object,
  cheapestOption: Boolean,
});
</script>

<template>
  <div class="flex gap-2 text-plain-typography">
    <div
      :class="
        clsx({
          'rounded w-2/3 flex items-center': true,
          'bg-travel-lighter': cheapestOption,
          'bg-travel-darker': !cheapestOption,
        })
      "
    >
      <TravelIcon :cheapestOption="cheapestOption" />
      <div class="flex-grow px-4 py-2 text-sm text-plain-typography">
        <h3 class="font-bold mb-0.5">{{ travel.name }}</h3>

        <p v-if="cheapestOption">Poltrona: {{ travel.seat }} (Convencional)</p>
        <p v-else>Leito: {{ travel.bed }} (Completo)</p>

        <p>Tempo estimado: {{ timeStringToHours(travel.duration) }}</p>
      </div>
    </div>

    <TravelPrice
      :price="cheapestOption ? travel.price_econ : travel.price_confort"
      :darker-variant="!cheapestOption"
    />
  </div>
</template>
