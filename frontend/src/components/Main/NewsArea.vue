<template>
  <v-card class="pa-5">
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :display="3"
      :width="windowWidth - 300"
      :height="windowHeight"
    >
      <slide v-for="(slide, i) in slides" :key="i" :index="i">
        <figure>
          <img src="https://picsum.photos/1920/1080?random" />
          <figcaption>
            The sky is the limit only for those who aren't afraid to fly! The
            sky is the limit only for those who aren't afraid to fly!
          </figcaption>
        </figure>
      </slide>
    </carousel-3d>
  </v-card>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  data() {
    return {
      windowWidth: window.innerWidth,
      windowHeight: window.innerHeight,
      slides: 7,
    };
  },
  components: {
    Carousel3d,
    Slide,
  },
};
</script>

<style>
.carousel-3d-container figure {
  margin: 0;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}
</style>
