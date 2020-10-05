<template>
    <v-container pa-0>
        <div id="tabs">
            <button v-for="(tab, index) in tabs" :key=index
            :class="{active: currentTab === index}"
            @click="currentTab = index"> {{tab}}</button>

            <div id="TabContent">
                <div v-show="currentTab==0"> 
                    <v-layout column>     
                        <span style="font-size:20pt;">
                            <img src="../assets/insta.png" height="20px" width="20px">&nbsp;instagram 인기 키워드</span>
                            <v-divider class="mb-5" ></v-divider>
                        <v-flex class="white">
                            <word-cloud></word-cloud>
                        </v-flex>
                    </v-layout>     
                </div>
                <div v-show="currentTab==1">
                    <v-layout column>
                        <span style="font-size:20pt;">사람들은 지금..?</span>
                        <v-divider class="mb-5" ></v-divider>
                        <v-list three-line style="max-height: calc(100vh - 260px)" class="overflow-y-auto">
                        <v-list-item v-for="(item, i) in items" v-bind:key="i">
                            <img src="../assets/covidRemove.png" height="30px" width="30px">&nbsp;
                                {{item.value}}
                        </v-list-item>
                        </v-list>
                    </v-layout>
                </div>
                <div v-show="currentTab==2"> 
                    <v-layout column>
                        <span style="font-size:20pt;">코로나 한눈에 확인하기</span>
                        <v-divider class="mb-5" ></v-divider>
                    </v-layout>
                    <v-layout row class="small"><bar-chart></bar-chart></v-layout>
                    <v-layout row>
                        <v-flex xs3 class="middle"><doughnut-chart></doughnut-chart></v-flex>
                        <v-flex xs3 class="middle"><doughnut-chart></doughnut-chart></v-flex>
						<v-flex xs3 class="middle"><doughnut-chart></doughnut-chart></v-flex>
                    </v-layout>
                </div>
            </div>
        </div>
    </v-container>
</template>

<script>
import WordCloud from "../components/WordCloud"
import DoughnutChart from "../components/Chart/DoughnutChart"
import BarChart from "../components/Chart/BarChart"

export default {
	components: {
        WordCloud,
		BarChart,
		DoughnutChart
    },
    data() {
        return {
            items: [],
            currentTab : 0,
            tabs: ['HOT 키워드', 'sns 파악하기', '코로나 정보']
        }
    },
    mounted() {
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
    }
};
</script>

<style scoped>
	@font-face { 
    font-family: 'Maple'; 
    src: url(../assets/font/Maplestory_Bold.ttf) format('truetype')
		,url(../assets/font/Maplestory_Light.ttf) format('truetype'); 
	}

    button {
		background-color: rgb(120, 120, 120);
        color: white;
        margin-right: 2px;
        padding: 2px 9px;
        border-radius: 15px 15px 0 0;
		outline: none;
		box-shadow: none;
		font-family: Maple;
    }
	button:hover {
		padding-top: 10px;
		border-radius: 15px 15px 0 0;
		background-color:#f08c8c;
		transition: all 1s;
	}
	.active {
		padding-top: 10px;
		border-radius: 15px 15px 0 0;
		background-color: #f08c8c;
		transition: all 1s;
	}
    #TabContent {
        border: 1px solid gray;
    }
	span {
		padding: 20px;
		font-family: Maple;
	}
	.small {
		width: 35%;
		height: 20%;
		margin: 0 auto;
		padding: 0;
 	}
	.middle {
		width: 20%;
		height: 20%;
		margin: 30px auto;
		padding: 0;
 	}
</style>