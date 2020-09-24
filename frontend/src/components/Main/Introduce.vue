<template>
    <v-parallax
      dark
      src="https://picsum.photos/1920/1080?random"
      :height="windowHeight"
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col class="text-center" cols="12">
          <h1 class="display-1 font-weight-thin mb-4">싸이코</h1>
          <h4 class="subheading">싸우자 이기자 COVID-19</h4>
        </v-col>
      </v-row>
    </v-parallax>
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