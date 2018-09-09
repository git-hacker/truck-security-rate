<template>
  <div class="detail-container" v-if="this.ready==true">
    <header class="banner">
      <img class="banner-bg" src="../assets/img/detail-banner.png" alt="banner">
      <div class="title">
        <img class="driver-avatar" :src="driverDetail.d_avatar" alt="avatar">
        <div class="driver-info">
          <span>{{driverDetail.d_name}}</span>
        </div>
        <div class="licence">
          {{driverDetail.t_plate.replace('#', '川A-').toUpperCase()}}
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
    <div class="category">{{this.category}}</div>
    <div class="score">  
      <div class="sub-score ">
        <div class="sub-title">人物指数</div>
        <CircleChart chartsName="driver-chart" :score="this.masterScore"></CircleChart>
      </div>
      <div class="sub-score">
        <div class="sub-title">卡车指数</div>
        <CircleChart chartsName="truck-chart" :score="this.truckScore"></CircleChart>
      </div>
    </div>
    
    <div class="detail-list">
      <DetailItem 
      title= "酣然入梦"
        color= "#73D13D"
        :icon= "require('@/assets/img/water.png')"
        :content= "`休息比：${parseInt(this.driverDetail.avg_rest*100)}%`"
        :updesc= "`运送：${this.driverDetail.nbr_trip}次`"
        :downdesc= "`休息：${parseInt(this.driverDetail.nbr_trip *  this.driverDetail.avg_rest)}次`">
      </DetailItem>
      <DetailItem         
        title= "知法知律"
        color= "#FFC53D"
        :content= "`安全度：${this.security}%`"
        :icon= "require('@/assets/img/security.png')"
        :updesc= "`违章：${this.driverDetail.nbr_violations}次`"
        :downdesc= "`事故：${this.driverDetail.nbr_accident}次`">
      </DetailItem>
      <DetailItem         
        title= "久经沙场"
        color= "#40A9FF"
        :content= "`平均里程：${this.avaDistance}km`"
        :icon= "require('@/assets/img/speed.png')"
        :updesc= "`里程：${parseInt(this.driverDetail.total_dist_drive)} km`"
        :downdesc= "`天数：${this.driverDetail.nbr_days_drive}`">
      </DetailItem>
      <DetailItem         
        title= "稳如泰山"
        color= "#13C2C2"
        :content= "`平均载重：${parseInt(this.driverDetail.avg_weight/1000)}吨`"
        :icon= "require('@/assets/img/data.png')"
        updesc= "载重吨位："
        :downdesc= "`${parseInt(this.driverDetail.t_maxload/1000)}吨`">
      </DetailItem>
      <DetailItem         
        title= "动力十足"
        color= "#722ED1"
        :content= "`车龄：${parseInt(this.driverDetail.truck_age)}天`"
        :icon= "require('@/assets/img/truck.png')"
        updesc= "保养次数："
        :downdesc= "`${this.driverDetail.nbr_truck_maintenance}次`">
      </DetailItem>
      <DetailItem         
        title= "弹性满满"
        color= "#D46B08"
        :content= "`轮胎磨损：${this.tyreScore}%`"
        :icon= "require('@/assets/img/tire.png')"
        updesc= "更换时间："
        :downdesc= "this.latestChangeTyle">
      </DetailItem>
    </div>
  </div>
</template>

<script>
import DetailItem from "../components/DetailItem.vue";
import CircleChart from "../components/CircleChart.vue";
export default {
  name: "detail",
  components: {
    DetailItem,
    CircleChart
  },
  beforeCreate () {
    const driverId = this.$route.query.driverId;
    this.$http.get(`${this.$serverUrl}/detail?_id=${driverId}`).then((res) => {
      this.driverDetail = res.data;
      if (!res.data){
        alert("can not get detail data!")
        return
      } else {
        this.truckScore = parseInt(res.data.truck_score * 100)
        this.masterScore = parseInt(res.data.master_score * 100);
        this.ready = true;
      }
    })
  },
  data() {
    return {
      driverDetail: {},
      truckScore: 0,
      masterScore: 0,
      ready: false
    };
  },
  computed: {
    totleScore() {
      return ((this.driverDetail.truck_score + this.driverDetail.master_score)*100/2).toFixed(1) ;
    },
    security() {
     return ((1-(this.driverDetail.nbr_violations + this.driverDetail.nbr_accident)/2/this.driverDetail.nbr_trip)*100).toFixed(1)
    },
    category() {
      if (this.totleScore >= 75 ) return '安全可靠';
      else if (this.totleScore >= 50) return '值得信赖'
      else if (this.totleScore >= 25) return '有待改进'
      else return '马路杀手'
    },
    avaDistance() {
      return (this.driverDetail.total_dist_drive / this.driverDetail.nbr_days_drive).toFixed(0);
    },
    latestChangeTyle() {
      return new Date(this.driverDetail.latest_tyre_change.$date).toISOString().split('T')[0]
    },
    tyreScore() {
      return parseInt((this.driverDetail.tyre_unchanged_time / 200) * 100);
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
    font-size:18px;
    font-family:PingFangSC-Light;
    font-weight:300;
    text-align: center;
    position: absolute;
    bottom: 23%;
    left: 0;
    right: 0;
    .licence {
      font-size:24px;
      font-family:PingFangSC-Regular;
      font-weight:400;
      color:rgba(255,255,255,1);
      line-height:33px;
      letter-spacing:3px;
    }
    .driver-avatar {
      height: 70px;
      width: 70px;
      border-radius: 50%;
      border: solid 7px white;
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
  margin-bottom: 20px;
}

.score {
  display: flex;
  justify-content: space-between;
  padding: 0 5%;
  text-align: left;
  align-items : center;
  .sub-score {
    text-align: center;
  }
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
