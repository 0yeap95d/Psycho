<template>
    <v-container>
        <v-layout column>
            <span style="font-size:20pt;">
                <img src="../assets/insta.png" height="60px" width="60px">
                instagram 인기 키워드</span>
            <v-divider class="mb-5" ></v-divider>
            <v-flex class="white">
                <word-cloud></word-cloud>
            </v-flex>
        </v-layout>
        <v-layout column>
            <br><br>
            <span style="font-size:20pt;">원문 보기</span>
            <v-divider class="mb-5" ></v-divider>
            <v-list three-line style="max-height: calc(100vh - 100px)" class="overflow-y-auto">
                <v-list-item v-for="(item, i) in items" v-bind:key="i">
                    <img src="../assets/covidRemove.png" height="30px" width="30px">&nbsp;
                    {{item.value}}
                </v-list-item>
            </v-list>
        </v-layout>
        <v-layout column>
            <br><br>
            <span style="font-size:20pt;">차트</span>
            <v-divider class="mb-5" ></v-divider>
        </v-layout>
        <v-layout row>
            <v-flex col>
                <RandomChart></RandomChart>
            </v-flex>
            <v-flex col>
                <RandomChart></RandomChart>
            </v-flex>
            <v-flex col>
                <RandomChart></RandomChart>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import WordCloud from "../components/WordCloud"
import RandomChart from "../components/Chart/RandomChart"

export default {
    data() {
        return {
            items: []
        }
    },
    created() {
        this.getContents()
    },
    methods: {
        getContents() {
            let contentList = new Array;
            d3.csv("content.csv", function(error, data) {
                if(error) throw error;
                for(var i = 1; i < data.length; i++){
                    contentList.push({value: data[i][0]})
                }
            });
            this.items = contentList;
        }
    },
    components: {
        WordCloud,
        RandomChart
    }
};
</script>