<script setup>
import FormLabel from '@/components/FormLabel.vue';
import { api } from '@/lib/axios';
import { PhHandCoins } from '@phosphor-icons/vue';
import { BIconCalendar4Week } from 'bootstrap-icons-vue';
import { onMounted, ref } from 'vue';

const emit = defineEmits(['success', 'error']);

const options = ref([]);

const isStarting = ref(true);
const isLoading = ref(false);

async function formSubmit(form) {
  isLoading.value = true;

  try {
    if (!form.data.city || !form.data.date) {
      throw new Error('Insira os valores para realizar a cotação.');
    }

    const { data } = await api.post('/travels/options', form.data);
    emit('success', data.best_option, data.cheapest_option);
  } catch (err) {
    emit('error', err.message || 'Um erro ocorreu');
  } finally {
    isLoading.value = false;
  }
}

onMounted(async () => {
  try {
    const { data } = await api.get('/travels/destinations');
    options.value = data;
  } catch (err) {
    options.value = [];
  } finally {
    isStarting.value = false;
  }
});
</script>

<template>
  <div class="bg-plain-darker text-plain-typography rounded-lg px-8 py-28">
    <h2 class="flex items-center gap-2 font-bold text-lg mb-8">
      <PhHandCoins size="32" weight="bold" />
      <span>Calcule o Valor da Viagem</span>
    </h2>

    <Vueform :float-placeholders="false" :endpoint="false" @submit="formSubmit">
      <SelectElement
        name="city"
        id="city"
        :items="options"
        placeholder="Selecione o destino"
        :native="false"
        :loading="isStarting"
      >
        <template #label>
          <FormLabel label="Destino" for="city" />
        </template>
      </SelectElement>

      <DateElement
        placeholder="Selecione uma data"
        name="date"
        id="date"
        :min="new Date().toJSON().slice(0, 10)"
        value-format="YYYY-MM-DD"
      >
        <template #label>
          <FormLabel label="Data" for="date" />
        </template>
        <template v-slot:addon-after>
          <BIconCalendar4Week />
        </template>
      </DateElement>

      <div class="h-5"></div>

      <ButtonElement
        :submits="true"
        align="center"
        name=""
        size="sm"
        :loading="isLoading"
      >
        <span class="text-secondary font-bold">Buscar</span>
      </ButtonElement>
    </Vueform>
  </div>
</template>
