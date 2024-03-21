<script setup>
import AppCard from '@/components/AppCard.vue';
import TravelDisplay from '@/components/TravelDisplay';
import TravelForm from '@/components/TravelForm.vue';
import WarningModal from '@/components/WarningModal.vue';
import { PhVan } from '@phosphor-icons/vue';
import { ref } from 'vue';

const travelOptions = ref({});
const showErrorModal = ref(false);
const errorMessage = ref('');

function onFormSuccess(bestOption, cheapestOption) {
  travelOptions.value.best = bestOption;
  travelOptions.value.cheapest = cheapestOption;
}

function onFormError(message) {
  errorMessage.value = message;
  showErrorModal.value = true;
  travelOptions.value = {};
}
</script>

<template>
  <main class="w-full px-8 py-10">
    <AppCard class="w-full">
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

    <WarningModal
      v-if="showErrorModal"
      @modal-close="showErrorModal = !showErrorModal"
      :message="errorMessage"
    />
  </main>
</template>
