<template>
  <v-footer
    dark
    padless
  >
    <v-card
      flat
      tile
      color="#F44336"
      class="white--text text-center"
      width="100%"
    >
      <v-card-text width class="white--text pt-10">
        여기는 Footer 입니다 
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>COSAT</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>