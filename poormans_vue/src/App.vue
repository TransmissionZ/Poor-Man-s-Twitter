<template>
  <!--  <img alt="Vue logo" src="./assets/logo.png" />-->
  <nav class="navbar navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img
          src="./assets/logo.png"
          alt=""
          width="30"
          height="20"
          class="d-inline-block align-text-top"
        />
        Poor Man's Twitter
      </a>
    </div>
  </nav>
  <TweetsAdd msg="" @update="updateTweets" />
  <br />
  <br />
  <TweetsTable :tweets="tweets" />
</template>

<script>
import TweetsAdd from "@/components/TweetsAdd";
import TweetsTable from "@/components/TweetsTable";
import { getUpdateAPI } from "@/axios-api";

export default {
  name: "App",
  components: {
    TweetsAdd,
    TweetsTable,
  },
  data() {
    return {
      tweets: [],
    };
  },
  created() {
    this.updateTweets();
  },
  methods: {
    async updateTweets() {
      await getUpdateAPI
        .get("/tweets/")
        .then((response) => {
          console.log("Data Recieved");
          this.tweets = response.data;
          this.tweets.forEach(function (items, idx, theArr) {
            // console.log(items.dt)
            var d = new Date(items.dt);
            theArr[idx].dt =
              d.toISOString().slice(0, 10) +
              " " +
              d.toISOString().slice(11, 19);
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
