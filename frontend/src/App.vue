<template>
  <v-app id="app">
    <toolbar />   
    <route-view />
    <go-top />
    <Footer />
  </v-app>
</template>

<script>
import Toolbar from "@/components/Toolbar";
import RouteView from "@/components/RouteView";
import GoTop from "@/components/GoTop";
import Footer from "@/components/Footer";

export default {
  components: {
    Toolbar,
    RouteView,
    GoTop,
    Footer
  },
};
</script>
