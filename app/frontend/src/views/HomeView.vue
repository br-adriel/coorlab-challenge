<script setup>
import AppCard from '@/components/AppCard.vue';
import TravelForm from '@/components/TravelForm.vue';
import TravelDisplay from '@/components/TravelDisplay';
import { PhVan } from '@phosphor-icons/vue';
import { ref } from 'vue';

const travelOptions = ref({});

function onFormSuccess(bestOption, cheapestOption) {
  travelOptions.value.best = bestOption;
  travelOptions.value.cheapest = cheapestOption;
  console.log(bestOption);
  console.log(cheapestOption);
}

function onFormError(message) {
  // TODO: show modal
  travelOptions.value = {};
}
</script>

<template>
  <main class="w-full px-8 py-10">
    <AppCard>
      <template #header>
        <div class="flex items-center gap-2">
          <PhVan :size="24" />
          <h1>Calculadora de Viagem</h1>
        </div>
      </template>

      <div class="flex flex-col lg:flex-row">
        <div class="lg:w-5/12">
          <TravelForm @error="onFormError" @success="onFormSuccess" />
        </div>
        <div class="lg:w-7/12 px-6">
          <TravelDisplay
            :best="travelOptions.best"
            :cheapest="travelOptions.cheapest"
          />
        </div>
      </div>
    </AppCard>
  </main>
</template>
