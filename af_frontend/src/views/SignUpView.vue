<template>
  <div class="signup">
    <div>SignUp</div>
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
      <input
        type="email"
        placeholder="Enter Email"
        v-model="email"
        required
      />
      <div>
      <button @click="Signup">Sign Up</button>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: "SignUpView",
  data() {
    return {
      bits_id: "",
      username: "",
      password: "",
      full_name: "",
      email: "",
    };
  },
  methods: {
    ...mapActions({
      SignUpUser: 'SignUpUser'
    }),

    Signup() {
      this.SignUpUser({
        'bits_id': this.bits_id,
        'u_name': this.username,
        'pwd': this.password,
        'full_name': this.full_name,
        'email': this.email
      })
      this.$router.push({ name: 'HomeView' })
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

.signup{
  color: white;
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
