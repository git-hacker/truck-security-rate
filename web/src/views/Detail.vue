<template>
  <div class="detail-container">
    <header class="banner">
      <img class="banner-bg" src="../assets/img/detail-banner.png" alt="banner">
      <div class="title left">
        <div class="sub-title licence">
          {{driverDetail.licenceNum}}
        </div>
        <div class="driver-info">
          <img class="driver-avatar" :src="driverDetail.driverAvatar" alt="avatar">
          <span>{{driverDetail.driverName}}</span>
        </div>
      </div>
      <div class="title right">
        <div class="sub-title">总评分</div>
        <div class="totle-score">{{totleScore}}</div>
      </div>
    </header>
    <div class="score">
      <!-- todo -->
    </div>
    <div class="detail-list">
      <DetailItem 
      titl= "酣然入梦"
        color= "#95DE64"
        :icon= "require('@/assets/img/water.png')"
        updesc= "运送"
        downdesc= "休息">
      </DetailItem>
      <DetailItem         
        titl= "知法知律"
        color= "#FFD666"
        :icon= "require('@/assets/img/security.png')"
        updesc= "违章"
        downdesc= "事故">
      </DetailItem>
      <DetailItem         
        titl= "久经沙场"
        color= "#69C0FF"
        :icon= "require('@/assets/img/speed.png')"
        updesc= "里程"
        downdesc= "天数">
      </DetailItem>
      <DetailItem         
        titl= "稳如泰山"
        color= "#36CFC9"
        :icon= "require('@/assets/img/data.png')"
        updesc= "载重吨位："
        downdesc= "40吨">
      </DetailItem>
            <DetailItem         
        titl= "动力十足"
        color= "#722ED1"
        :icon= "require('@/assets/img/truck.png')"
        updesc= "保养次数："
        downdesc= "String">
      </DetailItem>
      <DetailItem         
        titl= "弹性满满"
        color= "#D46B08"
        :icon= "require('@/assets/img/tire.png')"
        updesc= "更换时间："
        downdesc= "String">
      </DetailItem>

    </div>
  </div>
</template>

<script>
import DetailItem from "../components/DetailItem.vue";
import testData from "../assets/data/driver-detail.json";
export default {
  name: "detail",
  components: {
    DetailItem
  },
  data() {
    return {
      driverDetail: testData,
      
    };
  },
  computed: {
    totleScore() {
      return (this.driverDetail.driverScore + this.driverDetail.truckScore) / 2;
    }
  }
};
</script>


<style lang="stylus" scoped>
.banner {
  width: 100%;
  position: relative;

  .banner-bg {
    width: 100%;
    height: auto;
  }

  .title {
    color: white;
    text-align: left;
    position: absolute;
    bottom: 20px;

    &.left {
      left: 5%;

      .driver-avatar {
        height: 39px;
        width: 39px;
        border-radius: 50%;
      }
    }

    &.right {
      right: 5%;
    }
  }
}

.score {
  width: 100%;
  height: 55vw;
  // background-image: url('../assets/img/scoure-bg.png');
  // background-size: 100% 104%;
  // background-repeat: no-repeat;
}

</style>
