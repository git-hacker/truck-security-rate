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
    </header>
    <div class="score">
      <div class="score-title">
        <div class="sub-title">安全值评估</div>
        <div class="totle-score">{{totleScore}}<span>分</span></div>
      </div>
      <img src="@/assets/img/security-badge.png" alt="security-badge">
    </div>
    <div class="category">值得信赖</div>
    <div class="score">
      
      <div class="truck-score"></div>
      
      <div class="driver-score"></div>
    </div>
    
    <div class="detail-list">
      <DetailItem 
      title= "酣然入梦"
        color= "#73D13D"
        :icon= "require('@/assets/img/water.png')"
        :content= "`休息比：${90}%`"
        updesc= "运送次数："
        downdesc= "休息次数：">
      </DetailItem>
      <DetailItem         
        title= "知法知律"
        color= "#FFC53D"
        :content= "`安全度：${95}%`"
        :icon= "require('@/assets/img/security.png')"
        updesc= "违章次数："
        downdesc= "事故次数：">
      </DetailItem>
      <DetailItem         
        title= "久经沙场"
        color= "#40A9FF"
        :content= "`平均里程：${360}km`"
        :icon= "require('@/assets/img/speed.png')"
        updesc= "里程："
        downdesc= "天数：">
      </DetailItem>
      <DetailItem         
        title= "稳如泰山"
        color= "#13C2C2"
        :content= "`平均载重：${90}吨`"
        :icon= "require('@/assets/img/data.png')"
        updesc= "载重吨位："
        :downdesc= "`${40}吨`">
      </DetailItem>
      <DetailItem         
        title= "动力十足"
        color= "#722ED1"
        :content= "`车龄：${4}年`"
        :icon= "require('@/assets/img/truck.png')"
        updesc= "保养次数："
        :downdesc= "`${3}次`">
      </DetailItem>
      <DetailItem         
        title= "弹性满满"
        color= "#D46B08"
        :content= "`轮胎磨损：${20}%`"
        :icon= "require('@/assets/img/tire.png')"
        updesc= "更换时间："
        :downdesc= "`${new Date().toISOString().split('T')[0]}`">
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
  margin-bottom: 10px;

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

.category {
  font-size:36px;
  font-family:PingFangSC-Semibold;
  font-weight:600;
  color:rgba(155,155,155,0.3);
  line-height:50px;
  letter-spacing:2px;
}

.score {
  display: flex;
  justify-content: space-between;
  padding: 0 5%;
  text-align: left;
  align-items : center;
  img {
    width: 88px;
    height: 88px;
  }
  .sub-title {
    font-size:18px;
    font-family:PingFangSC-Regular;
    font-weight:400;
    color:rgba(19,116,230,1);
    line-height:25px;
    letter-spacing:2px;
  }
  .totle-score {
    font-size:48px;
    font-family:PingFangSC-Semibold;
    font-weight:600;
    color:rgba(54,207,201,1);
    line-height:67px;
    letter-spacing:2px;
    span {
      font-size: 16px;
      font-weight: normal;
    }
  }
}

</style>
