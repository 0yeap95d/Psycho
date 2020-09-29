<template>
  <div id="app">
    <cloud 
        :data="words" 
        :fontSizeMapper="fontSizeMapper"
        :width="width"
        :height="height"
    />
  </div>
</template>
 
<script>
import Cloud from 'vue-d3-cloud'
 
export default {
    name: 'app',
    data() {
        return {
            width: 1161,
            height: 600,
            words:[],
            fontSizeMapper: word => Math.log2(word.value) * 5,
        }
    },
    created() {
        this.getWordCloud()
    },
    methods: {
        getWordCloud() {
            let wordList = new Array;
            d3.csv("insta_keyword.csv", function(error, data) {
                if(error) throw error;
                for(var i = 0; i < data.length; i++){
                    wordList.push({text: data[i].코로나, value: data[i][58] * 100})
                }
            });
            this.words = wordList;
        }
    },
    components: {
        Cloud,
    },
}
</script>