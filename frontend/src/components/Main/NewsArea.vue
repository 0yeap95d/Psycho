<template>
    <v-card :height="windowHeight">
        <v-card-text>
            뉴스 카드
        </v-card-text>
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