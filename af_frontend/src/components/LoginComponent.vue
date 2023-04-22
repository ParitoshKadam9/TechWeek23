<template>
  <div class="login">
    <h1>Login</h1>
    <input type="email" placeholder="Enter Email" v-model="email" />
    <input type="password" placeholder="Enter Password" v-model="password" />
    <button @click="login">Submit</button>
    <p>
      <router-link to="signup" class="tag">New User? Sign Up </router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
      console.log(this.email);
      this.$router.push({name : 'HomeComponent'})
    },
  },
};
</script>

<style>
.login input {
  width: 300px;
  height: 40px;
  display: block;
  padding-left: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  margin-top: 20px;
  border: 1px solid steelblue;
}

.login button {
  width: 320px;
  height: 40px;
  background: steelblue;
  border-color: 1px solid steelblue;
  color: white;
  cursor: pointer;
}

.tag {
  text-decoration: none;
  color: black;
}

.login h1 {
  margin-top: 150px;
}

</style>
