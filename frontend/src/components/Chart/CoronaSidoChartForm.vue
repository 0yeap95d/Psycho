<template>
  <div id="ChartForm">
    <corona-age-chart :chart-data="ChartData" />
    <input id="date" v-model="date" type="date" />
  </div>
</template>

<script>
import CoronaAgeChart from "./CoronaAgeChart";
import CoronaApi from "../../api/CoronaApi";

export default {
  components: {
    CoronaAgeChart,
  },
  data: () => {
    return {
      date: null,
      data: null,
      ChartData: {},
    };
  },
  watch: {
    date: function () {
      this.getChart();
    },
  },
  mounted() {
    this.date = this.getFormatDate(new Date("2020-09-01"));
    this.getChart();
  },
  methods: {
    getFormatDate(date) {
      var year = date.getFullYear();
      var month = 1 + date.getMonth();
      month = month >= 10 ? month : "0" + month;
      var day = date.getDate();
      day = day >= 10 ? day : "0" + day;
      return year + "-" + month + "-" + day;
    },
    getChart() {
      let d = this.date.split("-");
      this.data = {
        syear: d[0] * 1,
        smonth: d[1] * 1,
        sday: d[2] * 1,
        eyear: d[0] * 1,
        emonth: d[1] * 1,
        eday: d[2] * 1,
        gubun: "",
      };
      this.getDatasets(this.data);
    },
    getDatasets(data) {
      CoronaApi.requestCoronaSido(
        data,
        (res) => {
          console.log(res);
          this.ChartData = {
            labels: [
              "서울",
              "부산",
              "대구",
              "인천",
              "광주",
              "대전",
              "울산",
              "세종",
              "경기",
              "강원",
              "충북",
              "충남",
              "전북",
              "전남",
              "경북",
              "경남",
              "제주",
            ],
            datasets: [
              {
                label: "일별 증가 확진자",
                backgroundColor: "#8c8cf4",
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              },
            ],
          };
          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i].gubun == "서울") {
              this.ChartData.datasets[0].data[0] = res.data[i].incDec;
            } else if (res.data[i].gubun == "부산") {
              this.ChartData.datasets[0].data[1] = res.data[i].incDec;
            } else if (res.data[i].gubun == "대구") {
              this.ChartData.datasets[0].data[2] = res.data[i].incDec;
            } else if (res.data[i].gubun == "인천") {
              this.ChartData.datasets[0].data[3] = res.data[i].incDec;
            } else if (res.data[i].gubun == "광주") {
              this.ChartData.datasets[0].data[4] = res.data[i].incDec;
            } else if (res.data[i].gubun == "대전") {
              this.ChartData.datasets[0].data[5] = res.data[i].incDec;
            } else if (res.data[i].gubun == "울산") {
              this.ChartData.datasets[0].data[6] = res.data[i].incDec;
            } else if (res.data[i].gubun == "세종") {
              this.ChartData.datasets[0].data[7] = res.data[i].incDec;
            } else if (res.data[i].gubun == "경기") {
              this.ChartData.datasets[0].data[8] = res.data[i].incDec;
            } else if (res.data[i].gubun == "강원") {
              this.ChartData.datasets[0].data[9] = res.data[i].incDec;
            } else if (res.data[i].gubun == "충북") {
              this.ChartData.datasets[0].data[10] = res.data[i].incDec;
            } else if (res.data[i].gubun == "충남") {
              this.ChartData.datasets[0].data[11] = res.data[i].incDec;
            } else if (res.data[i].gubun == "전북") {
              this.ChartData.datasets[0].data[12] = res.data[i].incDec;
            } else if (res.data[i].gubun == "전남") {
              this.ChartData.datasets[0].data[13] = res.data[i].incDec;
            } else if (res.data[i].gubun == "경북") {
              this.ChartData.datasets[0].data[14] = res.data[i].incDec;
            } else if (res.data[i].gubun == "경남") {
              this.ChartData.datasets[0].data[15] = res.data[i].incDec;
            } else if (res.data[i].gubun == "제주") {
              this.ChartData.datasets[0].data[16] = res.data[i].incDec;
            }
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
};
/*
요청 json 형식
{
    "syear": 2020, //시작년도
    "smonth": 9, //시작월
    "sday": 4, //시작일
    "eyear": 2020, //끝년도
    "emonth": 9, //끝월
    "eday": 4, //끝일
}
*/
</script>

<style scoped>
#date {
  margin-top: 10px;
}
#ChartForm {
  text-align: center;
  width: 33%;
  height: 430px;
}
</style>