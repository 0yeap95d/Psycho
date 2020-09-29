<template>
    <v-card :height="windowHeight">
        <v-layout align-center justify-center>
            <v-flex>
                현재 상태
            </v-flex>
        </v-layout>
    </v-card>
</template>

<script>
  export default {
    data () {
      return {
        windowHeight: window.innerHeight,
      }
    },
  }
</script>