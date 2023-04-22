<template>
    <h1 v-if="this.$store.state.error.length">
        {{ this.$store.state.error }}
    </h1>
</template>

<script>
export default {
    name: 'ErrorBar',
}
</script>