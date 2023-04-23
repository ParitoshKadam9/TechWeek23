<template>
    
    <div class="Sidebar">

    </div>

    <div class="Home">
        <div class="Search">
            <input :class="!up ? 'searchBar' : 'searchBarUp'" placeholder="Search Communities" v-model="search"
                @change="ChangeSearch(search)" />
        </div>
        <div class="CreateCommunity">
                <div class="button" @click="this.addcomm = !this.addcomm">+ Create Community</div>
                <div v-if="addcomm" >
                    <AddCommunity></AddCommunity> 
                </div>
            </div>
            <div class="BasicStats">
                    <div class="line">
                        #{{ this.$store.state.community.communities.length }} Communities around the world
                    </div>

                </div>
            </div>
            <div v-for="community in this.$store.state.community.communities" v-bind:key="community.id">
                    <CommunitiesBox v-bind:title="community.title" :cid="community.id"></CommunitiesBox>
                </div>
                <div class="profile" v-if="this.$store.state.isLoggedIn">
            </div>
</template>
<script>
import { mapActions } from 'vuex'
import CommunitiesBox from '@/components/CommunitiesBox.vue'
import AddCommunity from '@/components/AddCommunity.vue'

export default {
    name: "HomeView",
    components: {
        CommunitiesBox,
        AddCommunity
    },
    data() {
        return {
            search: "",
            up: false,
            addcomm: false
        }
    },
    methods: {
        ...mapActions({
            GetCommunities: 'GetCommunities',
            CreateCommunity: 'CreateCommunity',
            DeleteCommunity: 'DeleteCommunity'
        }),
        ChangeSearch(sea) {
            console.log(sea)
            if (sea == "") {
                console.log('helu')
                this.up = false
            }
            else {
                console.log('909')
                this.up = true
            }
        }
    },
    mounted() {
        this.GetCommunities();
    }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.button {
    min-width: 20vh;
    cursor: pointer;
    padding: 1.5vh;
    color: white;
    font-size: 2.5vh;
    margin-top: 5vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 5vh;
    border-radius: 5px;
    justify-content: center;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background: rgb(176, 176, 31);
    transition: 0.1s ease-in;
}

.button:hover {
    background: rgba(188, 188, 8, 0.442);
}

.line {
    font-size: 6vh;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: white;
    margin-top: 15vh;
}

.Home {
    margin: 0;
    padding: 0;
    width: 70vw;
    margin-left: auto;
    margin-right: auto;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    background: rgb(36, 36, 36);
    /* justify-content: center; */
}

.searchBar {
    border: 1px solid gray;
    border-radius: 5px;
    background-color: rgb(36, 36, 36);
    color: gray;
    height: 5vh;
    width: 50vh;
    padding: 10px;
    font-size: 2.6vh;
    margin-top: 10vh;
    transition: 0.2s;
}

.searchBarUp {
    border: 1px solid gray;
    border-radius: 5px;
    background-color: rgb(34, 34, 34);
    color: gray;
    height: 5vh;
    width: 50vh;
    padding: 10px;
    font-size: 2.6vh;
    margin-top: 10vh;
    transition: 0.2s;
}

@keyframes GoUp {
    0% {
        margin-top: 0vh;
    }

    100% {
        margin-top: 5vh;
    }

}

:-moz-placeholder {
    text-align: center;
}</style>