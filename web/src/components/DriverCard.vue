<template>
  <router-link :to="`/driver-detail/${driverId}`" class="card-container">
      <div class="driver-card">
      <img :src="driverAvatar" class="driver-avatar" alt="avatar"/>
      <div class='driver-name'>{{driverName}}</div>
      <div class="driver-score">{{driverScore}}<small>分</small></div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'DriverCard',
  props: {
    driverId: String,
    driverAvatar: String,
    driverName: String,
    driverScore: Number
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="stylus" scoped>
.card-container{
  width: 100%;
  text-decoration: none;
  color: auto;
}
  div.driver-card{
    width: 94%;
    height:80px;
    background:rgba(255,255,255,1);
    box-shadow:0px 2px 5px 0px rgba(0,0,0,0.1);
    border-radius:10px;
    display: flex;
    justify-content: space-between;
    align-items : center;
    padding: 0 2%;
    margin-top: 15px;
    img.driver-avatar{
      width: auto;
      height: 90%;
      border-radius : 50%;
      border: solid #D7E4FF 5px ;
    }
    .driver-name {
      font-size:24px;
      font-family:PingFangSC-Regular;
      font-weight:400;
      color:rgba(74,74,74,1);
      line-height:33px;
      letter-spacing:1px;
    }
    .driver-score {
      font-size:36px;
      font-family:PingFangSC-Semibold;
      font-weight:600;
      color:rgba(54,207,201,1);
      letter-spacing:2px;
      small{
        font-size: 16px;
        font-weight : normal;
      }
    }
  }
</style>
