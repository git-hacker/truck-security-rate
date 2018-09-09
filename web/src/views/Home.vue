<template>
  <div class="home-container">
    <header class="banner">
      <img src="@/assets/img/banner.png" alt="banner">
      <div class="banner-title">
        <h2>卡车司机安全评估</h2>
        <div>找到放心司机</div>
      </div>
      <el-input
        class="search-input"
        placeholder="请输入内容"
        prefix-icon="el-icon-search"
        v-model="searchInput"
        :clearable="true">
      </el-input>
    </header>
    <content class="home-content">
      <driver-card v-for="(item, index) in filterDiiverList" 
        :key = "index" 
        :driverId="item._id.$oid" 
        :driverName="item.d_name" 
        :driverAvatar="item.d_avatar" 
        :driverScore="((item.master_score + item.truck_score)*100/2).toFixed(1)">
      </driver-card>
    </content>
  </div>
</template>

<script>
// @ is an alias to /src
import DriverCard from "@/components/DriverCard.vue";
import driverList from "@/assets/data/driver-list.json"

export default {
  name: "home",
  components: {
    DriverCard
  },
  mounted () {
    this.$http.get(`${this.$serverUrl}/homepage`).then((res) => {
      this.driverList = res.data;
    })
  },
  data() {
    return {
      searchInput: "",
      driverList: driverList
    };
  },
  computed: {
    filterDiiverList() {
      if(this.searchInput == "") {
        return this.driverList;
      } else {
        return this.driverList.filter((item) => {
          return item.driverName.includes(this.searchInput);
        })
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
div.home-container {
  display: flex;
  flex-direction: column;
  .banner {
    position: fixed;
    background-color: white;
    padding-bottom: 10px;
    
    z-index: 2;
    top: 0;
    width: 100%;
    .banner-title{
      position: absolute;
      color: white;
      right: 3%;
      top: 100px;
      text-align: left;
      h2{
        font-size:24px;
        font-family:PingFangSC-Semibold;
        font-weight:600;
        color:rgba(255,255,255,1);
        line-height:33px;
        letter-spacing:1px;
        margin: 0;
      }
      div{
        font-size:18px;
        font-family:PingFangSC-Light;
        font-weight:300;
        color:rgba(255,255,255,1);
        line-height:25px;
        letter-spacing:1px;
      }

    }
    img {
      width: 100%;
      height: auto;
    }
  }
}
.home-content {
  margin-top: 300px;
  display: flex;
  flex-direction : column;
  align-items : center;
  padding: 0 3%;
  overflow-y: scroll;
}

</style>

<style lang="stylus">
   .search-input {
      width: 343px;
      height: 36px;
      overflow: hidden;
      border-radius: 10px;
      color: #8E8E93;
      input {
        background: rgba(142, 142, 147, 0.12);
        border: none;
      }
    }
</style>

