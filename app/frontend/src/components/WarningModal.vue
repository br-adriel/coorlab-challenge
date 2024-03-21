<script setup>
import Modal from '@/components/Modal.vue';
import { BIconExclamationSquare } from 'bootstrap-icons-vue';

const emit = defineEmits(['modal-close']);
const props = defineProps({ message: String });
</script>

<template>
  <Modal @modal-close="$emit('modal-close')">
    <div
      class="flex flex-col items-center gap-4 px-10 lg:px-20 py-5 max-w-[450px]"
    >
      <BIconExclamationSquare class="text-6xl text-primary" />
      <p class="text-xl text-center text-plain-typography font-medium">
        {{ props.message }}
      </p>
      <button
        type="button"
        @click="$emit('modal-close')"
        class="bg-primary text-secondary cursor-pointer py-1 px-12 font-bold rounded hover:brightness-110 transition-all"
      >
        Fechar
      </button>
    </div>
  </Modal>
</template>
