<template>
  <v-carousel cycle :height="windowHeight" hide-delimiters>
    <v-carousel-item>
      <v-img src="../../assets/hero02.png">
        <div class="display-3">{{ slide }} Slide???</div>
      </v-img>
    </v-carousel-item>

    <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <v-sheet height="100%">
        <v-row> SLIDE </v-row>
        <v-row class="fill-height" align="center" justify="center">
          <v-img src="../../assets/hero01.png">
            <div class="display-3">{{ slide }} Slide</div>
          </v-img>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      windowHeight: window.innerHeight,
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4",
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
    };
  },
};
</script>

<style>
.v-image__image {
  opacity: 0.6;
}
</style>