<template>
  <div class="hello">
    <br />
    <br />
    <form class="row g-3 p-3" v-on:submit.prevent="submitForm">
      <div class="col-md-2">
        <input
          type="text"
          class="form-control"
          placeholder="Name"
          aria-label="Name"
          v-model="form.name"
        />
      </div>
      <div class="col-md-8">
        <input
          type="text"
          class="form-control"
          placeholder="Tweet Text"
          maxlength="50"
          aria-label="Tweet Text"
          v-model="form.tweet"
        />
      </div>
      <button type="submit" class="col-md-2 btn btn-primary">Tweet</button>
    </form>
  </div>
</template>

<script>
import { getUpdateAPI } from "@/axios-api";

export default {
  name: "TweetsAdd",
  props: {
    msg: String,
  },
  data() {
    return {
      form: {
        name: "",
        tweet: "",
      },
    };
  },
  methods: {
    submitForm() {
      getUpdateAPI
        .post("/tweets/", this.form)
        .then((res) => {
          console.log("Added " + res);
          this.$emit("update", "ok");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
