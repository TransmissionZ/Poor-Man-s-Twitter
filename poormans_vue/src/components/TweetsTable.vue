<template>
  <table v-if="tweets.length" class="table table-striped table-dark">
    <thead>
      <tr>
        <!--        <th scope="col" style="width:10%">ID</th>-->
        <th scope="col">Name</th>
        <th scope="col">Tweet</th>
        <th scope="col">Time Posted</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in tweets" :key="row.id">
        <!--        <th scope="row" style="width:10%">{{ row.id }}</th>-->
        <td style="width: 20%">{{ row.name }}</td>
        <td style="width: 60%">{{ row.tweet }}</td>
        <td style="width: 20%">{{ row.dt }}</td>
      </tr>
    </tbody>
  </table>
  <h3 class="heading" v-else>0 tweets, add now or come back later.</h3>
</template>

<script>
export default {
  name: "TweetsTable",
  props: {
    tweets: Array,
  },
};
</script>

<style scoped></style>
