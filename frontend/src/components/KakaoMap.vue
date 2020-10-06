<template>
  <div id="kakaoMap">
    <div id="mapMain" :style="myStyle"></div>
  </div>
</template>

<script>
export default {
  name: "kakaoMap",
  props: {
    storeList: Array,
  },
  data() {
    return {
      myStyle: {
        height: "",
        width: "" 
      },
      map: "",
    };
  },
  created() {
    this.initSize();
  },

  watch: {
    storeList: function() {
      this.setMakers();
    }
  },

  mounted() {
    this.initMap();
    this.setMakers();
    this.setCurPosition();
  },

  methods: {
    initSize() {
      let myheight = window.innerHeight - 112;
      let mywidth = "100%";
      this.myStyle.height = myheight + "px";
      this.myStyle.width = mywidth;
    },
    initMap() {
      console.log("initMap");
      this.map = new kakao.maps.Map(document.getElementById("mapMain"), {
        // 지도를 표시할 div
        center: new kakao.maps.LatLng(36.2683, 127.6358), // 지도의 중심좌표
        level: 10, // 지도의 확대 레벨
      });
    },

    setMakers() {
      console.log("setMakers");

      // 마커 클러스터러를 생성합니다
      var clusterer = new kakao.maps.MarkerClusterer({
        map: this.map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
        averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
        minLevel: 10, // 클러스터 할 최소 지도 레벨
        calculator: [10, 30, 50], // 클러스터의 크기 구분 값, 각 사이값마다 설정된 text나 style이 적용된다
        texts: ["안전", "조금 안전", "조금 위험", "위험"], // texts는 ['삐약', '꼬꼬', '꼬끼오', '치멘'] 이렇게 배열로도 설정할 수 있다
        styles: [
          {
            // calculator 각 사이 값 마다 적용될 스타일을 지정한다
            width: "60px",
            height: "60px",
            background: "rgba(000, 153, 000, .8)",
            borderRadius: "30px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "61px",
          },
          {
            width: "50px",
            height: "50px",
            background: "rgba(102, 102, 255, .8)",
            borderRadius: "25px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "51px",
          },
          {
            width: "40px",
            height: "40px",
            background: "rgba(255, 153, 0, .8)",
            borderRadius: "20px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "41px",
          },
          {
            width: "30px",
            height: "30px",
            background: "rgba(255, 051, 051, .8)",
            borderRadius: "15px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "31px",
          },
        ],
      });

      var markers = this.storeList.map(function (store, i) {
        console.log(store.pos_x + " " + store.pos_y);
        return new kakao.maps.Marker( {
          position: new kakao.maps.LatLng(store.pos_y, store.pos_x),
        });
      });

      console.log(markers[0].position);

      clusterer.addMarkers(markers);
    },

    displayMarker(locPosition, message) {
      // 마커를 생성합니다
      var marker = new kakao.maps.Marker({
        map: this.map,
        position: locPosition,
      });

      var iwContent = message, // 인포윈도우에 표시할 내용
        iwRemoveable = true;

      // 인포윈도우를 생성합니다
      var infowindow = new kakao.maps.InfoWindow({
        content: iwContent,
        removable: iwRemoveable,
      });

      // 인포윈도우를 마커위에 표시합니다
      infowindow.open(this.map, marker);

      // 지도 중심좌표를 접속위치로 변경합니다
      this.map.setCenter(locPosition);
    },

    setCurPosition() {
      var displayMarker = this.displayMarker;
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
          var lat = position.coords.latitude; // 위도
          var lon = position.coords.longitude; // 경도

          var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            message = '<div style="padding:5px;">여기에 계신가요?!</div>'; // 인포윈도우에 표시될 내용입니다

          // 마커와 인포윈도우를 표시합니다
          displayMarker(locPosition, message);
        });
      } else {
        var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
          message = "geolocation을 사용할수 없어요..";

        this.displayMarker(locPosition, message);
      }
    },
  },
};
</script>