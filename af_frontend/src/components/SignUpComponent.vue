<template>
  <div class="signup">
    <h1>SignUp</h1>
    <input type="text" placeholder="Enter BITSID" v-model="bits_id" required />
    <input
      type="text"
      placeholder="Enter Username"
      v-model="username"
      required
    />
    <input
      type="password"
      placeholder="Enter Password"
      v-model="password"
      required
    />
    <input
      type="text"
      placeholder="Enter Full Name"
      v-model="full_name"
      required
    />
    <button @click="Signup">Sign Up</button>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      bits_id: "",
      username: "",
      password: "",
      full_name: "",
      karma: 0,
    };
  },
  methods: {
    Signup() {
      console.log(this.bits_id);
      this.$router.push({name : 'HomeComponent'})
    },
  },
};
</script>

<style>
.signup input {
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

.signup button {
  width: 320px;
  height: 40px;
  background: steelblue;
  border-color: 1px solid steelblue;
  color: white;
  cursor: pointer;
}

.signup h1 {
  margin-top: 150px;
}
</style>
