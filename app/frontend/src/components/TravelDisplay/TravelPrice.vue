<script setup>
import { moneyFormatter } from '@/utils/intl';
import clsx from 'clsx';

const props = defineProps({
  darkerVariant: Boolean,
  price: Number,
});
</script>

<template>
  <div
    :class="
      clsx({
        'rounded w-1/3 flex flex-col justify-center p-4 text-sm': true,
        'bg-travel-lighter': !darkerVariant,
        'bg-travel-darker': darkerVariant,
      })
    "
  >
    <p class="font-bold">Preço</p>
    <p>
      {{ moneyFormatter.format(price) }}
    </p>
  </div>
</template>
