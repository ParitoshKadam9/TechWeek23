<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" />
        <div class="wrapper" >
            <input type="checkbox" id="btn" hidden>
            <label for="btn" class="menu-btn">
                <i class="fas fa-bars"></i>
                <i class="fas fa-times"></i>
            </label>
            <nav id="sidebar">
                <div class="title">Side Menu</div>
                <ul class="list-items">
                    <li><router-link to="/">Home</router-link></li>
                    <li><router-link to="/profile">Profile</router-link></li>
                            <li ><router-link to="/login" @click="logout" v-if="!this.$store.state.isLoggedIn">Log In</router-link></li>
                            <li ><router-link to="/login" @click="logout" v-if="this.$store.state.isLoggedIn">LogOut</router-link></li>
                        </ul>
                    </nav>
                </div>
</template>

<script>

export default {
    methods: {
        open() {
            document.getElementById("main").style.marginLeft = "25%";
            document.getElementById("mySidebar").style.width = "25%";
            document.getElementById("mySidebar").style.display = "block";
            document.getElementById("openNav").style.display = 'none';
            console.log('Open')
        },
        close() {
            document.getElementById("main").style.marginLeft = "0%";
            document.getElementById("mySidebar").style.display = "none";
            document.getElementById("openNav").style.display = "inline-block";
        },
        logout() {
            this.$store.state.isLoggedIn = false
        }
    },
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.wrapper {
    height: 100%;
    width: 300px;
    position: relative;
}

.wrapper .menu-btn {
    position: absolute;
    left: 20px;
    top: 10px;
    background: #4a4a4a;
    color: #fff;
    height: 45px;
    width: 45px;
    z-index: 9999;
    border: 1px solid #333;
    border-radius: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

#btn:checked~.menu-btn {
    left: 247px;
}

.wrapper .menu-btn i {
    position: absolute;
    transform: -200px;
    font-size: 23px;
    transition: all 0.3s ease;
}

.wrapper .menu-btn i.fa-times {
    opacity: 0;
}

#btn:checked~.menu-btn i.fa-times {
    opacity: 1;
    transform: rotate(-180deg);
}

#btn:checked~.menu-btn i.fa-bars {
    opacity: 0;
    transform: rotate(180deg);
}

#sidebar {
    position: fixed;
    background: #404040;
    height: 100%;
    width: 270px;
    overflow: hidden;
    left: -270px;
    transition: all 0.3s ease;
}

#btn:checked~#sidebar {
    left: 0;
}

#sidebar .title {
    line-height: 65px;
    text-align: center;
    background: #333;
    font-size: 25px;
    font-weight: 600;
    color: #f2f2f2;
    border-bottom: 1px solid #222;
}

#sidebar .list-items {
    position: relative;
    background: #404040;
    width: 100%;
    height: 100%;
    list-style: none;
}

#sidebar .list-items li {
    padding-left: 40px;
    line-height: 50px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid #333;
    transition: all 0.3s ease;
}

#sidebar .list-items li:hover {
    border-top: 1px solid transparent;
    border-bottom: 1px solid transparent;
    box-shadow: 0 0px 10px 3px #222;
}

#sidebar .list-items li a {
    color: #f2f2f2;
    text-decoration: none;
    font-size: 18px;
    font-weight: 500;
    height: 100%;
    width: 100%;
    display: block;
}

#sidebar .list-items li a i {
    margin-right: 20px;
}
</style>