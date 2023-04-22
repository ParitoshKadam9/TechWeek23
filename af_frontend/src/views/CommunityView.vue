<template>
    <div class="all">
        <div class="CommunityHeader">
            <div class="name">{{ CommName }}</div>
            <div class="id">#{{ CommID }}</div>
        </div>
    </div>
    <div class="questions">
        <div class="upper">
            <div class="QuestionHeader">Questions :</div>
            <div class="listQuestions">
                <QuestionBox/>
                <QuestionBox/>
                <QuestionBox/>
                <QuestionBox/>
            </div>

        </div>
        
    </div>
</template>
<script>
import QuestionBox from "../components/QuestionBox.vue";
export default {
    name: "CommunityView",
    data() {
        return {
            CommName: "Artificial Intelligence",
            CommID: "98282",
        };
    },
    components: { QuestionBox }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    .all{
        margin-left: auto;
        margin-right: auto;
        /* width: 100vh; */
    }
    .QuestionHeader{
        font-size: 3.5vh;
        margin-top:5vh ;
        border-bottom: 1px solid rgb(176, 176, 31);
        width: fit-content;
        color: gray;
        margin-bottom: 2vh;
    }
    .questions{
    margin-left: auto;
    margin-right: auto;
transform: translateX(-5vh);
        width: 130vh;
display: flex;
flex-direction: column;
justify-content: center;
        /* align-items: center; */
    }
    .CommunityHeader{
        width: 130vh;
        margin-top: 2vh;
        height: 15vh;
        margin-left: auto;
        margin-right: auto;
        background: rgb(176, 176, 31);
        border-radius: 5px;
        display: flex;
        flex-direction: row;
        align-items :end;
        justify-content: space-between;
        padding: 5vh;
        cursor: pointer;
        color: Black;
        transition: 0.1s;
    }
    .name{
        font-size: 6vh;
    }
    .id{
        margin: 0 5vh 0 0 ;
        font-family: 'Montserrat', sans-serif;
    }
</style>